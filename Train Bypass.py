from threading import *
from time import sleep
from tkinter import messagebox
from tkinter import *
from winsound import *

# Avoid errors if required pip modules isn't installed.
try:
    from pymsgbox import *
except ModuleNotFoundError:
    print("Required modules not installed!")
    sys.exit("Run (pip install -r requirements.txt) to resolve this issue")


# Messagebox to make the user confirm they've turned on sound before animation plays
def popupMsgBox():
    root = Tk()
    root.withdraw()
    messagebox.showinfo("Note", "Please turn on sound for a better experience")
    soundConfirmation = confirm(text='Do you have your sound turned on?', title='Confirmation',
                                buttons=["Yes, I have my sound turned on", "No, I don't want to turn on my sound"])
    if soundConfirmation == "Yes, I have my sound turned on":
        # Start the animation by executing the required threads.
        graphicsThread.start()
        soundEffectThread.start()
    else:
        messagebox.showerror("Cannot Run Program", "Please turn on sound and try again!")
        sys.exit("This program requires sound.")


def soundEffect():
    # Wait 3 second to match traffic light
    # Start playing once light turn orange (Animation starts)
    sleep(1)
    PlaySound("assets/bgmusic.wav", SND_FILENAME)
    # sleep(1)
    # PlaySound("assets/bgmusic.wav", SND_FILENAME)


def graphics():
    # Tkinter animation is in another script, importing the module to use it.
    import graphics  # Pure graphics and animation script @ graphics.py in the same directory


# Initiate threads (Graphics and sound needs to be on independent threads)
graphicsThread = Thread(target=graphics)
soundEffectThread = Thread(target=soundEffect)

Thread(target=popupMsgBox).start()
