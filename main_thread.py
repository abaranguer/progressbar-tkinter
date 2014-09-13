#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from secondary_thread import BackgroundJob
from tkinter import *
from tkinter.ttk import Progressbar
import queue

class MainThread():
    root = None
    queue = None
    counter = None
    value = 0
    popup = None
    
    def onButtonClick(self):
        self.queue = queue.Queue()
        self.popupWindow()
        
        backgroundJob = BackgroundJob(self.queue)
        backgroundJob.start()

    def __init__(self):
        print("Inici")
        print("Aquest és el fil principal")

        self.root = Tk()
        self.root.title("Main window")
        self.root.geometry("320x240")

        label = Label(self.root, text="Prem el botó per executar el fil")
        label.pack(expand = True)

        button = Button(text="Execute", command=self.onButtonClick)
        button.pack()
        # self.root.wait_window()
        self.root.mainloop()
        
    def popupWindow(self):
        self.popup = Toplevel(self.root)
        self.popup.title("Progress window")
        self.popup.geometry("200x50")  
        self.popup.focus()
        self.counter = IntVar()
        self.counter.set(0)
        #label = Label(self.popup, textvariable = self.strVar)
        #label.pack(expand=True)
        pb = Progressbar(self.popup, mode="determinate", orient="horizontal", variable=self.counter, maximum=1000000)
        pb.start()
        pb.pack(expand=True)
        
        self.root.after(100, self.read_queue)
        
    def setValue(self, newValue):
        self.counter.set(newValue)
    
    def read_queue(self):
        try:
            self.value = self.queue.get_nowait()
            print("read from queue: %d" % (self.value))
            self.setValue(self.value)
        except Queue.Empty:
            pass
  
        if self.value < 1000000:
            self.root.after(100, self.read_queue)
        else:
            print("job done")
            self.popup.destroy()

# main
if __name__ == "__main__":
    app = MainThread()
