from threading import *
from time import sleep
from tkinter import messagebox
from tkinter import *
from winsound import *

try:
    from pymsgbox import *
except ModuleNotFoundError:
    print("Required modules not installed!")
    sys.exit("Run (pip install -r requirements.txt) to resolve this issue")


def popupMsgBox():
    root = Tk()
    root.withdraw()
    messagebox.showinfo("Note", "Please turn on sound for a better experience")
    soundConfirmation = confirm(text='Do you have your sound turned on?', title='Confirmation',
                                buttons=["Yes, I have my sound turned on", "No, I don't want to turn on my sound"])
    if soundConfirmation == "Yes, I have my sound turned on":
        graphicsThread.start()
        soundEffectThread.start()
    else:
        messagebox.showerror("Cannot Run Program", "Please turn on sound and try again!")
        sys.exit("This program requires sound.")


def soundEffect():
    sleep(3)
    PlaySound("assets/bgmusic.wav", SND_FILENAME)


def graphics():
    import graphics  # Pure graphics and animation script @ graphics.py in the same directory


graphicsThread = Thread(target=graphics)
soundEffectThread = Thread(target=soundEffect)

Thread(target=popupMsgBox).start()
