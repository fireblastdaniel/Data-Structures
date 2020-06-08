class Node:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def __str__(self):
      string = '('
      nodeval = self.head
      while nodeval:
          string += f'{nodeval.value}, '
          nodeval = nodeval.next
      string += ')'
      return string

  def add_to_tail(self, value):
    if self.head:
      nextval = self.head
      while nextval.next:
        nextval = nextval.next
      self.tail = Node(value)
      nextval.next = self.tail
    else:
      self.head = Node(value)
      self.tail = self.head

  def remove_head(self):
    if self.head:
      headval = self.head.value
    else:
      headval = None
    if self.head == self.tail:
      self.head = None
      self.tail = None
    else:
      self.head = self.head.next
    return headval

  def remove_tail(self):
    if self.tail:
      tailval = self.tail.value
    else:
      tailval = None
    if self.head == self.tail:
      self.head = None
      self.tail = None
    else:
      nexttolastval = self.head
      while nexttolastval.next.next:
        nexttolastval = nexttolastval.next
      self.tail = nexttolastval
      self.tail.next = None
    return tailval

  def get_max(self):
    maxval = None
    testval = self.head
    while testval:
      if maxval == None or testval.value > maxval:
        maxval = testval.value
      testval = testval.next
    return maxval

  def contains(self, value):
    testval = self.head
    while testval:
      if testval.value == value:
        return True
      testval = testval.next
    return False
