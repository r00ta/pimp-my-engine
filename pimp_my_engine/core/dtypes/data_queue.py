from threading import Lock

class DataQueue:
    ''' Shared object that contains data fetched by the OBD device '''
    def __init__(self):
        self.lock = Lock()
        self.queue = []

    def add(self, data):
        try:
            self.lock.acquire()
            self.queue.append(data)
        finally:
            self.lock.release()

    def pop(self, idx = -1):
        try:
            self.lock.acquire()
            return self.queue.pop(idx)
        finally:
            self.lock.release()

    def erase(self):
        try:
            self.lock.acquire()
            self.queue = []
        finally:
            self.lock.release()

    def is_empty(self):
        try:
            self.lock.acquire()
            return not bool(self.queue)
        finally:
            self.lock.release()
