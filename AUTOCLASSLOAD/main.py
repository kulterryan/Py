from launch import open_class as oc

# Welcome Message
print("Automatic Class Loader by KulterRyan")
print("Let's Get Started")

# Import Libraries
import datetime
from dateutil import parser

# Importing Time
time_current = datetime.datetime.now()
print("Current Time: ", time_current)

# hour = int(input("Enter Hour"))
# minute = int(input("Enter Minute"))
# time_bcs = datetime.datetime(hour, minute)

time_bcs = parser.parse(input("Enter Time: "))
time_bcs = time_bcs.hour

if time_current.hour == time_bcs:
    oc.class_bcs()
