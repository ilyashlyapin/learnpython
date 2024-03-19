# You can use Python to read and write the contents of files.
# This is particularly useful when you need to work 
# with a lot of data that is saved in a file. 
# For example, in data science and analytics, 
# the data is commonly in CSV (comma-separated values) files.
# Let's start by working with text files, 
# as they are the easiest to manipulate. 
# Before a file can be edited, it must be opened, 
# using the open function.
myfile = open("filename.txt")

# # You can specify the mode used to open a file 
# by applying a second argument to the open function.
# Sending "r" means open in read mode, which is the default. 
# Sending "w" means write mode, 
# for rewriting the contents of a file.

# Sending "a" means append mode, 
# for adding new content to the end of the file.
# Adding "b" to a mode opens it in binary mode, 
# which is used for non-text files (such as image and sound files).

# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary write mode
open("filename.txt", "wb")

# Once a file has been opened and used, you should close it.
# This is done with the close method of the file object. 

file = open("filename.txt", "w")
# do stuff to the file
file.close()

# The contents of a file that has been opened in text mode 
# can be read using the read method. 
# We have created a books.txt file on the server 
# which includes titles of books. 
# Let's read the file and output the content:

file = open("/usercode/files/books.txt")
cont = file.read()
print(cont)
file.close()

# To read only a certain amount of a file, 
# you can provide the number of bytes to read 
# as an argument to the read function. 
# Each ASCII character is 1 byte: 

file = open("/usercode/files/books.txt")
print(file.read(5))
print(file.read(7))
print(file.read())
file.close()

# To retrieve each line in a file, you can use the readlines() 
# method to return a list in which each element is a line in the file.

file = open("/usercode/files/books.txt")

for line in file.readlines():
    print(line)

# If you do not need the list for each line, 
# you can simply iterate over the file variable:
    
file = open("/usercode/files/books.txt")

for line in file:
    print(line)
    
file.close()

# Task. You need to make a program to read the given number 
# of characters of a file.
# Take a number N as input and output the first N characters
# of the books.txt file.

file = open("/usercode/files/books.txt", "r")
#your code goes here

n = int(input())
l = file.read()

print(l[:n])
file.close()
