import os
import tkinter as tk
from tkinter import Canvas, Label, filedialog
from time import sleep


def file_select():
    """ File select GUI button """
    filePath = filedialog.askopenfilename(initialdir=os.path.dirname(__file__), title='Select a File')
    fileName = os.path.basename(filePath)
    selected_filepath = Label(root, text=filePath)
    entry_text.set(fileName)
    entry_path_text.set(filePath)


def Send():
    """ Send GUI button """
    usr_input = entry.get()
    send_text.set('Sending ..')
    source = entry_path_text.get()
    destination = destination_path.get()
    IP = IP_adress.get()

    connect_device(IP)
    copy(source, destination)

    send_text.set('Send')


def connect_device(IP):
    """ This simply connects to the phone with an ip adress"""
    print('connection processing')
    os.system('adb kill-server')
    os.system('adb tcpip 5555')
    os.system(f'adb connect {IP}') # iv set it to a fixed IP, couldnt connect before because IP kept changing
    os.system('adb devices')


def copy(source, destination):
    """ This function uses the adb push cmd to send the file"""
    print ('copying')
    run = os.system(f'adb push "{source}" "{destination}"')


# GUI setup
HEIGHT = 200
WIDTH = 500

root = tk.Tk()
root.title('Send to Android')
root.configure(background='black')
root.geometry('600x100')

# Canvas(height=HEIGHT, width=WIDTH).pack()

header = tk.Label(text='Send file to android phone', fg='white', bg='black')
header.pack()

entry_path_text = tk.StringVar()
entry_path = tk.Entry(root, textvariable=entry_path_text)

entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text, bg='grey')
entry_text.set('Select a file')
entry.pack(side='left')

file_button = tk.Button(root, text='File', bg='grey', command=file_select)
file_button.pack(side='left')

IP_adress_text = tk.StringVar()
IP_adress = tk.Entry(root, textvariable=IP_adress_text, bg='grey')
IP_adress_text.set('10.0.0.109')
IP_adress.pack(side='left')

to = tk.Label(root,text='Destination : ', bg='grey')
to.pack(side='left')

destination_text = tk.StringVar()
destination_path = tk.Entry(root, textvariable=destination_text, bg='grey')
destination_text.set('mnt/sdcard/Dump')
destination_path.pack(side='left')

send_text = tk.StringVar()
send_button = tk.Button(root, textvariable=send_text, bg='grey', command=Send)
send_text.set('Send')
send_button.pack(side='left')

root.mainloop()