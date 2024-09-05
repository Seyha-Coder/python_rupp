# from machine import array
# import sleep

# list=['name','hello',1]
# list.romve('hello')
# for i in list:
#     print(i)
# dollar=int(input('Please input dollar: '))
# riel=dollar*4100
# print('Rial is: ',riel,' riel')
import math
m = float(input("please input the value of m :"))
n = float(input("please input the value of n :"))
e1= math.pow (math.pow (3 * m + 5,4)+ 1 ,1/3) + math.pow( math.pow(2 * n +1,3)+3,1/4)
e2= math.pow(math.pow(2 * m + 1 ,3) + math.pow(3 * n + 2 ,2 ),1/4) / math.pow(math.pow (5 * m + 2, 2)+ math.pow (2 * n + 1 ,3 ),1/4)
#e3= (math.pow(math.pow(3 * m + 4 ,3),1/5)-(math.pow(2 * n + 1 ,4),1/3)) / math.pow(math.pow(2 * m + 3 ,5 ),1/4) + (math.pow(3 * n + 5 ,5),1/3)
print("The answer of e1 =",e1)
print("The answer of e2 =",e2)
#print("The answer of e3 =",e3)