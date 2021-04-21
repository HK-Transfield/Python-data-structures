class INode:
    def __init__(self, key):
        self.key = key
        self.next = None


class IList:

    # Initialize an IList
    # object instance
    def __init__(self):
        self.head = None

    # Adds a new INode to the list unordered
    def add(self, val):
        temp = INode(val)

        if self.head == None:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp

    # hi
    def has_val(self, val):
        curr_node = self.head
        has_val = False

        while curr_node != None:
            if curr_node.key == val:
                has_val = True
                break
            else:
                curr_node = curr_node.next

        return has_val

    def remove(self, val):
        curr_node = self.head

        if curr_node == None:
            print('ERROR: cannot remove')
            return
        else:
            if curr_node.key == val:
                self.head = self.head.next
            else:
                prev_node = curr_node
                curr_node = curr_node.next

                while curr_node != None and curr_node.key != val:
                    prev_node = curr_node
                    curr_node = curr_node.next

                if curr_node == None:
                    print('ERROR: could not remove ', val)
                    return

                prev_node.next = curr_node.next

        return None

    def length(self):
        curr_node = self.head
        count = 0

        while curr_node != None:
            count += 1

            curr_node = curr_node.next

        return count

    #
    def is_empty(self):
        if self.length() == 0:
            return True
        else:
            return False

    #  Dumps all the values in the list
    def dump_vals(self):
        curr_node = self.head

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
        new_node = INode(val)
        curr_node = self.head
        prev_node = None

        while curr_node != None and curr_node.key < val:
            prev_node = curr_node
            curr_node = curr_node.next

        if prev_node == None:
            self.head = new_node
        else:
            prev_node.next = new_node

        new_node.next = curr_node
        return None
