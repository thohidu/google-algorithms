"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def partition(array, low, high):
    i = low - 1
    pivot = array[high]
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i+1


def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi-1)
        quick_sort(array, pi+1, high)

def quicksort(array):
    low = 0
    high = len(array) - 1
    quick_sort(array, low, high)
    return array



if __name__ == "__main__":
    # Test cases 
    test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    # low = 0
    # high = len(test) - 1
    # quick_sort(test, low, high)
    # print(test)
    print(quicksort(test))

    test_list2 = [10, 7, 8, 9, 1, 5]
    print(quicksort(test_list2))

    test_list3 = [20, -1, -100, 20, -1, 4,7, 13]
    print(quicksort(test_list3))
    