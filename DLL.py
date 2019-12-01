class Node: 
      
   
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)
  
class DoublyLinkedList: 
    
    def __init__(self): 
        self.head = None

    def size(self):
        count = 0
        node_iterator = self.head
        while node_iterator.next is not None:
            node_iterator = node_iterator.next
            count+=1
        return count
   
    def reverse(self): 
        temp = None
        current = self.head 
          
       
        while current is not None: 
            temp = current.prev  
            current.prev = current.next
            current.next = temp 
            current = current.prev 
  
     
        if temp is not None: 
            self.head = temp.prev 
          
   
    def push(self, new_data): 
   
       
        new_node = Node(new_data) 
        if self.head is None:
            self.head = new_node
        else:
            node_iterator = self.head
            while node_iterator.next is not None:
                node_iterator = node_iterator.next
            node_iterator.next = new_node
            new_node.prev = node_iterator
  

    def pushToK(self, value , k):
        new_node = Node(value)
        node_iterator = self.head
        count = 0
        if(k > self.size() or k < 0):
             return "Нет позиции"
        if(k !=0):
            while count != k-1:
                node_iterator = node_iterator.next
                count+=1
            if(node_iterator.next is None):
                node_iterator.next = new_node
                new_node.prev = node_iterator
            else:
                new_node.next = node_iterator.next
                new_node.prev = node_iterator
                node_iterator.next = new_node
                new_node.next.prev = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    def printList(self, node):
        s = ""
        while(node is not None): 
            s += "{} ".format(str(node)) 
            node = node.next
        return s


