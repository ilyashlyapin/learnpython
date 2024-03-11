# can rotate a list to the right by k places in Python using slicing. 

def rotate_list_to_right(lst, k):
    if not lst:
        return lst

    k %= len(lst)  # Ensure k is within the range of the list length
    return lst[-k:] + lst[:-k]

# Example usage:
my_list = [1, 2, 3, 4, 5]
k = 2
rotated_list = rotate_list_to_right(my_list, k)
print(rotated_list)  # Output: [4, 5, 1, 2, 3]

# This function takes a list lst and an integer k as input and returns the rotated list. 
# The % operator ensures that k is within the range of the list length. 
# Then, it slices the list to take the last k elements and the remaining elements 
# and concatenates them in the reversed order.