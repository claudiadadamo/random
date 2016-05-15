"""
Iterable queue class. Like a usual queue, can enqueue and dequeue, as well as
check size. This oen specifically allows for iteration over elements
currently stored in the queue.
"""

class IterableQueue(object):

    def __init__(self):
        self.queue = []
        self.pointer = 0

    def enqueue(self, item):
        """
        Add item to end of the queue.
        :param item: item to add to the queue.
        """
        self.queue.append(item)

    def dequeue(self):
        """
        Pop off the first item in the queue and return.
        """
        return self.queue.pop(0)

    def is_empty(self):
        """
        Return if the queue is empty.
        """
        return self.queue == []

    def __repr__(self):
        return str(self.queue)

    def __iter__(self):
        return self

    def next(self):
        """
        Keep track of the index of the next item in the queue that needs to be
        accessed is. Allows for multiple loops over queue so that data can be
        accessed again.
        """
        if self.pointer > len(self.queue) - 1:
            self.pointer = 0
            raise StopIteration
        val = self.queue[self.pointer]
        self.pointer += 1
        return val

    def size(self):
        """
        Return the size (length) of the queue.
        """
        return len(self.queue)
