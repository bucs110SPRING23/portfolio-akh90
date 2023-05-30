import turtle

class Num:
    
    def __init__(self,n):
        self.data = n #instance varibales for Numb type objects
        self.x = "string"

    #double under
    #no parameters other "self"
    #must return a strong

    def __str__(self):
        obj_str = f"The number is: {self.data}"
        return obj_str
        #NO PRITING





main()