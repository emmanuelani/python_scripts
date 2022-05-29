class Student(object): # Object here i the base class of the class hierarchy.

    school = "UNEC" # This is a class attribute that is applicable to all the class instance.

    def __init__(self, name, age, CGPA):
        self.name = name
        self.age = age
        self.CGPA = CGPA

    def student_info(self):
        print(f'{self.name} has a CGPA of {self.CGPA} and is {self.age} years old')


John = Student("Uhuo John", 24, 4.63)
Emma = Student("Emmanuel Ani", 21, 4.53)
Mike = Student("Elebesunu Emmanuel", 21, 4.65)
Gray = Student("Asika Marvelous", 23, 4.21)
print(John.school)
print(John.CGPA)

print(John.student_info())
print("____________")
print(Emma.student_info())
print("____________")
print(Mike.student_info())
print("____________")
print(Gray.student_info())

class BankAccount(object): # Class uses Camelcase instead of Snake_case.
    '''this is a class that represent the different bank accounts in 
    UBA bank'''

    def __init__(self, balance=0.00):
        #self here is a palceholder that refers to the instances that will be created
        self.balance = balance

    def check_balance(self):
        print(f'Your account balance is {self.balance}.\nThank you for banking with us.')

    def make_deposit(self):
        amount = float(input("How much do you wish to deposi?: "))
        self.balance += amount
        #print new balance
        print(f"Your account balance is {self.balance}.\nThank you for banking with us.")

    def make_withdrawal(self):
        amount = float(input("How much do you wish to withdraw?: "))
        if amount > self.balance:
            print("You do not have sufficient balance in your account to make this transaction.")
        else:
            self.balance -= amount
            #print remaining balance
            print(f'You have succesfully withdrawn {amount}. Your balance is {self.balance}.\nThank you for banking with us')

emmanuel = BankAccount(2000)
print(emmanuel.check_balance())
print(emmanuel.make_deposit())
print(emmanuel.make_withdrawal())


class Student(object):

    def __init__(self, name, age, grade):
        
        self.name = name
        self.age = age
        self.grade = grade
    
how_many_snakes = 1
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Juno
"""


print(snake_string * how_many_snakes)

