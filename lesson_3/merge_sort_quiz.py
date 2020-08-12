"""merge sort algorithm"""

def merge_sort(input_array):
    n = len(input_array)
    if n > 1:
        m = n//2
        left = input_array[:m]
        right = input_array[m:]
        left = merge_sort(left)
        right = merge_sort(right)
        input_array = []
        while len(left) and len(right):
            if left[0] > right[0]:
                input_array.append(right[0])
                right.pop(0)
            else:
                input_array.append(left[0])
                left.pop(0)
        for el in left:
            input_array.append(el)
        for el in right:
            input_array.append(el)
    return input_array
     

if __name__ == "__main__":
    # Test cases 
    test_list = [12, 90, 2,1,1,100,99]         # odd 
    test_list2 = [200, -2, -2, 0, 3, 10, 8]    # even

    print(f'test_list with odd elements: {test_list}')
    print(f'Results from merge_sort func: {merge_sort(test_list)}')
    print(f"test_list2 with even elements: {test_list2}")
    print(f'Results from merge_sort func: {merge_sort(test_list2)}')

    # Comparing with built-in sort method in list data structure
    print()
    print('Comparing with built-in sort method in list data structure: ')
    test_list.sort()
    print(f"test_list: {test_list}")
    test_list2.sort()
    print(f"test_list2: {test_list2}")

    # Test new way to print list with *
    print()
    print("Test printing list with * ") 
    test_list3 = [12,11,13,5,6,7]
    print("Given array is : ")
    print(*test_list3)
    sorted_test_list3 = merge_sort(test_list3)
    print("Sorted array is: ")
    print(*sorted_test_list3)
    print(f"Merge sort not in-place check: {test_list3}")