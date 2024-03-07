# To find the minimum distance between two elements in an array, 
# you can iterate through the array and keep track of the minimum distance 
# encountered between the two elements. 

def minimum_distance(arr, elem1, elem2):
    if elem1 not in arr or elem2 not in arr:
        return -1  # Elements not found in the array
    
    min_dist = float('inf')
    last_seen = None
    
    for i, num in enumerate(arr):
        if num == elem1 or num == elem2:
            if last_seen is not None and arr[i] != arr[last_seen]:
                min_dist = min(min_dist, i - last_seen)
            last_seen = i
    
    return min_dist if min_dist != float('inf') else -1

# Example usage:
arr = [1, 3, 4, 8, 6, 7, 3, 2, 8, 3]
elem1 = 3
elem2 = 8
print(minimum_distance(arr, elem1, elem2))  # Output: 1
