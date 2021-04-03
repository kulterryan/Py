# PASSWORD GENERATOR USING PYTHON W/ CLIPBOARD FEATURE

# SOURCE: @python.hub

# importing libraries
import random
import pyperclip as cb

print("Generating Password")

text1 = str('abcdefghijklmnopqrstuvwxyz').lower()
text2 = str('abcdefghijklmnopqrstuvwxyz').upper()

num = str("0123456789")
sym = str("[](){}*;/,_-")

all = text1 + text2 + num + sym # generating string
leg = 16 # length
pwd = "".join(random.sample(all,leg)) # generating password from string

print("Password Generated:", pwd)

print("Do you want to Copy Password to Clipboard:")
print("1.Yes\n2.No")

inpc = str(input("Your Choice: "))
if (inpc=='1'):
    cb.copy(pwd) # Copy to Clipboard
    print("Generated Password Copied to Clipboard!")

else:
    print("Opps! Something went wrong")

print("Exiting Program!")