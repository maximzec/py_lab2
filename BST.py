from itertools import *
class Node:

      def __init__(self,info): 

          self.info = info  
          self.left = None  
          self.right = None 
          self.level = None 

      def __str__(self):

          return str(self.info) 


class searchTree:

      def __init__(self): 

          self.root = None


      def create(self,val): 

          if self.root == None:

             self.root = Node(val)

          else:

             current = self.root

             while 1:

                 if val < current.info:

                   if current.left:
                      current = current.left
                   else:
                      current.left = Node(val)
                      break;      

                 elif val > current.info:
                 
                    if current.right:
                       current = current.right
                    else:
                       current.right = Node(val)
                       break;      

                 else:
                    break 

      def bft(self): 

          self.root.level = 0 
          queue = [self.root]
          out = []
          current_level = self.root.level

          while len(queue) > 0:
                 
             current_node = queue.pop(0)
 
             if current_node.level > current_level:
                current_level += 1
                out.append("\n")

             out.append(str(current_node.info) + " ")

             if current_node.left:

                current_node.left.level = current_level + 1
                queue.append(current_node.left)
                  

             if current_node.right:

                current_node.right.level = current_level + 1
                queue.append(current_node.right)
                      
                 
          print ("".join(out))   


      def inorder(self,node):
            
           if node is not None:
              
              self.inorder(node.left)
              print (node.info)
              self.inorder(node.right)


      def preorder(self,node):
           if node is None:
               return ""
           if node is not None:
              
              return str(node.info) +"( "+ str(self.preorder(node.left)) +" , "+str(self.preorder(node.right)) + " )"


      def postorder(self,node):
            
           if node is not None:
              
              self.postorder(node.left)
              self.postorder(node.right)
              print (node.info)
              
      def searchAtLevel(self , node  , level):
           s = ""
           if node is None :
              return
           elif level == 1:
               return node.info
           elif level > 1 :
               return [self.searchAtLevel(node.left , level - 1)  , self.searchAtLevel(node.right , level - 1)]
        

        
            
        
