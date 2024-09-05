#min max
#input the value of a
a = int(input("please input the value of a:"))
#input the value of b
b = int(input("please input the value of b:"))
#input the value of c
c = int(input("please input the value of c:"))
#input the value of d
d = int(input("please input the value of d:"))

#if else statemant
if a > b:
    max = a
    min = b
else:
    max = b 
    min = a
if  max < c: 
    max = c
if  min > c:
    min = c
if  d > max:
    max = d
if  d < c:
    min = d
if  d < min:
    min = d
#display the anwser
print("The maximum of number is = ", max)
print("The minimum of number is = ", min)