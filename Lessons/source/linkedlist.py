#!python

class BinaryNode(object):

    def __init__(self, data):

        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList(object):

    def __init__(self, iterable=None):

        self.head = None
        self.tail = None
        self.size = 0

        if iterable != None:
            for item in iterable:
                self.append(item)

    def items(self):
        """Return a list of all items in this linked list."""
        item_list = []
        curr = self.head

        while curr != None:
            item_list.append(curr.data)
            curr = curr.next
        return item_list

    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        if self.head == None:
            return True
        return False

    def length(self):
        """Return the length of this linked list by traversing its nodes."""
        return self.size

    def get_at_index(self, index):
        """Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size."""

        if index < 0 or index > self.size:
            raise ValueError("index out of range: {}".format(index))

        curr_node = self.head
        while curr_node != None:
            if index == 0:
                return curr_node.data
            curr_node.prev = curr_node
            curr_node = curr_node.next
            index -= 1


    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size."""
        if index < 0 or index > self.size:
            raise ValueError("index out of range: {}".format(index))

        if index == self.size:
            self.append(item)
            return
        if index == 0:
            self.prepend(item)
            return

        new_node = BinaryNode(item)
        curr_node = self.head

        while curr_node != None and index > 1:

            curr_node.prev = curr_node
            curr_node = curr_node.next
            index -= 1

        new_node.next = curr_node.next
        curr_node.next = new_node
        self.size += 1

    def append(self, item):
        """Insert the given item at the tail of this linked list."""
        new_node = BinaryNode(item)
        if self.head == None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list."""

        new_node = BinaryNode(item)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality."""

        if self.is_empty():
            return

        curr_node = self.head
        while curr_node != None:
            if quality(curr_node.data):
                return curr_node.data
            curr_node.prev = curr_node
            curr_node = curr_node.next
        return None

    def replace(self, old_item, new_item):
        """Replace the given old_item in this linked list with given new_item
        using the same node, or raise ValueError if old_item is not found."""

        curr_node = self.head
        while curr_node != None:
            if curr_node.data == old_item:
                curr_node.data = new_item
                return
            curr_node.prev = curr_node
            curr_node = curr_node.next

        raise ValueError("old_item not found")

    def reverse(self):
        """Reverse all the items in our linked list"""

        if self.is_empty():
            raise ValueError("Empty doubly linked list: {}".format(self))

        

    def delete(self):
        """Delete the given item from this linked list, or raise ValueError."""

        pass

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes
        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list of all items in this linked list.
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes.
        Best and worst case space complexity: O(l) - l is length of list
        """
        # Create an empty list of results
        result = []  # Constant time to create a new list
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Always n iterations because no early exit
            # Append this node's data to the results list
            result.append(node.data)  # Constant time to append to a list
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # Now result contains the data from all nodes
        return result  # Constant time to return a list

    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Best and worst case runtime: O(1) - constant time to return property
        """
        # # Node counter initialized to zero
        # node_count = 0
        # # Start at the head node
        # node = self.head
        # # Loop until the node is None, which is one node too far past the tail
        # while node is not None:
        #     # Count one for this node
        #     node_count += 1
        #     # Skip to the next node
        #     node = node.next
        # # Now node_count contains the number of nodes
        # return node_count
        return self.size

    def get_at_index(self, index):
        """Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case runtime: O(1) - when index is the first one in the list
        Worst case runtime: O(n) - When index is near/at the end of the list
        """
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # TODO: Find the node at the given index and return its data

        result = ''

        # index becomes your counter
        # iterate through linked list, with counter decrement with each iteration
        # once counter becomes 0 or out of range, check if we have some data
        # if we find the data, we return that, otherwise return nil

        node = self.head
        while index > 0 and node is not None:
            node = node.next
            index -= 1
        result = node.data
        return result

    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case runtime: O(1) - If index is close to/at front of the linked list
        Worst case runtime: O(n) - Traverse through most of/entire linked list to get to index
        """
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # TODO: Find the node before the given index and insert item after it

        if index == self.size:   # if no items in linked list
            self.append(item)                       # append [O(1)]
        elif index == 0:         # if items exist, and we want to add item to front
            self.prepend(item)                      # add item to front [O(1)]
        else:
            new_node = Node(item)                   # create new node with the new item [O(1)]
            node = self.head                        # start at front of list [O(1)]
            while index > 1 and node is not None:   # traverse through list [0(l) - l being length of list]
                node = node.next                    # go to next node [O(1)]
                index -= 1                          # keep track of where we are [O(1)]
            new_node.next = node.next               # set pointer of new node so chain isn't broken thru insert [O(1)]
            node.next = new_node                    # insert our new node [O(1)]
            self.size += 1                          # update list length [O(1)]

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Best and worst case runtime: O(1) - just add item to end of the list, no traversal
        """
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign head to new node
            self.head = new_node
        else:
            # Otherwise insert new node after tail
            self.tail.next = new_node
        # Update tail to new node regardless
        self.tail = new_node
        self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Best and worst case runtime: O(1) - just add item to front of the list, no traversal
        """
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign tail to new node
            self.tail = new_node
        else:
            # Otherwise insert new node before head
            new_node.next = self.head
        # Update head to new node regardless
        self.head = new_node
        self.size += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Up to n iterations if we don't exit early
            # Check if this node's data satisfies the given quality function
            if quality(node.data):  # Constant time to call quality function
                # We found data satisfying the quality function, so exit early
                return node.data  # Constant time to return data
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # We never found data satisfying quality, but have to return something
        return None  # Constant time to return None

    def reverse(self):
        """Reverse all the items in our linked list"""

        if self.head == None or self.head.next == None:
            print("Can't reverse, one or no nodes in list")
            return self.head

        print("original list: {}".format(self))

        self.tail = self.head           # track end of reversed list
        curr_node = self.head           # set starting point
        prev_node = None

        while curr_node != None:
            next_node = curr_node.next  # track next node in list
            curr_node.next = prev_node  # doing the reversing on the pointers
            prev_node = curr_node       # move up one node for prev
            curr_node = next_node       # move up one node for curr
        self.head = prev_node           # reset where the head is in list

        print("reversed list: {}".format(self))
        print("head: {}".format(self.head))
        print("tail: {}".format(self.tail))

    def replace(self, old_item, new_item):
        """Replace the given old_item in this linked list with given new_item
        using the same node, or raise ValueError if old_item is not found.
        Best case runtime: O(1) - item is close to/at front of the list
        Worst case runtime: O(n) - item is close to/at end of the list, traverse
        linked list to get to item
        """
        # TODO: Find the node containing the given old_item and replace its
        # data with new_item, without creating a new node object

        node = self.head                # start at front of list [O(1)]
        while node != None:             # traverse thru list [O(l) - l is length of list]
            if node.data == old_item:   # did we find item we wanna replace? [O(1)]
                node.data = new_item    # if we did, replace it [O(1)]
                return
            else:
                node = node.next        # move on to next node [O(1)]
        raise ValueError('Item not found: {}'.format(old_item))

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case runtime: O(1) - item to delete is close to/at front of list
        Worst case runtime: O(n) - item to delete is close to/at end of list,
        need to traverse list to get to item
        """
        # Start at the head node
        node = self.head
        # Keep track of the node before the one containing the given item
        previous = None
        # Create a flag to track if we have found the given item
        found = False
        # Loop until we have found the given item or the node is None
        while not found and node is not None:
            # Check if the node's data matches the given item
            if node.data == item:
                # We found data matching the given item, so update found flag
                found = True
            else:
                # Skip to the next node
                previous = node
                node = node.next
        self.size -= 1
        # Check if we found the given item or we never did and reached the tail
        if found:
            # Check if we found a node in the middle of this linked list
            if node is not self.head and node is not self.tail:
                # Update the previous node to skip around the found node
                previous.next = node.next
                # Unlink the found node from its next node
                node.next = None
            # Check if we found a node at the head
            if node is self.head:
                # Update head to the next node
                self.head = node.next
                # Unlink the found node from the next node
                node.next = None
            # Check if we found a node at the tail
            if node is self.tail:
                # Check if there is a node before the found node
                if previous is not None:
                    # Unlink the previous node from the found node
                    previous.next = None
                # Update tail to the previous node regardless
                self.tail = previous
        else:
            # Otherwise raise an error to tell the user that delete has failed
            raise ValueError('Item not found: {}'.format(item))

def test_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    print('Getting items by index:')
    for index in range(ll.size):
        item = ll.get_at_index(index)
        print('get_at_index({}): {!r}'.format(index, item))

    print('Deleting items:')
    ll.delete('B')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('A')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    ll.insert_at_index(0, 'A')
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    ll.insert_at_index(1, 'B')
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))
    print(ll)

    ll.replace('A', 'D')
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))
    print(ll)

    ll.insert_at_index(2, 'C')
    ll.insert_at_index(3, 'F')
    ll.reverse()

def test_doubly_linked_list():
    dll = DoublyLinkedList()

if __name__ == '__main__':
    test_linked_list()
    # test_doubly_linked_list()
