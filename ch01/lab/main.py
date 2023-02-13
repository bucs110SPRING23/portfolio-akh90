#Part A
import random

weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)

classes_per_week = 3  #how many times per week a class meets
print ("Classes per week:", classes_per_week)
print (classes_per_week, (type(classes_per_week)))

cost_per_class = (cost_per_week / classes_per_week) 
print ("Cost per class:", cost_per_class)
print (cost_per_class, type(cost_per_class))

print ("that's not too bad!")

#Part B
r1 = random.randint (1,56)
print ("A random number for you:", (r1))

pets = ["cat", "dog", "lizard", "snake", "bird"]
r2 = random.choice (pets)
print ("A pet for you:", (r2))

#l = list()
#i = random.randint (1,675)
#l.append(i)
#print (l)

r3 = ["hi there", "how are you", "you look nice", "69", "you look funny"]
print (random.choice (r3)) #"message 4 you", r3)

git add .



