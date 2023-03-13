num = int(input("enter an upper limit: "))

for i in range (num+1): 
    print ("number: ", i)
    #if not i % 3: 
    if i % 3 == 0:
        print ("fizz")
    elif i % 5 ==0:
        print ("buzz")
    if i % 3 == 0 and i % 5 ==0:
        print ("fizzbuzz")
