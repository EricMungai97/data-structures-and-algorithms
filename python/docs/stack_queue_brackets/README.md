# Challenge Summary

Write a function called validate brackets

Arguments: string

Return: boolean representing whether or not the brackets in the string are balanced

There are 3 types of brackets:

* Round Brackets : `()`

* Square Brackets : `[]`

* Curly Brackets : `{}`

## Whiteboard Process

![stack-queue-brackets](/python/docs/stack_queue_brackets/stack_queue_brackets.png)

## Approach & Efficiency

I utilized a stack, a dictionary with opening and closing brackets as keys and open as value for opening brackets and close as value for closing brackets and a dictionary with matching pairs brakets as key and value
I looped through the string, and checked every element. If the element is an opening bracket, I add to the stack. If the element is a closing bracket, I check if the stacks is not empty and it matches whats on top of the stack. If either of those conditions are false, I return false. Otherwise I pop off the stack and move on. At the end I return whether the stack is empty.

Big O:

* Time: O(n)

* Space: O(n)

## Solution

```
multi_bracket_validation({[()]})

output #TRUE

```

[Link to code](/python/code_challenges/stack_queue_brackets.py)
