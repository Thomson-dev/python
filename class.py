class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
name = input('what is your name :')
age = input('what your age:')

p1 = Person('Tom', 27)
print(p1.name)
print(p1.age)     
        