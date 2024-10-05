#Python Program to implement linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self,data) :
        self.newnode=Node(data)
        self.head=self.newnode
    def AddatEnd(self,data):
          newnode=Node(data)
          currentnode=self.head
          while(currentnode.next is not None):
              currentnode=currentnode.next
          currentnode.next=newnode      
    def printLL(self):
            temp=self.head
            while(temp is not None):
                 print(temp.data,end=' ')
                 temp=temp.next        
LL=LinkedList(36)
LL.AddatEnd('a')
LL.AddatEnd(78)
LL.printLL()                 