import pytest
from pimp_my_engine.core.dtypes.circular_queue import CircularQueue

class TestCircularQueue(object):
    def test_circular_queue(self):
        cq = CircularQueue(size = 5)
        for x in range(5):
            cq.add(x)
        for x in range(5):
            assert cq.get(current = False, idx = x) == x

    def test_circular_queue_2(self):
        cq = CircularQueue(size = 5)
        elements = range(5)
        for x in elements:
            cq.add(x)
        elements = range(5,10)
        for x in elements:
            cq.add(x)
        for idx, x in enumerate(elements):
            assert cq.get(current = False, idx = idx) == x
        assert cq.get() == elements[-1]

