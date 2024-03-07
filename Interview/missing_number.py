def find_missing(input):
  # calculate sum of all elements 
  # in input list
  sum_of_elements = sum(input)
  
  # There is exactly 1 number missing 
  n = len(input) + 1
  actual_sum = (n * ( n + 1 ) ) / 2
  return actual_sum - sum_of_elements

# Find the sum sum_of_elements of all the numbers in the array. 
# This would require a linear scan, 
# Then find the sum expected_sum of first n numbers using the arithmetic series sum formula
# The difference between these i.e. expected_sum - sum_of_elements, is the missing number in the array.