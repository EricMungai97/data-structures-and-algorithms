# Challenge Summary

Create a new class called pseudo queue.

Do not use an existing Queue.

Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below),

Methods:

* enqueue
        Arguments: value
        Inserts a value into the PseudoQueue, using a first-in, first-out approach.
* dequeue
        Arguments: none
        Extracts a value from the PseudoQueue, using a first-in, first-out approach.

Internally, utilize 2 Stack instances to create and manage the queue


## Whiteboard Process

![stack_queue_pseudo](/python/docs/stack_queue_pseudo/stack_queue_pseudo.png)

## Approach & Efficiency

I used two stacks. All items get pushed and stored on first stack when enqueing. Whenever dequeueing we move everything from the first stack to the second and then pop off. Then to keep the correct order, we pop every item in the second stack and push back to the first stack.

Big O:

* Time: O(n)

* Space: O(1)

## Solution

```

Stack1 [10]->[15]->[20]

PseudoQueue.enqueue(Stack1, 5)

 Output

 [5]->[10]->[15]->[20]

 ```

 **Dequeue**

```

 PseudoQueue.dequeue(Stack1)

Output

20
```
[Link to Code](/python/code_challenges/stack_queue_pseudo.py)
