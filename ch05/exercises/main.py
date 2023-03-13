

"""
#local varables get delted at the end of the function
#parameters are local variable 
#in the following, x cannot be printed bc it is defined and confined to that function
def foo():
    local_var = 5 #local scope
    x = 2
def foo():
    local_var = 5 #local scope
    print (X)

global_var = 5 #global scope 


def my_min (x, y, z):
    result = x #local scope
    if result > y:
        result = y
    if result > z:
        result = z
    print ("in my_min: ", result)

result = 0 #global scope
my_min(1,2,3)
print (result)


def foo():
    x=5
    #return none: nonetype
def bar(x=None):
    if x is None:
        x = 5*2

print (foo())

#function returns 1 value

def foo():
    x = 5
    return x #not returning x, returning the value (5)

y = foo()
print (y)


def my_func (x=0):
    return x+x #scoped to my_func
my_func(5)
print(x) #"x" is not defined

"""
def powerof(x=0, p=0):
    power = p
    y = x**power 
    return y

power = 2
result = powerof(5,3)
print(result)
