# Locating Phone Numbers

# importing libraries
import phonenumbers
from phonenumbers import geocoder # For Country
from phonenumbers import carrier

# importing phone number 
from num import phnum

ch_num = phonenumbers.parse(phnum, "CH")
print(geocoder.description_for_number(ch_num, "en"))

carr_num = phonenumbers.parse(phnum, "RO")
print(carrier.name_for_number(carr_num, "en"))

