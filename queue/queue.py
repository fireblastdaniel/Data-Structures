"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

from singly_linked_list import LinkedList
from stack import Stack

# #Array implementation
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.size += 1
#         self.storage.append(value)

#     def dequeue(self):
#         if self.storage:
#             self.size -= 1
#             removeval = self.storage[0]
#             self.storage = self.storage[1:]
#             return removeval
#         else:
#             return None

# #LinkedList implementation
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.size += 1
#         self.storage.add_to_tail(value)

#     def dequeue(self):
#         if self.size:
#             self.size -= 1
#             return self.storage.remove_head() 

#Double stack implementation
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = Stack()
        self.remove_stack = Stack()

    def __str__(self):
        return str(self.storage.storage)
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.push(value)

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            while self.storage.size > 1:
                self.remove_stack.push(self.storage.pop())
            headval = self.storage.pop()
            while self.remove_stack.size > 0:
                self.storage.push(self.remove_stack.pop())
            return headval
            