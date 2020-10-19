import signal
from threading import *
from tkinter import messagebox
from tkinter import *
from pymsgbox import *
from winsound import *
import os
from pynput.keyboard import Listener


def soundEffect(): PlaySound("assets/bgmusic.wav", SND_FILENAME)


def graphics():
    import graphics  # Pure graphics and animation script @ graphics.py in the same directory


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
    messagebox.showwarning("Note",
                           "You can't exit until the animation is fully finished!\n\nDon't worry, the program automatically closes once the "
                           "animation is finished!\n\nForce exit by pressing Q on your keyboard")
    messagebox.showinfo("Note", "Please turn on sound for a better experience")
    soundConfirmation = confirm(text='Do you have your sound turned on?', title='Confirmation',
                                buttons=["Yes, I have my sound turned on", "No, I don't want to turn on my sound"])
    if soundConfirmation == "Yes, I have my sound turned on":
        graphicsThread.start()
        soundEffectThread.start()
        key_listenerThread.start()
    else:
        messagebox.showerror("Cannot Run Program", "Please turn on sound and try again!")


Thread(target=popupMsgBox).start()
