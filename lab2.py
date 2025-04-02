"index_number: 1825622"
"Name: Nyarko Prince Edwin"

class Node:
    def __init__(self, data_n):
        self.data = data_n
        self.next = None
        self.prev = None

class singly_linkedList:
    def __init__(self):
        self.head = None

    def append(self, data_n):
        new_node = Node(data_n)
        # for empty list
        if not self.head:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete(self, data_n):
        current = self.head
        prev = None

        # deleting node at the head
        if current and current.data == data_n:
            self.head = current.next
            current = None
            return

        while current and current.data != data_n:
            prev = current
            current = current.next

        # when the input or data is not found
        if not current:
            return

        prev.next = current.next
        current = None

    def search(self, data_n):
        current = self.head
        index = 0

        while current:
            if current.data == data_n:
                return index
            current = current.next
            index += 1

        return None

class doubly_linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data_n):
        new_node = Node(data_n)

        # empty list
        if not self.head:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def delete(self, data_n):
        current = self.head

        while current and current.data != data_n:
            current = current.next

        if not current:
            return

        if current == self.head:
            self.head = current.next
            if self.head:
                self.head.prev = None
            return

        if current.next:
            current.next.prev = current.prev

        if current.prev:
            current.prev.next = current.next

        current = None

    def search(self, data_n):
        if not self.head:
            return None

        current = self.head
        index = 0

        while True:
            if current.data == data_n:
                return index
            current = current.next
            index += 1
            if current == self.head:
                break
        return None

class circle_linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data_n):
        new_node = Node(data_n)

        if not self.head:
            self.head = new_node
            self.head.next = self.head
            return
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next
        last_node.next = new_node
        new_node.next = self.head

    def delete(self, data_n):
        if not self.head:
            return

        current = self.head
        prev = None

        if current.data == data_n and current.next == self.head:
            self.head = None
            return

        if current.data == data_n:
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return

        temp = self.head
        while temp.next != self.head:
            if temp.next.data == data_n:
                temp.next = temp.next.next
                return
            temp = temp.next

    def search(self, data_n):
        if not self.head:
            return None

        current = self.head
        index = 0

        while True:
            if current.data == data_n:
                return index
            current = current.next
            index += 1
            if current == self.head:
                break

        return None

class ReverseLinkedList:
    def reverse_singly(self, linked_list):
        # Reversing a singly linked list
        prev = None
        current = linked_list.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        linked_list.head = prev

    def reverse_doubly(self, linked_list):
        # Reversing a doubly linked list
        current = linked_list.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev  # Moves to the next node (which was previously the previous)
        if linked_list.head:
            linked_list.head = linked_list.head.prev  # Update head to the new first node

    def reverse_circular(self, linked_list):
        # Reversing a circular linked list
        if not linked_list.head or linked_list.head.next == linked_list.head:
            return  # No need to reverse if list is empty or has only one element
        prev = None
        current = linked_list.head
        start = linked_list.head
        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            if current == start:
                break
        linked_list.head.next = prev
        linked_list.head = prev  # Update head to the new first node

class MiddleLinkedList:
    def find_middle_singly(self, linked_list):
        # Finding middle of a singly linked list using one traversal
        slow = linked_list.head
        fast = linked_list.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    def find_middle_doubly(self, linked_list):
        # Finding middle of a doubly linked list using one traversal
        slow = linked_list.head
        fast = linked_list.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    def find_middle_circular(self, linked_list):
        # Finding middle of a circular linked list using one traversal
        slow = linked_list.head
        fast = linked_list.head
        if not slow:
            return None
        while fast != slow and fast and fast.next != slow:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None


# Create linked lists
singly_linked_list = singly_linkedList()
doubly_linked_list = doubly_linkedlist()
circular_linked_list = circle_linkedlist()

# Append data
singly_linked_list.append(1)
singly_linked_list.append(2)
singly_linked_list.append(3)

doubly_linked_list.append(1)
doubly_linked_list.append(2)
doubly_linked_list.append(3)

circular_linked_list.append(1)
circular_linked_list.append(2)
circular_linked_list.append(3)

# Reverse and find middle of linked lists
reverse_obj = ReverseLinkedList()
middle_obj = MiddleLinkedList()

# Reverse the singly linked list
reverse_obj.reverse_singly(singly_linked_list)

# Find middle of the doubly linked list
middle_data = middle_obj.find_middle_doubly(doubly_linked_list)

# Reverse the circular linked list
reverse_obj.reverse_circular(circular_linked_list)

# Output middle data
print("Middle of doubly linked list:", middle_data)

# Print the reversed singly linked list
current_node = singly_linked_list.head
reversed_list = []
while current_node:
    reversed_list.append(current_node.data)
    current_node = current_node.next
print("Reversed singly linked list:", reversed_list)
