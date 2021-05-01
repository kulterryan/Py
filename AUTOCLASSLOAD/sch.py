import time
import schedule

from launch import open_class

def bcs():
    open_class.class_bcem()

schedule.every().day.at("12:11").do(bcs)

while True:
    schedule.run_pending()
    time.sleep(1)