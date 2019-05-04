#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(n) because we loop through each node in the 
        linked list to complete the method"""
        # Loop through all nodes and count one for each
        length = 0

        if self.is_empty():             # if ll is empty    O(1)
            return length               # return 0          O(1)

        node = self.head                # get the first node       O(1)
        while node is not None:         # while we can continue getting nodes from the list; from 1 to n iterations: O(1), O(n)
            length += 1                 # increment length by 1     O(1)
            node = node.next            # and get the next node     O(1)

        return length                   # after we run out of nodes return length     O(1)



    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) because we jump to the tail and
        create and wire up a new node there"""
        # Append node after tail, if it exists
        if self.tail is None:           # if there is no tail       O(1)
            self.head = Node(item)      # head points to a Node where data=item     O(1)
            self.tail = self.head       # tail points to head       O(1)
        else:                           # if there is a tail
            node = self.tail            # get the node tail points to   O(1)
            node.next = Node(item)      # point that node to a Node where data=item     O(1)
            self.tail = node.next       # tail points to that instance      O(1)

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) because we jump to the head and create
        and wire up a new node before it"""
        if self.head is None:           # if there is no head       O(1)
            self.head = Node(item)      # head points to a Node where data=item     O(1)
            self.tail = self.head       # tail points to head       O(1)
        else:                           # if there is a head
            node = self.head            # get the node the head points to       O(1)
            self.head = Node(item)      # point head to a Node where data=item      O(1)
            head = self.head            # get the node head ponts to        O(1)
            head.next = node            # point that node to the old head node      O(1)

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) if data is found in the first node.
        Worst case running time: O(n) if the data is not found at all.
        Where n is the number of items stored in the linked list."""
        node = self.head    # O(1)
        while node is not None:         # from 1 to n iterations: O(1), O(n)
            if quality(node.data):      # O(1)
                return node.data        # O(1)
            node = node.next            # O(1)
        
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) if the head node is the item
        we're looking for
        Worst case running time: O(n) if we loop all the way through the
        input and don't find the key"""
        node = self.head                                                # get node head points to       O(1)
        while node is not None:                                         # so long as node isn't None;  from 1 to n iterations: O(1), O(n)
            next_node = node.next                                       # hold the next node    O(1)
            if node.data == item:                                       # if node.data is item  O(1)

                if node == self.head and node == self.tail:             # if only one node in ll    O(1)
                    self.head = None                                    # point head to None    O(1)
                    self.tail = None                                    # point tail to None    O(1)
                    del node                                            # delete only node    O(1)
                    return                                              # return    O(1)
            
                                                                        # if first node is a match:
                self.head = node.next                                   # point head to the next node       O(1)
                del node                                                # delete that node    O(1)
                return                                                  # return    O(1)

            if next_node is not None and next_node.data == item:        # if the next node holds the item    O(1)
               
                if next_node == self.tail:                              # if the next node is the tail    O(1)
                    self.tail = node                                    # self.tail points to node    O(1)
                    node.next = None                                    # node points to None    O(1)
                    del next_node                                       # delete the next node    O(1)
                    return                                              # return    O(1)

                node.next = next_node.next                              # node points to the node that next_node pointed to    O(1)
                del next_node                                           # delete next_node    O(1)
                return                                                  # return    O(1)
            
            node = next_node                                            # moves thru ll in while    O(1)

        raise ValueError('Item not found: {}'.format(item))             # while ends, not found


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
