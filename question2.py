###This program computes the greatest common divisor (GCD) of two numbers.

factor_num1 = [] #this list stores the factors of the first number

factor_num2 = []  #this list stores the factors of the second number

factors = [] #this list stores the common factors of both numbers

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# This will exit the program if negative integers are entered.    
if num1 < 0 or num2 < 0:
    print("Please enter positive integers only.")
    exit()  
    
for i in range(1,num1 + 1): # This loop finds the factors of the first number
    if num1 % i == 0:
        factor_num1.append(i)
        
for k in range(1,num2 + 1): # This loop finds the factors of the second number
    if num2 % k == 0:
        factor_num2.append(k)
        
for i in factor_num1: # This loop checks for common factors between the two lists
    if i in factor_num2:
        factors.append(i)
        
great_common_divisor = max(factors) # This finds the maximum value in the list of common factors, which is the GCD

print(f"The GCD of {num1} and {num2} is: {great_common_divisor}")