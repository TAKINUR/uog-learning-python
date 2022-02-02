class Calculator:
    def Add (self, x, y):
        return (x+y)
    
    def Sub (self, x, y):
        return (x-y)
    
    def Mul (self, x, y):
        return (x*y)
    
    def Div (self, x, y):
        return (x/y)
    

cal = Calculator()
r = cal.Add(10,20)

print(r)
print(cal.Sub(300, 200))
print(cal.Mul(30, 20))
print(cal.Div(300, 200))

# Initialize Class
class Student:
    #Default Constructor in Class
    def __init__(self):
        print('I am from Constructor of student class!')

#create Object of Student Class
st = Student()

