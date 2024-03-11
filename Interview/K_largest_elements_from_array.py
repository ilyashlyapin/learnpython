# can find the K largest elements from an array without using any library 
# in Python by implementing your own algorithm. One simple approach is to use sorting. 

def find_k_largest_elements(arr, k):
    # Sort the array in descending order
    arr.sort(reverse=True)
    
    # Return the first K elements
    return arr[:k]

# Example usage:
arr = [3, 10, 4, 7, 15, 20]
k = 3
result = find_k_largest_elements(arr, k)
print("The", k, "largest elements are:", result)