import locale

class Person:
    def __init__(self, name, age) -> None:
        print('I am from Person Class')
        self.name = name
        self.age = age
        locale.setlocale(locale.LC_ALL, 'en_US')
        
    def walk (self):
        print(f'{self.name.upper()} is now walking')
        
    def run (self):
        print(f'{self.name.upper()} is now running')
    
    def show(self):
        print(f'I am {self.name.upper()} and {self.age} years Old!')

# pr = Person('Takinur', 9)

# pr.walk()
# pr.run()
# pr.show()

#Inheritance -> From Person
class Employee(Person):
    def __init__(self, name, age, salary = 100) -> None:
        super().__init__(name, age)
        print('I am from Employee Class!')
        self.salary = salary
    
    def show(self):
        print(f'I am {self.name.upper()} and {self.age} years Old and Salary is £' + locale.format_string("%d", self.salary, grouping=True))
        
emp = Employee('Sid', 12, 50000)

emp.walk()
emp.run()
emp.show()

