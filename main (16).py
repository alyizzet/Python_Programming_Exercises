class Node:
  def __init__(self, init_data):
    self.data = init_data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None    #top stores a Node
  def push(self, x):
    if x == None:
      self.top = Node(x)
    else:
      new_node = Node(x)
      new_node.next = self.top
      self.top = new_node

  def pop(self):
    if self.is_empty() == True:
      return None
    else:
      pop = self.top
      self.top = self.top.next
      pop.next = None 
      return pop.data
    #implement this: makes top point to the next of the Node pointed to by top
  def peek(self):
    if self.is_empty() == True:
      return None
    else: 
      return self.top.data
    #implement this: returns the data of the Node pointed to by top
  def is_empty(self):
    if self.top == None:
      return True
    else:
      return False 
      
    #implement this: returns True if there are no Nodes in
    #Stack, otherwise False