# Challenge Summary

Create a method called find maximum value for the Binary Tree Class.The method should take in no arguments and should return the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.

## Whiteboard Process

![tree_max](/python/docs/tree_max/tree_max.png)

## Approach & Efficiency

I called the tree my pre_order tree traversal method and assigned the list returned to a varibale called nodes. I then created a variable called max_val and assigned it the int zero. I then looped through every element in my nodes list and reassigned the max_val to the element, whenever the element was greater than max_val. I then returned the max_val once the for loop ended.

Big O:
Time: O(n) we have to traverse every node in our binary tree and worst case every element in our node list.
Space:O(n) additional space was required to store the nodes list.
## Solution

```
tree = BinaryTree()
tree.root = Node(10)
tree.root.left = Node(30)
tree.root.right = Node(-7)

tree.find_maximum_value()
# output 30
```

[Link To Code](/python/data_structures/binary_tree.py)

