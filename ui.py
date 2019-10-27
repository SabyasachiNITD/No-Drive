#! /usr/bin/python3
import socket
from tkinter import *
from tkinter.ttk import *
from server import create_server
myip = socket.gethostbyname(socket.gethostname())  
root = Tk()
root.geometry("500x400")
root.iconbitmap("no_drive_icon.ico")
root.resizable(False, False)
root.title("NoDrive")
style = Style() 
style.configure('TButton', font = ('calibri', 24, 'bold'), borderwidth = '4') 
style.map('TButton', foreground = [('active', 'blue')], background = [('active', 'red')]) 
root.grid_columnconfigure(1, weight = 1)
label = Label(root, text = "Send or Recive Files using NoDrive")
label.config(foreground = "red", font = "Verdana 15 bold", justify=CENTER)
label2 = Label(root, text = "Your IP : "+myip)
label2.config(foreground = "green", font = "Verdana 15 bold", justify=CENTER)
label.grid(row = 0, column = 1)
label2.grid(row = 1, column = 1)
button1 = Button(root, text = 'SEND*', command = create_server) 
button1.grid(row = 2, column = 1, pady = 50) 
button2 = Button(root, text = 'RECEIVE', command = None) 
button2.grid(row = 3, column = 1) 
label3 = Label(root, text = "*Your IP needs to be reachable by the client")
label3.config(foreground = "red", font = "Verdana 9 bold", justify=LEFT)
label3.grid(row = 4, column = 1, pady = "50")

root.mainloop()