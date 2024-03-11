# You can rotate an array by K positions in Python using various methods. 
# Here's a simple way to achieve this using array slicing:

def rotate_array(arr, k):
    # Calculate actual rotation index
    k %= len(arr)
    # Rotate the array using slicing
    arr[:] = arr[-k:] + arr[:-k]

# Example usage:
arr = [1, 2, 3, 4, 5]
k = 2
rotate_array(arr, k)
print(arr)  # Output: [4, 5, 1, 2, 3]
