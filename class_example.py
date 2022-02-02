'''
Class 
-----------------------------

A class is a blue print for the object. 

An object has two characteristic.

    1.Attribute 
    2.Behaivior

Syntex: 

Class ClassName (object):
    snippet
    
    making an instance from a class
    objectName = ClassName(arguments)
    
'''

class MyClass:
    '''This is my first Class'''
    a = 10
    def MyFunc(self):
        print('This is a function of my class.')
        

obj = MyClass()
print(obj.a)

obj.MyFunc()

print(obj.__doc__)