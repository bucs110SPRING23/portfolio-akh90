#iteration
#iterable = you can loop over it

mystr = "hello" #special iterable list of characters
mynums = [1,2,3,4,5]

for ch in mystr:
    print(ch)

for num in mynums:
    print(num)

#anything iterable can be "indexed" into
print(mystr[0], mystr[1],mystr[2],mystr[3],mystr[4]) #individually prints out each letter in the string

mynums[0] = 5
print(mynums)


#mystr[0]= "J" cannot do this

#mutable = changable, can assign new value to it 
#immutable = cannot be changed once created

num = 5 #can change num, but cannot change 5 (it will never not be the value 5)

mystr = "hello" #immutable
myotherstr = "hello"

mynums = [1,2,3,4,5] #mutable
myothernums = [1,2,3,4,5] #mutable

if mystr == myotherstr:
    print ("they are the same")

if mynums == myothernums:
    print ("they are the same")

if mystr is myotherstr:
    print ("they are the same")

if mynums is myothernums:
    print ("they are the same")


#substring
mystr = "hello"
print (mystr[0] ) 
print (mystr[1:4]) # by adding : you can get substring of overall string

mystr = "h" + mystr [1:5]
print(mystr)

print (mystr.lower(), mystr.upper(), mystr.capitalize(), mystr)

#iterable objects are not always mutable
#slicing with mutable objects

#tuple is immutable lsit