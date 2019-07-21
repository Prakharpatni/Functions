def addition(x,y):
    return x+y
def sub(x,y):
    return x-y
def multi(x,y):
    return x*y
def div(x,y):
    return x/y

print("Press 1- For Addition")
print("Press 2- For Substraction")
print("Press 3- For Multiplication")
print("Press 4- For Division")
choice=int(input("Please Enter your choice"))

num1=int(input("Please Enter first no."))
num2=int(input("Please Enter second no."))


if(choice==1):
    print("The sum of", num1, "and", num2, "is", addtion(num1,num2))
elif(choice==2):
    print("The substraction of", num1, "and", num2, "is", sub(num1,num2))
elif(choice==3):
    print("The multi of", num1, "and", num2, "is", multi(num1,num2))
elif(choice==4):
    print("The dvision of", num1, "and", num2, "is", div(num1,num2))
else:
    print("Invalid Input")


    






          
