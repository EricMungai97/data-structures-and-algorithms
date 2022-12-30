from data_structures.linked_list import LinkedList, Node


def zip_lists(a, b):
    # assign head node of each linked to specific variable
    current1 = a.head
    current2 = b.head

    if a.head:
        # create a new Linked list with the head being the head of our first ll
        new_ll = LinkedList(a.head)
        # set current node on 1st ll to be its 2nd node
        current1 = current1.next
        current_new = new_ll.head

    else:
        return b

    while current1 and current2:
        # set the next of our current node to be value of first node in 2nd ll
        current_new.next = Node(current2.value)
        # change current on 2nd ll to next node
        current2 = current2.next
        # set current of new ll to new node
        current_new = current_new.next

        # set the next of our current node to be value of 2nd node in 1st ll
        current_new.next = Node(current1.value)
        current1 = current1.next
        current_new = current_new.next

    while current1:
        current_new.next = Node(current1.value)
        current1 = current1.next
        current_new = current_new.next

    while current2:
        current_new.next = Node(current2.value)
        current2 = current2.next
        current_new = current_new.next

    return new_ll
