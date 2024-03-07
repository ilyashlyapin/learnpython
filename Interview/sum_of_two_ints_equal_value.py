def find_sum_of_two(A, val):
  found_values = set()
  for a in A:
    if val - a in found_values:
      return True

    found_values.add(a)
    
  return False

# Scan the whole array once and store visited elements in a hash set.
# During scan, for every element e in the array, we check if val - e is present in the hash set i.e. val - e is already visited.
# If val - e is found in the hash set, it means there is a pair (e, val - e) in array whose sum is equal to the given val.
# If we have exhausted all elements in the array and didn’t find any such pair, the function will return false