"""Your goal is to create your own binary tree. You'll need to implement two methods
: search(), which searches for the presence of a node in the tree and print_tree(),
which prints out the values of tree nodes in a pre-order traversal.
You should attempt to use the helper methods provided to create
 recursive solutions to these functions. """

class Node():
     def __init__(self, value):
         self.value = value
         self.left = None
         self.right = None

class BinaryTree():
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value is in the tree, return False otherwise."""
        boolean = self.preorder_search(self.root, find_val)
        return boolean

    def print_tree(self):
        """Print out all tree nodes as they are visited in a pre-order traversal."""
        traversal = ""
        traversal = self.preorder_print(self.root, traversal)
        return "-".join(traversal)

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a recursive search solution."""
        if start.value == find_val:
            return True 
        if start.left:
            pre_boolean = self.preorder_search(start.left, find_val)
            if pre_boolean:
                return pre_boolean
        if start.right:
            pre_boolean = self.preorder_search(start.right, find_val)
            if pre_boolean:
                return pre_boolean
        return False

    def preorder_print(self, start, traversal):
        """Use this to create a recursive print solution."""
        traversal = traversal + str(start.value) 
        if start.left:
            traversal = self.preorder_print(start.left, traversal)
        if start.right:
            traversal = self.preorder_print(start.right, traversal)
        return traversal

if __name__ == "__main__":
    # Set up tree
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)  

    # Test search 
    # Should be True
    print(tree.search(4))
    # Should be False
    print(tree.search(6))

    # Test print_tree
    # Should be 1-2-4-5-3
    print(tree.print_tree())

    # Set up 2nd tree
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7) 

    # Test search 
    # Should be True
    print(tree.search(4))
    # Should be True
    print(tree.search(6))

    # Test print_tree
    # Should be 1-2-4-5-3-6-7
    print(tree.print_tree())