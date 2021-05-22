class Node:
  #create node
  def __inti__(self,item):
    self.item = item
    self.next = None

class LinkedList:
  def __init__(self)
    self.head = None

if __name__ == '__main__':
  
  linkedlist = LinkedList()
  
 #assign item values
  linkedlist.head() = Node(1)
  second = Node(2)
  third = Node(3)
  
 # connect nodes
  linkedlist.head.next() = second
  second.next  = third
  
  while linked_list.head != None:
        print(linked_list.head.item, end=" ")
        linked_list.head = linked_list.head.next
