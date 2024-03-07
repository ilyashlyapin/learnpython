def are_anagrams(str1, str2):
    # Remove spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if the lengths of the strings are the same
    if len(str1) != len(str2):
        return False
    
    # Count the frequency of characters in both strings
    char_count = {}
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Decrement the count for characters in str2
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
        else:
            # If a character is not present in str1, then str1 and str2 can't be anagrams
            return False
    
    # Check if all character counts are zero
    for count in char_count.values():
        if count != 0:
            return False
    
    return True

# Test the function
string1 = "listen"
string2 = "silent"
if are_anagrams(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")