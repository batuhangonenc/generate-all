"""
 The MIT License (MIT)

Copyright © 2020 Batuhan Gonenc

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

secki1 = "1234567890-=!@#$%^&*()_+qwertyuiop[]QWERTYUIOP{}asdfghjkl'\ASDFGHJKL|zxcvbnm<>?/~ZXCVBNM"
secki2 = "1234567890-=!@#$%^&*()_+qwertyuiop[]{}asdfghjkl'\|zxcvbnm<>?/~"
secki3 = "1234567890-=!@#$%^&*()_+[]QWERTYUIOP{}'\ASDFGHJKL|<>?/~ZXCVBNM"
secki4 = "1234567890qwertyuiopQWERTYUIOPasdfghjklASDFGHJKLzxcvbnmZXCVBNM"
secki5 = "-=!@#$%^&*()_+[]{}'\|<>?/~"
from random import randint as rInt
import sys


print("-----------\nGenerateAll")
while True:
    i1=input('----------------------------\nchoose one(for options "o"):')
    if i1 =='o':
        print("----------\n1 - generate with all characters\n2 - generate except uppercase\n3 - generate except lowercase \n4 - generate with only alphabet and numbers\n5 - generate except alphabet and numbers\nq - quit\n-----------")
        
    elif i1 == '1':
        i2 = input("how many characters will your password contain?")
        try:
            i2 = int(i2)
        except:
            print("#this input must be integer.#")
            continue
        if i2  > 1000:
            print("-----\nwhy did you do this..just..\n-----\ni didn't understand\n-----\ntry something less.\ndon't be a paranoid.")
            continue
        newpassword = ""
        while i2 > 0:
            r_int = rInt(1,len(secki1))-1
            new_char = secki1[r_int]
            newpassword = newpassword + new_char
            i2 = i2 - 1
        print("----------\nyour new password is below.\n-----\n{}".format(newpassword))

    elif i1 == '2':
        i2 = input("how many characters will your password contain?")
        try:
            i2 = int(i2)
        except:
            print("#this input must be integer.#")
            continue
        if i2 > 1000:
            print("-----\nwhy did you do this..just..\n-----\ni didn't understand\n-----\ntry something less.\ndon't be a paranoid.")
            continue
        newpassword = ""
        while i2 > 0:
            r_int = rInt(1,len(secki2))-1
            new_char = secki2[r_int]
            newpassword = newpassword + new_char
            i2 = i2 - 1
        print("----------\nyour new password is below.\n-----\n{}".format(newpassword))
    elif i1 == '3':
        i2 = input("how many characters will your password contain?")
        try:
            i2 = int(i2)
        except:
            print("#this input must be integer.#")
            continue
        if i2 > 1000:
            print("-----\nwhy did you do this..just..\n-----\ni didn't understand\n-----\ntry something less.\ndon't be a paranoid.")
            continue
        newpassword = ""
        while i2 > 0:
            r_int = rInt(1,len(secki3))-1
            new_char = secki3[r_int]
            newpassword = newpassword + new_char
            i2 = i2 - 1
        print("----------\nyour new password is below.\n-----\n{}".format(newpassword))
    elif i1 == '4':
        i2 = input("how many characters will your password contain?")
        try:
            i2 = int(i2)
        except:
            print("#this input must be integer.#")
            continue
        if i2 > 1000:
            print("-----\nwhy did you do this..just..\n-----\ni didn't understand\n-----\ntry something less.\ndon't be a paranoid.")
            continue
        newpassword = ""
        while i2 > 0:
            r_int = rInt(1,len(secki4))-1
            new_char = secki4[r_int]
            newpassword = newpassword + new_char
            i2 = i2 - 1
        print("----------\nyour new password is below.\n-----\n{}".format(newpassword))

    elif i1 == '5':
        i2 = input("how many characters will your password contain?")
        try:
            i2 = int(i2)
        except:
            print("#this input must be integer.#")
            continue
        if i2 > 1000:
            print("-----\nwhy did you do this..just..\n-----\ni didn't understand\n-----\ntry something less.\ndon't be a paranoid.")
            continue
        newpassword = ""
        while i2 > 0:
            r_int = rInt(1,len(secki5))-1
            new_char = secki5[r_int]
            newpassword = newpassword + new_char
            i2 = i2 - 1
        print("----------\nyour new password is below.\n-----\n{}".format(newpassword))

    elif i1 == 'q':
        print('good bye...')
        sys.exit()
    else:
        print("#unvalid input#")
