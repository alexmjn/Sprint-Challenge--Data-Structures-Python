"""This module builds off of previously constructed DoublyLinkedList class
to implement a RingBuffer class -- essentially, where a linked list's end
points back to the beginning.
"""
from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        """Initialize the ring.

        Ring is initialized with a fixed capacity, a current value being
        accessed, and a doubly-linked list to define the element structure
        and hold the elements.
        """
        self.capacity = capacity
        self.current = None
        self.elements = DoublyLinkedList()


    def append(self, item):
        """Function to add an item to the ring structure.

        If we're under capacity, we simply add the item to the tail, then
        point back to the head for future operations. If we're above capacity,
        we set the pointer to the item itself, iteratively move to the tail --
        which is also the head -- and replace the item held there with the
        desired value to append. This can be thought of as overwriting the
        oldest value held in memory with the new item.
        """
        if len(self.elements) < self.capacity:
            self.elements.add_to_tail(item)
            self.current = self.elements.head

        else:
            self.current.value = item
            if self.current is not self.elements.tail:
                self.current = self.current.next
            else:
                self.current = self.elements.head


    def get(self):
        """Function to return all non-None values in the ring.

        We initialize an empty list, then, for every element in the ring,
        append that element if it exists (i.e. is not None).
        """
        ring_elements = []
        current_value = self.elements.head
        for _ in range(len(self.elements)):
            if current_value.value is not None:
                ring_elements.append(current_value.value)
            current_value = current_value.next

        return ring_elements
