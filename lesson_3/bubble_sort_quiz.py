"""Write a function that bubble sorts algorithm."""

def bubble_sort(input_array):
    n = len(input_array)
    for j in range(n-1):
        for i in range(n-1):
            if input_array[i] > input_array[i+1]:
                input_array[i+1], input_array[i] = input_array[i], input_array[i+1]

# Make it bit efficient
def bubble_sort_faster(input_array):
    n = len(input_array)
    for j in range(n-1, 0, -1):
        for i in range(j):
            if input_array[i] > input_array[i+1]:
                input_array[i+1], input_array[i] = input_array[i], input_array[i+1]

            



if __name__ == "__main__":
    # Test cases 
    test_list = [29,3,11,11,19,15,1]
    bubble_sort(test_list)
    print(test_list)
    
    test_list2 = [9,3,11,11,19,15,1]
    bubble_sort_faster(test_list2)
    print(test_list2)



    # [1,3,1,10,12]