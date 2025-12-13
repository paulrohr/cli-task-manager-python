"""
#0,5 bisher kann das programm nur exiten, nicht mehr und ich glaube ich probiere das morgen nochmal nur halt in dem output feld nicht mit
tkinter
"""

import tkinter as tk

root = tk.Tk()
root.title("Personal Task Manager CLI")
root.geometry("400x500")

labeladdtask = tk.Label(root, text="press 1 to Add task")
labeladdtask.pack()

labelshowtask = tk.Label(root, text="press 2 to Show task")
labelshowtask.pack()

labelexitprogramm = tk.Label(root, text="press 3 to exit")
labelexitprogramm.pack()


def keypressed(event):
    if event.char == "3":
        print("you have exited the programm")
        root.quit()


root.bind("<Key>", keypressed)

root.mainloop()
