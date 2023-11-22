import threading, enum
from PySide6.QtGui import QColor
from StatusMessage import StatusMessage

class ExecutorStatus(enum.Enum):
    AlreadyRunning = StatusMessage('Already running...', color=QColor('red'))
    Started = None



class AsyncExecutor(threading.Thread):
    def __init__(self, name:str, target_method, args=()):
        super().__init__()
        self.setName(name)
        self.target_method = target_method
        self.args = args

    def run(self):
        self.target_method(self.args)



class AsyncManager:
    _threads: list[AsyncExecutor] = []

    def _executeOnThread(self, method, args) -> ExecutorStatus:
        self._threads = [thread for thread in self._threads if not thread.is_alive]
        for thread in self._threads:
            if thread.getName() == method.__name__:
                return ExecutorStatus.AlreadyRunning

        thread = AsyncExecutor(method.__name__,method, args)
        thread.start()
        self._threads.append(thread)
        return ExecutorStatus.Started