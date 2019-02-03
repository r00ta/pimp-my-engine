from threading import Lock
from pimp_my_engine.core.dtypes.circular_queue import CircularQueue

class ObdCollector:
    def __init__(self):
        self.commands_queues = {}

    def update(command, value):
        if command not in self.commands_queues.keys():
            self.commands_queues.update({command: CircularQueue(startvalue = value, size = 5)})
        else:
            self.commands_queues[command].add(value)

