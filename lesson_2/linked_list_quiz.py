"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Element():
    def __init__(self, value):
        self.value = value 
        self.next = None 


class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        n = self.head
        if self.head:
            while n.next:
                n = n.next
            n.next = new_element                   
        else:
            self.head = new_element


if __name__ == "__main__":

    # Test cases
    # Set up some new elements
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    # Start setting up a LinkedList
    l1 = LinkedList(e1)
    l1.append(e2)
    l1.append(e3)

    # Test get_position
    # Should print 3
    print(l1.head.next.next.value) 


   
