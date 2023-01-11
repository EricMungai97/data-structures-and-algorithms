from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):
    queue = Queue()
    values = []

    if tree.root:
        queue.enqueue(tree.root)
    else:
        return values

    while queue.front:
        current = queue.dequeue()

        values.append(current.value)

        if current.left:
            queue.enqueue(current.left)

        if current.right:
            queue.enqueue(current.right)

    return values
