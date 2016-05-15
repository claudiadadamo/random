#!/usr/bin/env python2.7

import random
from data_structures import queue
"""
Silly command line thing that will randomly generate phone numbers that the
user must confirm if correct or not. This implementation uses a queue to append
a random number and basically shift the numbers over by one. For example:

    Original number:
    1234567890

    Is this your number? no
    2345678905

    etc, etc
"""

VALID_RESPONSES = ('y', 'n')
class PhoneNumber(object):

    def __init__(self):
        self.number = queue.IterableQueue()

    def generate(self):
        """
        Generate the random number. If it is the first time, generate 10 random
        integers for the starting phone number.
        """
        if self.number.size() == 0:
            for i in xrange(0, 10):
                num = random.randint(0, 9)
                self.number.enqueue(num)
        self.number.dequeue()
        rand_num = random.randint(0, 9)
        self.number.enqueue(rand_num)
        return ''.join([str(i) for i in self.number])

if __name__ == '__main__':
    base_number = PhoneNumber()

    answer = "n"
    while answer == "n":
        number = base_number.generate()
        print "is your number {}? y or n".format(number)
        answer = raw_input()

    if answer == 'y':
        print "WAHOO! "
    else:
        print "that is not a valid response. valid responses are {}".format(', '    .join((VALID_RESPONSES)))

