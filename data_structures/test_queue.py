import nose
import mock

import queue

class TestIterableQueue():

    def test_init(self):
        q = queue.IterableQueue()
        nose.tools.assert_equal(q.queue, [])
        nose.tools.assert_equal(q.pointer, 0)

    def test_enqueue_one_item(self):
        q = queue.IterableQueue()
        q.enqueue(1)
        nose.tools.assert_equal(q.queue, [1])

    def test_enqueue_multiple_items(self):
        q = queue.IterableQueue()
        q.enqueue(1)
        q.enqueue(5)
        q.enqueue('hi')
        nose.tools.assert_equal(q.queue, [1, 5, 'hi'])

    def test_dequeue_one_item_in_queue(self):
        q = queue.IterableQueue()
        q.enqueue(1)
        val = q.dequeue()
        nose.tools.assert_equal(val, 1)

    def test_dequeue_multiple_in_queue(self):
        q = queue.IterableQueue()
        q.enqueue(1)
        q.enqueue('hi')

        val = q.dequeue()
        nose.tools.assert_equal(val, 1)
        nose.tools.assert_equal(q.queue, ['hi'])
    
    def test_is_empty(self):
        q = queue.IterableQueue()
        empty = q.is_empty()
        nose.tools.assert_equal(empty, True)

    def test_is_empty_not(self):
        q = queue.IterableQueue()
        q.enqueue(1)
        empty = q.is_empty()
        nose.tools.assert_equal(empty, False)

    def test_repr(self):
        q = queue.IterableQueue()
        output = q.__repr__()
        nose.tools.assert_equal(type(output), str)

    def test_iter(self):
        q = queue.IterableQueue()
        obj = q.__iter__()
        nose.tools.assert_equal(obj, q)

    def test_next_end_of_queue(self):
        q = queue.IterableQueue()
        q.pointer = 2
        q.queue = [1, 3]

        with nose.tools.assert_raises(StopIteration):
            q.next()
        nose.tools.assert_equal(q.pointer, 0)

    def test_next(self):
        q = queue.IterableQueue()
        q.enqueue(1)
        q.enqueue(7)

        val = q.next()
        nose.tools.assert_equal(val, 1)

        val = q.next()
        nose.tools.assert_equal(val, 7)

        with nose.tools.assert_raises(StopIteration):
            q.next()

    def test_size_empty(self):
        q = queue.IterableQueue()

        nose.tools.assert_equal(q.size(), 0)

    def test_size_nonempty(self):
        q = queue.IterableQueue()
        q.enqueue(1)
        nose.tools.assert_equal(q.size(), 1)
