"""
def foo(parameter1, parameter2):
    return parameter1 + parameter2

def bar(param1=4, param2=3):  #default values, named params
    return param1 + param2 #return ends the function

#foo(1)
bar(1)
bar()
bar(1,3)
bar(param1=1, param2= 2)

foo (1, 2)
"""
def func():
    pass 

def percentage_to_letter(percent):
    let = "A"
    if 80 < percent < 90:
        let = "B"
    elif 70 <=percent < 80:
        let = "C"
    elif 60<=percent < 70:
        let = "D"
    elif percent < 60:
        let = "F"
    return let

def is_passing(letter):
    if letter.lower() in "abc":
        return True
    return False 



def main():
    grades = [90,80,70,60,50]
    for grade in grades:
        letter = percentage_to_letter (grade)
        if is_passing(letter):
            print ("you passed")
        else:
            print("someone messed up your grades!")

"""
if __name__ == "__main__":
    main()

def main(): #driver code , historically called main (where your code starts)

    letter = percentage_to_letter(90)
    if is_passing(letter):
        print("YOU PASSED")
    else:
        print ("someone messed up fr (not you ofc)")\
"""

#programming pattern
#accumulator, loop where you are summing up/accumulating data
'''
result = 0

for i in range(10):
    result = result + i

print (result)
'''''
def remove_vowels(string):
    vowels = "aeiou"
    vowels += vowels.upper()
    result = ""
    for ch in string:
        if ch not in vowels:
            result += ch
    return result

def main():
    mystring = "hello world"
    print (remove_vowels(mystring))
