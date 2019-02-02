from threading import Lock

class DataQueue:
    ''' Shared object that contains data fetched by the OBD device '''
    def __init__(self):
        self.lock = Lock()
        self.queue = []

    def add(self, data):
        with self.lock:
            self.queue.append(data)

    def pop(self, idx = -1):
        with self.lock:
            return self.queue.pop(idx)

    def erase(self):
        with self.lock:
            self.queue = []

    def is_empty(self):
        with self.lock:
            return not bool(self.queue)
