import os
from time import sleep



def connect_device(IP):
    """ This simply connects to the phone with an ip adress"""
    print('connection processing')
    os.system('adb kill-server')
    os.system('adb tcpip 5555')
    os.system(f'adb connect {IP}') # iv set it to a fixed IP, couldnt connect before because IP kept changing
    os.system('adb devices')



def LogIn():
    """ This function logs into the device """   

    print('Powering on')
    print('...')
    os.system('adb shell input keyevent 26')
    print('Logging in')
    os.system('adb shell input touchscreen swipe 340 1000 340 600')
    print('typing password')
    os.system('adb shell input keyevent 9')
    os.system('adb shell input keyevent 13')
    os.system('adb shell input keyevent 14')
    os.system('adb shell input keyevent 14')
    print ('succesfully logged in')


def start_music():
    """ This function starts music """

    os.system('adb shell input keyevent 3')
    print ('home button')
    print ('starting music app')
    sleep(2)
    os.system('adb shell input tap 218 992')
    print('tapped music icon')
    print ('sleep 3 seconds')
    sleep(3)
    print('shuffle selected')
    os.system('adb shell input tap 166 384')
    print ('sleep 1 second')
    sleep(1)
    print ('home button')
    os.system('adb shell input keyevent 3')
    print ('power off')
    os.system('adb shell input keyevent 26')


def stop_music():
    """ This function stops music """

    os.system('adb shell input keyevent 3')
    print ('home button')
    print ('closing music app')
    sleep(2)
    os.system('adb shell input tap 199 1410')
    print('tapped open apps')
    print ('sleep 3 seconds')
    sleep(3)
    print('close all apps')
    os.system('adb shell input tap 360 1210')
    print ('sleep 1 second')
    sleep(1)
    print ('home button')
    os.system('adb shell input keyevent 3')
    print ('power off')
    os.system('adb shell input keyevent 26')