import pytest

from pimp_my_engine.core.dtypes.data_queue import DataQueue

class TestDataQueue(object):
    
    def test_add_and_pop(self):
        dq = DataQueue()
        element = [1,2,3]
        dq.add(element)
        element_queue = dq.pop()
        assert element_queue == element

    def test_add_different_types(self):
        dq = DataQueue()
        elements = ['a', [1,2,3], 2323]
        dq.add(elements[0])
        dq.add(elements[1])
        dq.add(elements[2])
        for _ in range(3):
            assert dq.pop() == elements.pop()

    def test_erase(self):
        dq = DataQueue()
        element = 1
        dq.add(element)
        dq.erase()
        assert dq.is_empty() == True
