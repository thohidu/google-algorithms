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
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        return self.preorder_print(self.root, "")[:-1]
    
    def preorder_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False 
    
    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
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

