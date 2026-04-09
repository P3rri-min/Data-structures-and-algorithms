# Node class represents each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        current_position = 0
        while current_node and current_position < position - 1:
            current_node = current_node.next
            current_position += 1
        if current_node is None:
            print("position out of bounds")
            return
        new_node.next = current_node.next
        current_node.next = new_node

    def delete_by_value(self, x):
        if self.head is None:
            return
        if self.head.data == x:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.data == x:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def search(self, x):
        current_node = self.head
        index = 0
        while current_node:
            if current_node.data == x:
                return index
            current_node = current_node.next
            index += 1

        return -1
    
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


    def size(self): 
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next 
        return count
    
# TEST CASES
if __name__ == "__main__":
    linked_list = Linkedlist()

    # Test append and prepend
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    print("original linked list:", end=" ")
    linked_list.print_list()

    linked_list.prepend(0)
    print("after prepending 0:")
    linked_list.print_list()

    # Test insert at position
    linked_list = Linkedlist()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(4)
    linked_list.insert_at_position(3,2)
    print("insert 3 at position 4", end=" ")
    linked_list.print_list()

    # Test delete
    linked_list = Linkedlist()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.delete_by_value(3)
    print("after deleting 3: ", end="  ")
    linked_list.print_list()

    # Test search
    linked_list = Linkedlist()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    result = linked_list.search(3)
    print("index of 3:", result, end=" ")
    linked_list.print_list()


    # Test display
    linked_list = Linkedlist()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    print("display list:", end=" ")
    linked_list.print_list()

    # Test size
    linked_list = Linkedlist()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    print("size of linked list:", linked_list.size(), end="  ")
    linked_list.print_list()

    # Test empty check
    linked_list = Linkedlist()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    if linked_list.is_empty():
        print("The linked list is empty.")
    else:
        print("The linked list is not empty.")







    








