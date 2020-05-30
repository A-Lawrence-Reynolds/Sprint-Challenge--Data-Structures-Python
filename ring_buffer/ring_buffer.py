from doubly_linked_list import DoublyLinkedList
 

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None 
        self.storage = DoublyLinkedList()
    # using current to go over the oldest item and replace it when true 

    def append(self, item):
        if not self.current:
            # Assign current value as the head, even if it's NONE
            self.current = self.storage.head
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)

        else:
            if self.current == self.storage.head:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.current.next
            elif self.current == self.storage.tail:
                self.storage.remove_from_tail()
                self.storage.add_to_tail(item)
                self.current = self.storage.head
            else:
                self.current.insert_before(item)
                next_node = self.current.next
                self.storage.delete(self.current)
                self.current = next_node
                self.storage.length += 1
    def get(self):
        list_buffer_contents = []

        node = self.storage.head

        while node:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents