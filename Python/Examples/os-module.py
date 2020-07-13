import os

# Show current directory
os.getcwd()

# Change directory
os.chdir('C:\\Users\\tsl\\Downloads')

# List files in current directory
os.listdir()

# Open a file
myFile = open('pythontext.txt')

# Read a file
print(myFile.read())

# readlines puts each line as an array index
myFile.readlines()

# Write to a file
myFile = open('pythontext.txt', 'w')
myFile.write('Hello World\n')
myFile.close()


# Append to file without overwriting what's already there
myFile = open('pythontext.txt', 'a')
myFile.write('This is some new text \n')
myFile.close()
