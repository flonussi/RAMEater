#!/usr/bin/python

import sys
import time
import psutil
from threading import Thread
import tkinter as Tkinter


def fillUpMemory(speedScaleValue):
    array = []
    while True:
        array.append(' ' * 0x1337 * speedScaleValue.get())
        time.sleep(0.001)


def getMemoryInPercentage():
    totalMem = psutil.virtual_memory().total
    return round(psutil.virtual_memory().used / (totalMem / 100), 1)


def showPleaseWaitSequence(loadingLabelText, usedLabelText):
    i = 0
    while True:
        loadingLabelText.set("Please Wait, EATING RAM" + '.' * (i % 5))
        usedLabelText.set("Used Memory: " + str(getMemoryInPercentage()) + "%")
        i += 1
        time.sleep(0.5)


def startButtonClicked(killButton, startButton, loadingLabelText, usedLabelText, speedScaleValue):
    startButton.config(state=Tkinter.DISABLED)
    killButton.config(state=Tkinter.NORMAL)
    pws = Thread(target=showPleaseWaitSequence, args=(loadingLabelText, usedLabelText,))
    pws.daemon = True
    pws.start()

    ft = Thread(target=fillUpMemory, args=(speedScaleValue,))
    ft.daemon = True
    ft.start()


def killButtonClicked(root):
    root.quit()
    sys.exit()


def initUI(root):
    loadingLabelText = Tkinter.StringVar()
    loadingLabel = Tkinter.Label(root, textvariable=loadingLabelText)

    usedLabelText = Tkinter.StringVar()
    usedLabel = Tkinter.Label(root, textvariable=usedLabelText)

    speedScaleValue = Tkinter.IntVar()
    speedScale = Tkinter.Scale(root, variable=speedScaleValue, orient=Tkinter.HORIZONTAL, length=200, from_=1, to=1337)

    killButton = Tkinter.Button(root, text="EMERGENCY STOP", command=lambda: killButtonClicked(root))
    startButton = Tkinter.Button(root, text="EAT YOUR RAM!!!!", command=lambda: startButtonClicked(killButton, startButton, loadingLabelText, usedLabelText, speedScaleValue))

    killButton.place(x=50, y=150, width=150)
    killButton.config(state=Tkinter.DISABLED)

    startButton.place(x=50, y=55, width=150)

    speedScale.place(x=20, y=0)

    loadingLabel.place(x=50, y=90)
    usedLabel.place(x=60, y=115)


def main():
    root = Tkinter.Tk()
    root.wm_title("RAM EATER DELUXE 4.0.0")
    root.resizable(width=False, height=False)
    root.geometry('{}x{}'.format(250, 200))
    initUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
