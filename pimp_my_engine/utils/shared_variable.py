from threading import Lock

class SharedVariable:
    def __init__(self):
        self.lock = Lock()
        self.variable = None

    def set(self, value):
        with self.lock:
            self.variable = value

    def get(self):
        with self.lock:
            return self.variable

