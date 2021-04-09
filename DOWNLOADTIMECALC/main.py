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
filesize_Mb =  int(input("Enter File Size (in GB): ")) # File Size Mb = MegaBytes

# Defined

def time_convert(downloadtime):
    return time.strftime("%H:%M:%S", time.gmtime(downloadtime))

def dt_conversion(downloadspeed, filesize_Mb):
    filesize_bit = filesize_Mb * 1000 * 1000 * 1000 * 8 # (1 Gb = Mb * * 1000 mb * 1000 kb * 1000 bytes * 8 bits)
    # print(filesize_bit)

    filesize_mb = filesize_bit / (1000*1000)
    # print(filesize_mb)

    downloadtime = filesize_mb / downloadspeed
    # print(downloadtime)
    totaltime = time_convert(downloadtime)
    print("Total Download Time (HH:MM:SS): ", totaltime)


print("Speed Entered: ", downloadspeed, "mbps")
print("File Size Entered: ", filesize_Mb,  "MB")
dt_conversion(downloadspeed, filesize_Mb)