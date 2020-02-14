num1 = input("Number1: ")
num2 = input("Number2: ")
num3 = input("Number3: ")
if(num1 >= num2) and (num1 >= num3):
    largest = num1
elif(num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print("Largest Number is ",largest)