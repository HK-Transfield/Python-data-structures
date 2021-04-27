class Node:
    def __init__(self, data):
        self.data = data    # The data will be stored in the Node
        self.right = self.left = None  # A new node will have no children


class BSTInt:
    def __init__(self):
        """Constructor."""
        self.root = None

    def insert(self, val):
        """Inserts a new value into the BST.

        Args:
            val: The integer value to be inserted into the BST.
        """
        temp = Node(val)

        if self.root == None:
            self.root = temp
        else:
            curr = self.root

            while curr.data != val:
                if curr.data < val:

                    if curr.left == None:
                        curr.left = temp

                    curr = curr.left

                else:
                    if curr.right == None:
                        curr.right = temp

                    curr = curr.right
        return None

    def remove(self, val):
        """Traverses the BST and removes an interger value from the BST.

        Args:
            val: The interger value to be removed
        """
        self.remove_recur(self.root, val)
        return None

    def remove_recur(self, root, val):
        curr = root     # Start at the beginning of the BST
        parent = None   # The parent of the node that will be removed

        while curr != None and curr.key != val:
            parent = curr
            curr = curr.left if curr.key < val else curr.right

        if curr == None:
            return root

        if curr.left == None and curr.right == None:
            if curr != root:
                if parent.left == curr:
                    parent.left = None
                else:
                    parent.right = None
            else:
                root = None
        elif curr.left != None and curr.right != None:
            successor = self.minimum_key(curr.right)

            self.remove_recur(root, successor.key)

            curr.key = successor.key
        else:
            child = curr.left if curr.left != None else curr.right

            if curr != root:
                if parent.left == curr:
                    parent.left = child
                else:
                    parent.right = child
            else:
                root = child
        return None

    def minimum_key(self, curr):
        while curr.left != None:
            curr = curr.left
        return curr

    def is_empty(self):
        return self.root == None

    def find(self, val):
        curr = self.root

        while curr != None and curr.data != val:
            curr = curr.left if val < curr.left else curr.right

        return not curr == None

    def dump(self):
        self.in_order_recur(self.root)
        return None

    def in_order_recur(self, root):
        if root == None:
            return None

        self.in_order_recur(root.left)
        print(root.data)
        self.in_order_recur(root.right)

        return None
