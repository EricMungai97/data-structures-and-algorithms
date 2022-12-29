# Stacks and Queues

A stack is a data structure that consists of `Nodes`. Each Node references the next Node in the stack, but does not reference its previous.

A queue is a linear data structure that stores items in First In First Out (FIFO) manner

## Challenge

Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue with methods listed below.

## Approach & Efficiency

All Stack and Queue methods detailed below run in constant time, O(1). This is because direct references allow constant time access to the top of a stack, and to both the front and rear of a queue.

## API

Stack Methods:

* push: takes a value as an argument, creates a node with that value, adds it to the top of the stack

* pop: removes the top node from the stack and returns its value

* peek: returns the top node's value

* is_empty: returns True if stack is empty, otherwise returns False

Queue Methods:

* enqueue: takes a value as an argument, creates a node with that value, adds it to the rear of the queue

* dequeue: removes the front node from the queue and returns its value

* peek: returns the front node's value

* is_empty: returns True if queue is empty, otherwise returns False
