# Initializing a node
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data  # assign given data to the node
        self.next = next  # Initialize the next attribute to null
        self.prev = prev  # Initialize the previous attribute to null


# Creating a double linked list class, empty linked list and no nodes in this list to point. Will add nodes by inserting new nodes.
class Double_Linked_list:
    def __init__(self):
        self.head = None


    def print_LL(self):
        if self.head is None:
            print("linked list is empty")
        temp = self.head  # start from the head of the list
        while temp is not None:
            print(temp.data, end=" ")  # print data in the current mode
            temp = temp.next  # move to the next node
        print()  # Ensure the output is followed by a new line

    def insert_at_end(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node  # if the list is empty, make a new node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data, None, temp)  # make  the new node to the next node of last node

    def delete_at_beginning(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            self.head = self.head.next

    def delete_from_end(self):
        if self.head is None:
            print("Linked List is empty")
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        # Otherwise, go to the second-last node
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def search_item(self, value):
        current = self.head
        position = 0
        while current is not None:
            if current.data == value:
                print(f"Value {value} found at position {position}")
                return
            current = current.next
            position += 1
        return f"Value {value} not found in the list"

    def insert_value(self, data_list):
        self.head = None
        for value in data_list:
            self.insert_at_end(value)

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        if self.head is None:
            print("Linkedlist is Empty")
            return
        if self.head.data == data_after:
            # Now insert data_to_insert after data_after node
            self.head.next = Node(data_to_insert, self.head.next)
            return
        temp = self.head
        while temp is not None:
            if temp.data == data_after:
                # Now insert data_to_insert after data_after node
                temp.next = Node(data_to_insert, temp.next)
                break
            temp = temp.next
        print(f"Value {data_after} not found in the list")

    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head is None:
            print("Linkedlist is empty")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next is not None:
            if temp.next.data == data:
                temp.next = temp.next.next
                break
            temp = temp.next

    def print_forward(self):
        # this method prints list in forward direction. Use node.next
        if self.head is None:
            print("Linkedlist is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def print_backward(self):
        if self.head is None:
            print("Linkedlist is empty")
            return
        last_node = self.get_last_node()
        temp = last_node
        while temp:
            print(temp.data, end=" ")
            temp = temp.prev
        print()

    def get_last_node(self):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        return temp


"""
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += itr.data + '-->'
            itr = itr.prev
        print("Link list in reverse: ", llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

 

if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()"""
