import random
running = True
# import random module from Python standard library DONE

# define a dictionary with image urls and number of flucks

# set the served img variable to be a random element from imgs
# hints: 
#    to put dict keys in a list: list(dict.keys())
#    to choose a random item from a list: random.choice(lst)

# keep asking user if they want to fluck the image until
# they say either 'yes' or 'no'

# if they say 'yes', output a message and increment the flucks
# if they say 'no', serve another image?

# repeat process for another image...
# hint: group blocks of task-specific code into functions?

imgs = {"img1_url": 2, "img2_url": 5, "img3_url": 3, "img4_url": 6, "img5_url" :10}


def flucksGiven():
    lists = imgs.keys()
    num = random.choice(list(lists))
    print(lists)
    q = input("Woud you like to fluck? ")

    if q == "yes":
        print("here is a message")
        if num in imgs:
            imgs[num] += 1
        print(imgs[num])
        exit()

    elif q=="no":
        print(imgs[num])

        #   choice = #another random thing

def main():
    flucksGiven()

while(running):
    main()
