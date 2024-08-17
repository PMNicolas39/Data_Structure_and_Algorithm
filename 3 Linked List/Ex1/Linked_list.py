# Initializing a node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data  # assign given data to the node
        self.next = next  # Initialize the next attribute to null


# Creating a linked list class, empty linked list and no nodes in this list to point. Will add nodes by inserting new nodes.
class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        # create new node
        new_node = Node(data)
        # initialize next to head
        new_node.next = self.head
        # initialize head to node
        self.head = new_node

    def print_LL(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp = self.head  # start from the head of the list
            while temp is not None:
                print(temp.data, end=" ")  # print data in the current mode
                temp = temp.next  # move to the next node
            print()  # Ensure the output is followed by a new line

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  # if the list is empty, make a new node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node  # make  the new node to the next node of last node

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



"""if __name__ == '__main__':
  #create a new linkedlist
  llist = Linkedlist()
  #insert each letter at the beginning using the method we created
  llist.insert_at_beginning('fox')
  llist.insert_at_beginning('brown')
  llist.insert_at_beginning('quick')
  llist.insert_at_beginning('the')
  llist.insert_at_end('lazy')

  #print the list before deletion
  print("Before deletion:")
  llist.print_LL()

  #print the list after deletion
  llist.delete_at_beginning()
  llist.delete_from_end()
  print("After deletion: ")
  llist.print_LL()

  #search "quick" and "lazy" in the list
  llist.search_item("quick")
  llist.search_item("lazy")"""
