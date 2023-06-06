'''
variable:
    a named container that stores a value
    a placeholder, allowing data to be stored,
    manipulated and referenced within program, 
    having a name, data type, data-set (such as
        integer, float, double, string, boolean)
    and optional intial value 
    providing flexibility by allowing values 
        to change during program execution
    used in calculation, control flow, store temporary results, 

    Varible should not have gaped or spaced
    variable should not have semicolon, colon:
    Variable of data type, only can store one value at a time
    Variable of data set can store more than one value of data
    Data is a information
'''
#Initialization
integer = 1 # integer data-type
rate = 9.99 # rate is a variable used store floting point numbers
pi = 3.1415926535897932 # pi is variable store  double data type
name = "billy1234!" # name is variaable store string data type
isskyblue = False # isskyblue is variable store boolean data type

firstNumber = 2
secondNumber = 5
firstNumber = int(input("What's first number: "))
secondNumber = int(input("What's second number: "))
sum = firstNumber + secondNumber

student = []
subject = {}

name = "Anushil"
print(name)

pi = "I have been Changed to this" # pi is variable store string data type
print(pi)
# pi.append("I like to also include in this")

student.append("Billy1234")
student.append("Anushil")
hello = "hello world!"
student.append(hello)
student.append(pi)
student.append(integer)
subject = {"book name": "Science"}
print(student)
print(subject)
print(sum)
print("This is sum of two number:", sum)
