# Source: CodeWithHarry via Youtube
# URL: https://www.youtube.com/watch?v=DePWIOK1STg

# HCF/GDP using Python

num1 = int(input("Enter first number\n"))
num2 = int(input("Enter second number\n"))

if num1 > num2:
    mn = num1   #mn=minimum number
else:
    mn = num2

for i in range(1, mn+1):
    if num1%i==0 and num2%i==0:
        hcf = i

print("The HCF of two numbers is:", hcf)