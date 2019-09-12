# Creating the Node Class
class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None

# Creating the Single Linked List Class
class LinkedList:
    def __init__(self):
        self.start_node = None

    # Traversing Linked List Items
    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " ")
                n = n.ref

    # Inserting Items

    #Inserting Items at the Beginning
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node= new_node

    # Inserting Items at the End
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node;

    # Inserting Item after another Item
    def insert_after_item(self, x, data):

        n = self.start_node
        print(n.ref)
        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    # Inserting Item before another Item
    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List has no element")
            return

        if x == self.start_node.item:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            return

        n = self.start_node
        print(n.ref)
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    # Inserting Item at Specific Index
    def insert_at_index (self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
        i = 1
        n = self.start_node
        while i < index-1 and n is not None:
            n = n.ref
            i = i+1
        if n is None:
            print("Index out of bound")
        else: 
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def get_count(self):
        if self.start_node is None:
            return 0;
        n = self.start_node
        count = 0;
        while n is not None:
            count = count + 1
            n = n.ref
        return count

    def search_item(self, x):
        if self.start_node is None:
            print("List has no elements")
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                print("Item found")
                return True
            n = n.ref
        print("item not found")
        return False


# Creating a Linked List

    def make_new_list(self):
        nums = int(input("How many nodes do you want to create: "))
        if nums == 0:
            return
        for i in range(nums):
            value = int(input("Enter the value for the node:"))
            self.insert_at_end(value)

# Deletion from the Start

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        self.start_node = self.start_node.ref

# Deletion from the end

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return

        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

# Deletion by value 

    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return

        # Deleting first node 
        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return

        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref

        if n.ref is None:
            print("item not found in the list")
        else:
            n.ref = n.ref.ref

# Reversing a linked List

    def reverse_linkedlist(self):
        prev = None
        n = self.start_node
        while n is not None:
            next = n.ref
            n.ref = prev
            prev = n
            n = next
        self.start_node = prev

    def detectLoop(self): 
         s = set() 
         temp = self.start_node
         while (temp): 
          
             # If we have already has 
             # this node in hashmap it 
             # means their is a cycle 
             # (Because you we encountering 
             # the node second time). 
            if (temp in s): 
                return True
     
            # If we are seeing the node for 
            # the first time, insert it in hash 
            s.add(temp) 
     
            temp = temp.ref     
         return False

'''     
# First, create an object of the linked list class as follows:
new_linked_list = LinkedList()
new_linked_list.insert_at_end(5)
new_linked_list.insert_at_end(10)
new_linked_list.insert_at_end(15)

# let's traverse through the linked list using traverse function.
new_linked_list.traverse_list()

new_linked_list.insert_at_start(20)
new_linked_list.traverse_list()

# Let's add a new item 17 after item 10
new_linked_list.insert_after_item(10, 17)

# Let's now insert another item 25 before the item 17
new_linked_list.insert_before_item(17, 25)

# let's add an element at the third location
new_linked_list.insert_at_index(3,8)

'''
new_linked_list = LinkedList()
new_linked_list.make_new_list()
new_linked_list.insert_at_start(7)
new_linked_list.insert_before_item(7,0)
new_linked_list.insert_at_end(88) 

print("Now Traverse")
new_linked_list.traverse_list()
llist_count = new_linked_list.get_count()
print("Count = ", llist_count)

new_linked_list.start_node.ref.ref.ref.ref = new_linked_list.start_node;

check_loop = new_linked_list.detectLoop()
print("Check loop :",check_loop)
