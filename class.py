

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def __str__(self):
#     return f"{self.name}({self.age})"
#
# p1 = Person("John", 36) #agurment
#
# print(p1)


class A:
    def showA():
        print('This is class A')

class B:
    def showB():
        print('This is class B')

class C(A,B):
    def showC():
        print('lThis is class C')

demo=C
demo.showA()
demo.showB()
demo.showC()








