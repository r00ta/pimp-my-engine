class CircularQueue:
    def __init__(self, startvalue = None, size = 5):
        self.queue = [None]*size
        self.size = size
        self.current_idx = -1
        if startvalue is not None:
            self.add(startvalue)

    def add(self, value):
        self.current_idx = (self.current_idx + 1) % self.size
        self.queue[self.current_idx] = value

    def get(self, current = True, idx = None):
        if not current and idx is None:
            raise Exception('Invalid parameters')
        if current:
            return self.queue[self.current_idx]
        else:
            return self.queue[idx]

