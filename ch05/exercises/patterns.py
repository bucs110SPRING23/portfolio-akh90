#define the function
def star_pyramid (rows):
    for i in range (1, rows+1):
        print ("*" *i)


#define a function
def rstar_pyramid (rows):
    for i in range(rows, 0,-1):  #range(start, stop, step)
        print ("*" * i)


#scope
levels = int(input("enter the desired pyramid height: "))


star_pyramid(levels)
rstar_pyramid(levels)


def bar(x=0, y=2, z=3):
    print (x,y,z)

bar(1, 2, 3)
bar(z=1, x=2)
bar()