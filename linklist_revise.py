#circular doubly linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
node1 = Node(2)
node2 = Node(10)
node3 = Node(15)
node4 = Node(20)

node1.next = node2
node1.prev = node4

node2.next = node3
node2.prev = node1

node3.next = node4
node3.prev = node2

node4.next = node1
node4.prev = node3

print("Forward Traversal")

currentnode = node1
startnode = node1
print(currentnode.data, end=' -> ')

currentnode = currentnode.next

while currentnode != startnode:
    print(currentnode.data, end=' -> ')
    currentnode = currentnode.next
print('.....')

print("Reverse Traversal")

currentnode = node4
startnode = node4
print(currentnode.data, end=' -> ')

currentnode = currentnode.prev


while currentnode != startnode:
    print(currentnode.data, end=' -> ')
    currentnode = currentnode.prev
    
print('........')