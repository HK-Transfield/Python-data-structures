class INode:
    def __init__(self, key):
        self.key = key
        self.next = None


class IList:
    def __init__(self):
        """Initialize a new instance of
        the List"""
        self.head_node = None

    # Adds a new INode to the list unordered
    def add(self, val):
        temp = INode(val)

        # There is no head in this list
        if self.head_node == None:
            self.head_node = temp

        else:
            temp.next = self.head_node
            self.head_node = temp
        return None

    def has_val(self, val):
        """Return a boolean

        Finds an int value within the list
        """
        curr_node = self.head_node

        # loop through the list
        # until we find match

        while curr_node != None and curr_node.key != val:
            curr_node = curr_node.next

        return not curr_node == None

    def remove(self, val):
        """
        Removes a node in the list that contains a
        value.

        val: The value to be removed from the list 
        """
        curr_node = self.head_node  # start at the head of the list

        if curr_node == None:
            print('ERROR: cannot remove')
            return None
        else:
            if curr_node.key == val:
                self.head_node = self.head_node.next
            else:
                prev_node = curr_node
                curr_node = curr_node.next

                # While we haven't reach the end of the list
                # or found the INode with the matching value
                while curr_node != None and curr_node.key != val:
                    prev_node = curr_node
                    curr_node = curr_node.next

                if curr_node == None:
                    print('ERROR: could not remove ', val)
                    return None

                prev_node.next = curr_node.next

        return None

    def length(self):
        """Returns an int

        Counts the number of nodes in the list.
        """
        curr_node = self.head_node
        count = 0

        # loop through the list until we reach the end
        while curr_node != None:
            count += 1

            curr_node = curr_node.next

        return count

    def is_empty(self):
        """Returns a boolean

        Indicates if the list is empty
        """
        # call the length function
        if self.length() == 0:
            return True
        else:
            return False

    #  Dumps all the values in the list
    def dump_vals(self):
        curr_node = self.head_node

        if self.is_empty():
            # Check that the list isn't empty
            print("List is empty")
            return
        else:
            # loop through until it reaches the end of the list
            while curr_node != None:
                print(curr_node.key)
                curr_node = curr_node.next
        return None

    def insert(self, val):
        """
        This will insert a new node into the linked list. Unlike add,
        using this method will create an ordered linked list.

        val: the value to be inserted into the linked list
        """
        new_node = INode(val)
        curr_node = self.head_node
        prev_node = None

        # While we haven't reach the end of the list
        # or found the INode with the matching value
        while curr_node != None and curr_node.key < val:
            prev_node = curr_node
            curr_node = curr_node.next

        if prev_node == None:
            # insert new node at the head of the list
            self.head_node = new_node
        else:
            # insert new node inbetween prev and curr
            prev_node.next = new_node

        new_node.next = curr_node

        return None
