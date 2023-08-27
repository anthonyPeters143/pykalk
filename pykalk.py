#Bring in the basic math functions that are in basicmath.py and nickname that file as bmath
import basicmath as bmath

#This function from the old pykalk.py still prints our answer out
def printAnswer(s):
    print(s)

#Get the data from the user
print("Please enter your first number:")
num1 = float(input())
print("Please enter your operation [+ - * /]:")
oper = input()
print("Please enter your second number:")
num2 = float(input())

#Dispatch whatever basic math function is desired
if (oper == "+"):
    ans = bmath.doAdd(num1, num2)
if (oper == "-"):
    ans = bmath.doSub(num1, num2)
if (oper == "*"):
    ans = bmath.doMul(num1, num2)
if (oper == "/"):
    ans = bmath.doDiv(num1, num2)

#Print the answer out
print(" ")
printAnswer("{0} {1} {2} = {3:.3f}".format(num1, oper, num2, ans))
