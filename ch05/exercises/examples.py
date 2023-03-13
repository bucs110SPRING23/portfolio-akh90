# ending machine
#black box = dont care whats "inside" (HOW it works)

print ("welcome to the vending machine!")
code = input ("enter a code: ")
money = input ("give me money: ")

def my_vending_machine():
    if code == "A":
        if money >= 1:
            print("you got a coke")
        else:
            print ("you need more $$")
    elif code == "B":
        if money >=1.5:
            print ("you got water")
        else:
            print ("you need more $$")
    elif code == "C":
        if money >= 2:
            print ("you got a juice")
    else:
        print ("invalid code")



def foo (var):   #
    var+= 1
    print (var)

