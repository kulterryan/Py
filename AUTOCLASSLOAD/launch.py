import webbrowser

# Sources
# https://docs.python.org/3/library/webbrowser.html

# Defining Google Chrome
def launch_chrome(url):
    # Path to Google Chrome
    chrome_path = chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    # Launching URL in New Tab
    open_chrome = webbrowser.get(chrome_path).open_new(url)

# Defining Classes
class open_class():

    # Engineering Physics
    def class_physics():
        url='https://meet.google.com/ysy-pkoo-ijp?pli=1&authuser=2'
        launch_chrome(url)

    # Engineering Maths
    def class_maths():
        url='https://meet.google.com/qje-ojvn-qcy?pli=1&authuser=2'
        launch_chrome(url)

    # BCEM
    def class_bcem():
        url='https://meet.google.com/hbn-cyps-wnz?pli=1&authuser=2'
        launch_chrome(url)

    # Mechanical
    def class_me():
        url='https://meet.google.com/ozg-hhbx-ynd?pli=1&authuser=2'
        launch_chrome(url)

    # Computer Science
    def class_bcs():
        url='https://meet.google.com/epb-yegf-pcn?pli=1&authuser=2'
        launch_chrome(url)

    # Language
    def class_lls():
        url='https://meet.google.com/ymq-qegs-dfb?pli=1&authuser=2'
        launch_chrome(url)

# Opening Classes Meet Link
print("Launching Maths Class")
open_class.class_maths()
print("Launching Maths Class")
open_class.class_physics()
print("Launching Maths Class")
open_class.class_bcem()
print("Launching Maths Class")
open_class.class_bcs()
print("Launching Maths Class")
open_class.class_lls()
print("Launching Maths Class")
open_class.class_me()
print("Launching Maths Class")