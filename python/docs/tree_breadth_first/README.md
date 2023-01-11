# Challenge Summary

Write a function called breadth first

* Arguments: tree

* Return: list of all values in the tree, in the order they were encountered

Traverse the input tree using a Breadth-first approach

## Whiteboard Process

![Tree_breadth_first](/python/docs/tree_breadth_first/tree_breadth_first.png)

## Approach & Efficiency

I created an empty queue and then traversed the tree through Breadth-first approach. On each pop of the traversal I appended the popped value to a list.

Big O:

Time:O(n)

Space: O(n)

## Solution

```
 tree = BinaryTree()
 tree.root = Node("apples")
 tree.root.left = Node("bananas")
 tree.root.right = Node("cucumbers")
 tree.root.right.right = Node("dates")
 breadth_first(tree)

 Output ["apples", "bananas", "cucumbers", "dates"]
```

[Link To Code](/python/code_challenges/tree_breadth_first.py)
