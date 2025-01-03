import asyncio
import sys
import threading
from concurrent.futures import Future, ThreadPoolExecutor

from win32more.Windows.Win32.System.Com import IUnknown
from win32more.Windows.Win32.UI.WindowsAndMessaging import SetTimer


# Asyncio runner for Windows message loop.
def async_start_runner(delay_ms=100):
    def timer_proc(*args):
        loop._run_once()

    loop = asyncio.new_event_loop()
    loop.stop()
    loop._run_forever_setup()
    SetTimer(0, 0, delay_ms, timer_proc)


def async_callback(coroutine_function):
    def wrapper(*args):
        _addref(args)
        try:
            executor = RunningLoopTaskExecutor()
        except RuntimeError:
            executor = ThreadPoolTaskExecutor()
        future = executor.submit(coroutine_function(*args))
        future.add_done_callback(lambda _: _release(args))

    return wrapper


def _addref(args):
    for obj in args:
        if isinstance(obj, IUnknown) and obj.value:
            obj.AddRef()


def _release(args):
    for obj in args:
        if isinstance(obj, IUnknown) and obj.value:
            obj.Release()


class RunningLoopTaskExecutor:
    def __init__(self):
        self._loop = asyncio.get_running_loop()

    def submit(self, coro):
        task = self._create_task(self._loop, coro)
        return asyncio.run_coroutine_threadsafe(self._await_task(task), self._loop)

    async def _await_task(self, task):
        return await task

    def _create_task(self, loop, coro):
        if sys.version_info < (3, 12):
            return loop.create_task(coro)
        # Start task eagerly.
        # Some method can not be called after returned.
        # (e.g. CoreWebView2NewWindowRequestedEventArgs.GetDeferral())
        return asyncio.eager_task_factory(loop, coro)


class ThreadPoolTaskExecutor:
    _thread_pool = None
    _lock = threading.Lock()

    def __init__(self):
        self._init_thread_pool()

    @classmethod
    def _init_thread_pool(cls):
        if cls._thread_pool is None:
            with cls._lock:
                if cls._thread_pool is None:
                    cls._thread_pool = ThreadPoolExecutor()

    def submit(self, coro):
        loop = asyncio.new_event_loop()
        # start task eagerly in current thread context.
        # cannot use eager_task_factory because it requires running loop.
        task = loop.create_task(coro)
        loop.stop()
        loop.run_forever()
        if task.done():
            loop.run_until_complete(task)  # ensure calling done callback
            future = Future()
            future.set_result(task.result())
            return future
        # continue in background thread
        return self._thread_pool.submit(loop.run_until_complete, task)
