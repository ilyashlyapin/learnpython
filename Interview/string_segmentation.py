# Given a dictionary of words.
# apple, apple, pear, pie
# Input string of “applepie” can be segmented into dictionary words.
# apple pie
# Input string “applepeer” cannot be segmented into dictionary words.
# apple, peer

def can_segment_string(s, dictionary):
  for i in range(1, len(s) + 1):
    first = s[0:i]
    if first in dictionary:
      second = s[i:]
      if not second or second in dictionary or can_segment_string(second, dictionary):
        return True
  return False

s = "applepie"
dict = ["apple", "apple", "pear", "pie"]
print(can_segment_string(s, dict))


