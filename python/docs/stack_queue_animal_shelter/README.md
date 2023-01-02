# Challenge Summary

Create a class called AnimalShelter which holds only dogs and cats.

The shelter operates using a first-in, first-out approach.

Implement the following methods:

* enqueue

Arguments: animal

animal can be either a dog or a cat object.

* dequeue

Arguments: pref

pref can be either "dog" or "cat"

Return: either a dog or a cat, based on preference

If pref is not "dog" or "cat" then return null

## Whiteboard Process

![stack_queue_animal_shelter](/python/docs/stack_queue_animal_shelter/stack_queue_animal_shelter.png)

## Approach & Efficiency

The approach taken was to create two queues in our animal shelter initializer,one for cats the other for dogs. I also created a dog object constructor and cat constructor each with name and type property. The animal class has an enqueue method that takes either a cat or a dog and adds it to the shelter. It also has a dequeue that takes in a preference(cat/dog) and returns the animal that satisfies the preference

Big O:

  Time: O(1)

  Space: O(n)

## Solution

[Link to code](/python/code_challenges/stack_queue_animal_shelter.py)
