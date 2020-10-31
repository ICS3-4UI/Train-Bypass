from graphics import Train  # Pure graphics and animation script @ graphics.py in the same directory
from threading import *
from time import sleep
from tkinter import messagebox
from tkinter import *
from winsound import *

# Avoid errors if required pip modules isn't installed.
try:
    import config
    from pymsgbox import *
except ModuleNotFoundError:
    print("Required modules not installed!")
    sys.exit("Run (pip install -r requirements.txt) to resolve this issue")


def soundEffect():
    # Wait few seconds to match traffic light
    # Start playing once light turn orange (Animation starts)
    sleep(1.5)
    PlaySound("assets/bgmusic.wav", SND_FILENAME)

    # Play twice if user enables trains passing from both directions
    if config.enableSecT:
        PlaySound("assets/bgmusic.wav", SND_FILENAME)


# Messagebox to make the user confirm they've turned on sound before animation plays
def popupMsgBox():
    root = Tk()
    root.withdraw()
    messagebox.showinfo("Note", "Please turn on sound for a better experience")
    soundConfirmation = confirm(text='Do you have your sound turned on?', title='Confirmation',
                                buttons=["Yes, I have my sound turned on", "No, I don't want to turn on my sound"])
    if soundConfirmation == "Yes, I have my sound turned on":

        # Async background music only works with threading
        # Starting both threads concurrently
        if config.enableSecT:
            messagebox.showwarning("Warning!", "You enabled second train, this is going to cause lag, please expect errors or bugs.")

        graphicsThread.start()
        soundEffectThread.start()
    else:
        messagebox.showerror("Cannot Run Program", "Please turn on sound and try again!")
        sys.exit("This program requires sound.")


def graphics():
    # Tkinter animation is in another script, importing the module to use it.
    Train.animateTrain(None)


# Initiate threads (Graphics and sound needs to be on independent threads)
graphicsThread = Thread(target=graphics)
soundEffectThread = Thread(target=soundEffect)

popupMsgBox()
