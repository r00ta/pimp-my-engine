class CircularQueue:
    def __init__(self, startvalue = None, size = 5):
        self.queue = [None]*size
        self.queue[0] = startvalue
        self.size = size
        self.current_idx = 0

    def add(value):
        self.current_idx = (self.current_idx + 1) % self.size
        self.queue[self.current_idx] = value
