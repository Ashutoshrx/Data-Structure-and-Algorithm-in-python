#LINKED LIST
class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head = None

    def print(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next

list = Linkedlist()
list.head = Node(45)
second = Node(453)
third = Node(36)
list.head.next = second
second.next = third

list.print()
