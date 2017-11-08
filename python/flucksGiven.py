""" Task 2
	In this task, it's assumed you
	completed task 1.
	You'll now learn to:
		- accept user input with input() function
		- use an if/else statement
		- use a comparison operator
"""

# import random module from Python standard library
import random

# define a list of image urls (i.e. list of strings)
imgs = ["img_1","img_2","img_3","img_4"]

# set the served img variable to be a random element from imgs
served_img = imgs[random.randrange(0,len(imgs)-1)]

# output the img
print(served_img)

# --- Task 2 starts here ->

# ask if user wants to fluck it
q = input("Woud you like to fluck? ")


# if they said yes, output a message...

if q == "yes":
    print("here is a message")
    
