# Source: CodeWithHarry via Youtube
# URL: https://www.youtube.com/watch?v=hSTZ4Pi51lI

# LCM of two numbers using Python

x = int(input("Enter first number\n"))
y = int(input("Enter second number\n"))

maxNum = max(x ,y)

while(True):
    if( maxNum%x == 0 and maxNum%y == 0):
        break
    maxNum = maxNum + 1

print(f"The LCM of {x} and {y} is {maxNum}")
