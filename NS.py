from tkinter import *
root = Tk()

import tkinter

__author__ = 'tariq'
def CenterWindow(rootobj, width=450, height=450):
    screen_width = (rootobj.winfo_screenwidth() / 2)
    screen_height = (rootobj.winfo_screenheight() / 2)
    rootobj.geometry("%dx%d+%d+%d" % (width, height, (screen_width - (width / 2)), (screen_height - ((height / 2)))))


__author__ = 'tariq'
def PopupWindow(windowtext):
    def close():
        global mainmenu
        if not mainmenu == None:
            mainmenu.deiconify()
        subwindow.destroy()

    subwindow = tkinter.Toplevel(master=root)
    subwindow.configure(background='yellow')
    CenterWindow(subwindow)
    label = tkinter.Label(master=subwindow, text=windowtext, background='blue', foreground='white', font=('Calibri', 16, 'bold'), width=40, height=3)
    label.pack()

    closeButton = tkinter.Button(master=subwindow, text='Sluiten', background='blue', foreground='white', font=('Calibri', 11, 'bold'), command=close)
    closeButton.pack(pady=10)


CenterWindow(root)

root.mainloop()