


def longest_increasing_subsequence(nums):
    if not nums:
        return 0

    n = len(nums)
    # Initialize an array to store the length of LIS ending at each index
    lis_lengths = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                lis_lengths[i] = max(lis_lengths[i], lis_lengths[j] + 1)

    # The length of the LIS is the maximum value in the lis_lengths array
    max_length = max(lis_lengths)
    
    # Reconstruct the LIS
    lis = []
    max_index = lis_lengths.index(max_length)
    lis.append(nums[max_index])
    current_length = max_length - 1
    for i in range(max_index - 1, -1, -1):
        if lis_lengths[i] == current_length and nums[i] < lis[-1]:
            lis.append(nums[i])
            current_length -= 1

    return lis[::-1]

# Example usage:
nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print("Longest increasing subsequence:", longest_increasing_subsequence(nums))

# This function longest_increasing_subsequence takes an array of numbers 
# as input and returns the longest increasing subsequence. 
# It uses dynamic programming to compute the length of the longest increasing subsequence 
# ending at each index, and then reconstructs the subsequence using this information.






