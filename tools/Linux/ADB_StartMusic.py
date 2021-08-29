import os
from time import sleep
from scripts.ADB_functions import connect_device, start_music, LogIn


ADB = os.system

IP = '10.0.0.109'

connect_device(IP)

LogIn()

start_music()


# ADB('killall adb.exe')