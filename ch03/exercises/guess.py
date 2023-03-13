import random

num = random.randint(1,10) #both inclusive (random.randrange (1,12,3) = not inclusing 12, 3 is the step)

guess = -1

for i in range (3): 
    guess = int(input("guess a number between 1 and 10: "))

    if guess == num:
        print("correct!", num)
        break
    elif guess < num:
        print("oops too low!")
    else:
        print("oops too high!")




#same as the above, just a different way of stopping **
#for i in range (3):
    #**if guess != num:  
        #guess = int(input("guess a number between 1 and 10: "))

        #if guess == num:
            #print("correct!", num)
        #elif guess < num:
            #print("oop too low!")
        #else:
            #print("oop too high!")
