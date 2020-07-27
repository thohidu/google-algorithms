"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""


class Element():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_element            
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList" 
        new_element.next = self.head 
        self.head = new_element

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        current = self.head 
        self.head = self.head.next # test this assignment
        return current 


class Stack():
    def __init__(self, top=None):
        self.l1 = LinkedList(top) 

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.l1.append(new_element) # li error

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        current = self.l1.head 
        if current:
            previous = None 
            while current.next:
                previous = current
                current = current.next
            if previous:
                previous.next = current.next
            else:
                self.l1.head = None
            return current 
            
        else:
            None


if __name__ == "__main__":
    # Test cases 
    # Set up some new Elements
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    # Start setting up a Stack
    stack = Stack(e1)

    # Test stack functionality
    stack.push(e2)
    stack.push(e3)
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.pop())
    stack.push(e4)
    print(stack.pop().value)

