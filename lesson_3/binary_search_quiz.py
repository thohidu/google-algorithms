"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    n = len(input_array)
    start_idx = 0
    end_idx = n - 1 
    while start_idx <= end_idx:
        mid_dist = (end_idx - start_idx + 1)//2
        mid_idx = start_idx + mid_dist  # for even, right end value
        if value == input_array[mid_idx]:
            return mid_idx     
        elif value > input_array[mid_idx]:
            start_idx = mid_idx + 1
        elif value < input_array[mid_idx]:
            end_idx = mid_idx - 1    
    return -1

if __name__ == "__main__":

    # list with elements in increasing order
    test_list = [1,3,9,11,15,19,29]
    test_val1 = 25
    test_val2 = 15
    print(binary_search(test_list, test_val1))
    print(binary_search(test_list, test_val2))
    print(binary_search(test_list, 29))
    print(binary_search(test_list, 9))
    print(binary_search(test_list, 1))
    print(binary_search(test_list, 100))
    print(binary_search(test_list, -1))

