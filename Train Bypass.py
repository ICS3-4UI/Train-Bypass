import signal
from threading import *
from tkinter import *
from tkinter import messagebox
from winsound import *
import os
from pynput.keyboard import Listener


def soundEffect(): PlaySound("assets/bgmusic.wav", SND_FILENAME)


def graphics():
    import graphics  # Please mark my graphics @ graphics.py in the same directory


def on_press(key):
    if str(key).replace('\'', '') == 'q':
        os.kill(os.getpid(), signal.SIGINT)


def keyboardListener():
    with Listener(on_press=on_press) as listener:
        listener.join()


graphicsThread = Thread(target=graphics)
soundEffectThread = Thread(target=soundEffect)
key_listenerThread = Thread(target=keyboardListener)


def popupMsgBox():
    tk = Tk()
    tk.withdraw()
    messagebox.showwarning("Note", "You can't exit until the animation is fully finished!")
    messagebox.showinfo("Note", "Don't worry, the program automatically closes once the animation is finished!")
    messagebox.showinfo("Note", "Force exit by pressing Q on your keyboard")
    messagebox.showinfo("Note", "Please turn on sound for a better experience")
    soundConfirmation = messagebox.askyesno("Confirmation", "I have my sound turned on")
    if soundConfirmation:
        graphicsThread.start()
        soundEffectThread.start()
        key_listenerThread.start()
    else:
        messagebox.showerror("Cannot Run Program", "Please turn on sound and try again!")
        sys.exit()


Thread(target=popupMsgBox).start()
