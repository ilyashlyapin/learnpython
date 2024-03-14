# To write to files you use the write method.

file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()

# This will create a new file called "newfile.txt" 
# and write the content to it.

# If you want to add content to an existing file, 
# you can open it using the "a" mode, 
# which stand for "append": 

file = open("newfile.txt", "a")

file.write("\nThe Da Vinci Code")
file.close()

# This will add a new line with a new book title to the file.
# Remember, \n stands for a new line.

# The write method returns the number of bytes written 
# to a file, if successful.

msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()


