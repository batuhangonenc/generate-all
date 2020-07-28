#-----------------------------------------------------------
#    GenerateAll is a program that generates passwords.
#    Copyright (C) 2020  Batuhan Gonenc.
#
#    GenerateAll is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    GenerateAll is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

secki1 = "1234567890-=!@#$%^&*()_+qwertyuiop[]QWERTYUIOP{}asdfghjkl'\ASDFGHJKL|zxcvbnm<>?/~ZXCVBNM"
secki2 = "1234567890-=!@#$%^&*()_+qwertyuiop[]{}asdfghjkl'\|zxcvbnm<>?/~"
secki3 = "1234567890-=!@#$%^&*()_+[]QWERTYUIOP{}'\ASDFGHJKL|<>?/~ZXCVBNM"
secki4 = "1234567890qwertyuiopQWERTYUIOPasdfghjklASDFGHJKLzxcvbnmZXCVBNM"
secki5 = "-=!@#$%^&*()_+[]{}'\|<>?/~"
from random import randint as rInt
import sys


print("""-----------------------------\nGenerateAll Copyright (C) 2020  Batuhan Gonenc.
GenerateAll comes with ABSOLUTELY NO WARRANTY; for details
read more about GNU General Public License.GenerateAll is free
software, and you are welcome to redistribute it under certain
conditions;for see the conditions visit https://gnu.org/licenses/.
------------------------------------------------------------------""")
while True:
    i1=input('choose one(for options "o"):')
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
        print("----------\nyour new password is-->{}".format(newpassword))

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
        print("----------\nyour new password is-->{}".format(newpassword))
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
        print("----------\nyour new password is-->{}".format(newpassword))
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
        print("----------\nyour new password is-->{}".format(newpassword))

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
        print("----------\nyour new password is-->{}".format(newpassword))

    elif i1 == 'q':
        print('good bye...')
        sys.exit()
    else:
        print("#unvalid input#")
