# Take a input from user and store it into 'title'
title = input('Title: ')

# Take another input from user and store it into 'description'
description = input('Description: ')

# Once done, print Todo Title and Discription
print(title, ":", description)

# Write it into a file so that tasks get preserved.

with open("hello.txt", "w") as f:
    f.write(title)
    f.write(":")
    f.write(description)
    f.write("\n")

with open("hello.txt") as f:
    print(f.read())
