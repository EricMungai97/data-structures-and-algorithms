from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError


class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        # check to see if queue is empty!
        if self.rear:
            self.rear.next = Node(value)
            self.rear = self.rear.next
            return
        self.rear = self.front = Node(value)

    def dequeue(self):
        # consider a queue with only 1 node
        # TODO: refactor class to include a .length
        if self.front is None:
            raise InvalidOperationError
        if self.front == self.rear:
            dequeued = self.front
            self.front = self.rear = None
            return dequeued.value

        dequeued = self.front
        self.front = self.front.next
        return dequeued.value

    def peek(self):
        if self.front is None:
            raise InvalidOperationError
        else:
            return self.front.value

    def is_empty(self):
        if self.front:
            return False
        else:
            return True
