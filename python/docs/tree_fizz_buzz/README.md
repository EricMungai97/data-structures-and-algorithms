# Challenge Summary

Write a function called fizz buzz tree

* Arguments: k-ary tree

* Return: new k-ary tree

Determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:

* If the value is divisible by 3, replace the value with “Fizz”

* If the value is divisible by 5, replace the value with “Buzz”

* If the value is divisible by 3 and 5, replace the value with “FizzBuzz”

* If the value is not divisible by 3 or 5, simply turn the number into a String.

## Whiteboard Process

![tree-fizz-buzz](/python/docs/tree_fizz_buzz/tree-fizz-buzz.png)

## Approach & Efficiency
I first created a function to get return fizz,buzz of fizzbuzz. I then cloned the kary tree. I created a queue. I then enqueue the root of our clone_tree.
I then breadth traverse the clone_tree using a while loop. On traversal of each node, I assigned that nodes value to the return of my get_fizz_buzz_val function taking in that nodes value as an argument. I then returned the clone_tree.

Big O:
 Time: O(n2) since we have to traverse the kary tree with a while loop with a nested for loop.
 Space: O(n) we are creating a new kary tree

## Solution

[Link To Code](/python/code_challenges/tree_fizz_buzz.py)
