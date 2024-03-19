# It is good practice to avoid wasting resources 
# by making sure that files are always closed 
# after they have been used. One way of doing this is 
# to use try and finally.

try:
  f = open("/usercode/files/books.txt")
  cont = f.read()
  print(cont)
finally:
  f.close()

#  An alternative way of doing this is by using with statements.
# This creates a temporary variable (often called f),  
# which is only accessible in the indented block 
# of the with statement. 
  
with open("/usercode/files/books.txt") as f:
  print(f.read())

# Task: You are given a books.txt file, 
# which includes book titles, each on a separate line.
# Create a program to output how many words 
# each title contains, in the following format:
# Line 1: 3 words
# Line 2: 5 words
# ...
# Make sure to match the above mentioned format in the output.

with open("/usercode/files/books.txt") as f:
   #your code goes here
   j=1
   for line in f:
      print("Line " + str(j)+": "+str(len(line.split(" ")))+" words")
      j+=1