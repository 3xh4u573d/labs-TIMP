import sys
import os
import struct

def solve(secret, enc):
    for i in range(8):
        print(chr(48+int(enc[i] ^ (secret[i]-48))), end="") #наш ответ

def main():
    filename = 'LabReverse_kate.exe'
    f = open(filename, "rb")
    f.seek(0, os.SEEK_END)
    size = f.tell()
    f.seek(0, os.SEEK_SET)

    arr = []
    secret = [ord(x) for x in "dulqr8ms"]
    enc = []
    j = 0
    for i in range(0, size):
        b = struct.unpack("B", f.read(1))[0]
        if (j >= 2474148-7 and j <= 2474148):
            enc.append(b)

        arr.append(b)
        if i % 16 == 15:
            arr=[]
        j+=1
    for i in enc:
        print(hex(i), end=" ")
    print()
    secret = [x for x in secret if x != 0]
    solve(secret, enc)

main()
