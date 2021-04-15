# Python
# By Kulter Ryan

# https://github.com/kulterryan/

# Calculating Download Speed of A File
# Last Edit: 09/04/2021

# import Libraries
import time

# Welcome Screen
print("Hi There")
print("Download Time Calculator")
print("** Only 'mbps' to 'MBps' is currently available. ** ")

# Input Screen
downloadspeed =  int(input("Enter Download Speed (in mbps): "))
filesizeF = int(input("Choose the File Size format:\n1. GB\n2. MB\nEnter your Choice: "))

# Predefined
def time_convert(downloadtime):
    return time.strftime("%H:%M:%S", time.gmtime(downloadtime))

# For File Size Consversion
def dt_conversion_mb(downloadspeed):
    filesize_Mb = float(input("Enter File Size (in): ")) # File Size Mb = MegaBytes

    if (filesizeF==1): # For GB Conversion to Bits
        filesize_bit = filesize_Mb * 1000 * 1000 * 1000 * 8
    
    elif (filesizeF==2): # For MB Conversion to Bits
        filesize_bit = filesize_Mb * 1000 * 1000 * 8

    else:
        print("Incorrect Input! See YA!")

    filesize_mb = filesize_bit / (1000*1000)
    # print(filesize_mb)

    downloadtime = filesize_mb / downloadspeed
    # print(downloadtime)

    downloadrate = round(((filesize_mb/8) / downloadtime), 3)
    # print(downloadrate)

    totaltime = time_convert(downloadtime)
    print("Total Download Time (HH:MM:SS):", totaltime)
    print("Rate of File Downloading", downloadrate, "MBs Per Second")


# print("Speed Entered: ", downloadspeed, "mbps")
dt_conversion_mb(downloadspeed)