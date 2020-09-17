"""Now try implementing a BST on your own. This time you will implement 
search() and insert(). You should rewrite search() and not use your code 
from last excercise so it takes advantage of BST properties. Feel free to 
make any helper functions you feel like you need, including the print_tree
function from earlier for debugging. You can assume that two nodes with the 
same value won't be inserted into the tree. Beware of all the complications."""

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST():
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val) 

    def insert_helper(self, start, new_val):
        if new_val < start.value :
            if start.left is None:
                start.left = Node(new_val)
            else:
                self.insert_helper(start.left, new_val)
        elif new_val > start.value:
            if start.right is None:
                start.right = Node(new_val)
            else:
                self.insert_helper(start.right, new_val)
    
    def search_helper(self, start, find_val):
        if start:
            if find_val == start.value:
                return True 
            elif find_val < start.value:
                return self.search_helper(start.left, find_val)
            else:
                return self.search_helper(start.right, find_val)
        return False  

    def print_tree(self):
        print(self.preorder_print(self.root, "")[:-1])

    def preorder_print(self, start, traversal):
        if start:
            traversal += str(start.value) + "-"
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal 



if __name__ == "__main__":
    # Set up tree 
    tree = BST(4)

    # Insert elements
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(5)

    # print_tree
    tree.print_tree()

    # Check search 
    # Should be True
    print(tree.search(4))
    # Should be False
    print(tree.search(6))
    # Should be False
    print(tree.search(7))
    # Should be True
    print(tree.search(1))
    # Should be False 
    print(tree.search(10))