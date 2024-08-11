class Calculator():
    def __init__(self,val1,val2): 
        self.val1=val1
        self.val2=val2


    def addition(self):
        return self.val1+self.val2

    def Subtraction(self):
        return self.val2-self.val1
    
    def Multiple(self):
        return self.val1*self.val2
    
    def Division(self):
        if self.val1 == 0 and self.val2 == 0:
            print('undefined')

        else:
            return self.val1/self.val2
        


obj= Calculator(1,0)
print("Addition",obj.addition())
print("Subtication",obj.Subtraction())
print("Multiple",obj.Multiple())
print("Division",obj.Division())
