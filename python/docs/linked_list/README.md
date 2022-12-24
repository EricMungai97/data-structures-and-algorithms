# Singly Linked List

A singly linked list consists of nodes, each of which contains a value and a reference to the next node in the ordered list of nodes. The linked list variable holds a reference to the head node. The tail node of the linked list holds a reference to None.

## Challenge

Challenge was to create a linked list with the below features. Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node. Create a Linked List class, include a HEAD property that instantiates an empty link list. The linked list class should contain the following methods: insert, includes, and to string. The insert method needs to apply the Arguments: value, Return: nothing, and add a new node with that value to the head of the list with an O(1) time performance. The includes method needs to apply the arguments: value, return a Boolean that indicates that value's existence in the list. The to string method needs to apply arguments: value and return a string representing all the values in the format of "{ a } -> { b } -> { c } -> None".

## Approach & Efficiency

I started by running each test in tests/data_structures/test_linked_list.py one test at a time and then write the necessary code to make the that test pass.

* insert: O(1) time, O(1) space
* includes: O(N) time, O(1) space
* __str__: O(N) time, O(N) space

## API
Description of each method  in Linked List Class:

1. str which prints a string representation of the full linked list
2. insert which adds a new node to the head of the linked list
3. includes which returns True if a given value is in the linked list and False otherwise

