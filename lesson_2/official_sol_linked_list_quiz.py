"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


# Single unit in a linked list
class Element():
    def __init__(self, value):
        self.value = value
        self.next = None 

# Defining the linked list with the first element, defaults to None 
class LinkedList():
    def __init__(self, head=None):
        self.head = head
    
    # This method will add a new element to the end of our LinkedList
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element        
        else:
            self.head = new_element 

    # This method returns the element at a certain position 
    def get_position(self, position):  
        current = self.head
        counter = 1
        if position < 1:
            return None             
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    # This method will insert an element to a particular spot in the list 
    def insert(self, new_element, position):
        current = self.head 
        counter = 1
        if position > 1:            
            while current and counter <= position -1 :
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head 
            self.head = new_element

    # This method will delete the first element with that particular value
    def delete(self, value):
        current = self.head
        previous = None 
        # Locate the current and the previous element
        while current.next and current.value != value: 
            previous = current
            current = current.next 
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next


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
    # Should also print 3
    print(l1.get_position(3).value)

    # Test insert
    l1.insert(e4, 3)
    # Should print 4 now
    print(l1.get_position(3).value)

    # Test delete
    l1.delete(1)
    # Should print 2 now
    print(l1.get_position(1).value)
    # Should print 4 now
    print(l1.get_position(2).value)
    # Should print 3 now
    print(l1.get_position(3).value)




