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
from datetime import datetime
import sys


print("---------------------------------------------\nGenerateAll Copyright (c) 2020 Batuhan Gonenc\n---------------------------------------------")
while True:
    i1=input('----------------------------\nchoose one(for options "o"):')
    if i1 =='o':
        print("----------\n1 - generate with all characters\n2 - generate except uppercase\n3 - generate except lowercase \n4 - generate with only alphabet and numbers\n5 - generate except alphabet and numbers\nq - quit\n-----------")
    
    elif i1 == 'q':
        print('good bye...')
        sys.exit()



    elif (i1 == "1"):
        passwords = ""
        secki = secki1
        while 1:
            try:    
                timesinp = input("-----\nhow many passwords do you want? :")
                timesinp = int(timesinp)
                
                break
            except:
                print("-----\nthis input must be a positive integer .")
                continue

            if timesinp <= 0:
                print("-----\nthis input must be a positive integer .")
                continue

        i2 = input("how many characters will your password contain?")
        
        backupi2 = 0
        try:
            i2 = int(i2)
            backupi2 = i2
        except:
            print("#this input must be integer.#")
            continue


        if i2  > 1000:
            print("-----\nwhy did you do this..just..\n-----\ni didn't understand\n-----\ntry something less.\ndon't be a paranoid.")
            continue
        while timesinp > 0:
            i2 = backupi2
            newpassword = ""
            while i2 > 0:
                r_int = rInt(1,len(secki))-1
                new_char = secki[r_int]
                newpassword = newpassword + new_char
                i2 = i2 - 1
            if timesinp == 1:
                print("----------\nyour new passwords are above.")
                break

            print("{}\n".format(newpassword))
            passwords += "{}\n\n".format(newpassword)
            timesinp -= 1

        while 1:
            savein = input("-----\n\ndo you want to save it ? ( y / n ) :")

            if savein == "y":
                filename = input("write a file name:")

                try:
                    file = open("{}.txt".format(filename),"w")
                    
                    now = datetime.now()
                    now = now.strftime("%x %X")
                    content = "{}\n\n\n{} passwords above\n\n{}".format(passwords,backupi2,now)

                    file.write(content)
                    file.close()

                    print("-----\npasswords saved successfully.")

                    break
                except:
                    print("-----\nyou should enter a valid file name.")
                    continue


            elif savein == "n":
                break

            else:
                print("-----\n#unvalid input#")
                continue

    elif (i1 == "2"):
        passwords = ""
        secki = secki2
        while 1:
            try:    
                timesinp = input("-----\nhow many passwords do you want? :")
                timesinp = int(timesinp)
                
                break
            except:
                print("-----\nthis input must be a positive integer .")
                continue

            if timesinp <= 0:
                print("-----\nthis input must be a positive integer .")
                continue

        i2 = input("how many characters will your password contain?")
        
        backupi2 = 0
        try:
            i2 = int(i2)
            backupi2 = i2
        except:
            print("#this input must be integer.#")
            continue


        if i2  > 1000:
            print("-----\nwhy did you do this..just..\n-----\ni didn't understand\n-----\ntry something less.\ndon't be a paranoid.")
            continue
        while timesinp > 0:
            i2 = backupi2
            newpassword = ""
            while i2 > 0:
                r_int = rInt(1,len(secki))-1
                new_char = secki[r_int]
                newpassword = newpassword + new_char
                i2 = i2 - 1
            if timesinp == 1:
                print("----------\nyour new passwords are above.")
                break

            print("{}\n".format(newpassword))
            passwords += "{}\n\n".format(newpassword)
            timesinp -= 1

        while 1:
            savein = input("-----\n\ndo you want to save it ? ( y / n ) :")

            if savein == "y":
                filename = input("write a file name:")

                try:
                    file = open("{}.txt".format(filename),"w")
                    
                    now = datetime.now()
                    now = now.strftime("%x %X")
                    content = "{}\n\n\n{} passwords above\n\n{}".format(passwords,backupi2,now)

                    file.write(content)
                    file.close()

                    print("-----\npasswords saved successfully.")

                    break
                except:
                    print("-----\nyou should enter a valid file name.")
                    continue


            elif savein == "n":
                break

            else:
                print("-----\n#unvalid input#")
                continue
    elif (i1 == "3"):
        passwords = ""
        secki = secki3
        while 1:
            try:    
                timesinp = input("-----\nhow many passwords do you want? :")
                timesinp = int(timesinp)
                
                break
            except:
                print("-----\nthis input must be a positive integer .")
                continue

            if timesinp <= 0:
                print("-----\nthis input must be a positive integer .")
                continue

        i2 = input("how many characters will your password contain?")
        
        backupi2 = 0
        try:
            i2 = int(i2)
            backupi2 = i2
        except:
            print("#this input must be integer.#")
            continue


        if i2  > 1000:
            print("-----\nwhy did you do this..just..\n-----\ni didn't understand\n-----\ntry something less.\ndon't be a paranoid.")
            continue
        while timesinp > 0:
            i2 = backupi2
            newpassword = ""
            while i2 > 0:
                r_int = rInt(1,len(secki))-1
                new_char = secki[r_int]
                newpassword = newpassword + new_char
                i2 = i2 - 1
            if timesinp == 1:
                print("----------\nyour new passwords are above.")
                break

            print("{}\n".format(newpassword))
            passwords += "{}\n\n".format(newpassword)
            timesinp -= 1

        while 1:
            savein = input("-----\n\ndo you want to save it ? ( y / n ) :")

            if savein == "y":
                filename = input("write a file name:")

                try:
                    file = open("{}.txt".format(filename),"w")
                    
                    now = datetime.now()
                    now = now.strftime("%x %X")
                    content = "{}\n\n\n{} passwords above\n\n{}".format(passwords,backupi2,now)

                    file.write(content)
                    file.close()

                    print("-----\npasswords saved successfully.")

                    break
                except:
                    print("-----\nyou should enter a valid file name.")
                    continue


            elif savein == "n":
                break

            else:
                print("-----\n#unvalid input#")
                continue
    elif (i1 == "4"):
        passwords = ""
        secki = secki4
        while 1:
            try:    
                timesinp = input("-----\nhow many passwords do you want? :")
                timesinp = int(timesinp)
                
                break
            except:
                print("-----\nthis input must be a positive integer .")
                continue

            if timesinp <= 0:
                print("-----\nthis input must be a positive integer .")
                continue

        i2 = input("how many characters will your password contain?")
        
        backupi2 = 0
        try:
            i2 = int(i2)
            backupi2 = i2
        except:
            print("#this input must be integer.#")
            continue


        if i2  > 1000:
            print("-----\nwhy did you do this..just..\n-----\ni didn't understand\n-----\ntry something less.\ndon't be a paranoid.")
            continue
        while timesinp > 0:
            i2 = backupi2
            newpassword = ""
            while i2 > 0:
                r_int = rInt(1,len(secki))-1
                new_char = secki[r_int]
                newpassword = newpassword + new_char
                i2 = i2 - 1
            if timesinp == 1:
                print("----------\nyour new passwords are above.")
                break

            print("{}\n".format(newpassword))
            passwords += "{}\n\n".format(newpassword)
            timesinp -= 1

        while 1:
            savein = input("-----\n\ndo you want to save it ? ( y / n ) :")

            if savein == "y":
                filename = input("write a file name:")

                try:
                    file = open("{}.txt".format(filename),"w")
                    
                    now = datetime.now()
                    now = now.strftime("%x %X")
                    content = "{}\n\n\n{} passwords above\n\n{}".format(passwords,backupi2,now)

                    file.write(content)
                    file.close()

                    print("-----\npasswords saved successfully.")

                    break
                except:
                    print("-----\nyou should enter a valid file name.")
                    continue


            elif savein == "n":
                break

            else:
                print("-----\n#unvalid input#")
                continue
    elif (i1 == "5"):
        passwords = ""
        secki = secki5
        while 1:
            try:    
                timesinp = input("-----\nhow many passwords do you want? :")
                timesinp = int(timesinp)
                
                break
            except:
                print("-----\nthis input must be a positive integer .")
                continue

            if timesinp <= 0:
                print("-----\nthis input must be a positive integer .")
                continue

        i2 = input("how many characters will your password contain?")
        
        backupi2 = 0
        try:
            i2 = int(i2)
            backupi2 = i2
        except:
            print("#this input must be integer.#")
            continue


        if i2  > 1000:
            print("-----\nwhy did you do this..just..\n-----\ni didn't understand\n-----\ntry something less.\ndon't be a paranoid.")
            continue
        while timesinp > 0:
            i2 = backupi2
            newpassword = ""
            while i2 > 0:
                r_int = rInt(1,len(secki))-1
                new_char = secki[r_int]
                newpassword = newpassword + new_char
                i2 = i2 - 1
            if timesinp == 1:
                print("----------\nyour new passwords are above.")
                break

            print("{}\n".format(newpassword))
            passwords += "{}\n\n".format(newpassword)
            timesinp -= 1

        while 1:
            savein = input("-----\n\ndo you want to save it ? ( y / n ) :")

            if savein == "y":
                filename = input("write a file name:")

                try:
                    file = open("{}.txt".format(filename),"w")
                    
                    now = datetime.now()
                    now = now.strftime("%x %X")
                    content = "{}\n\n\n{} passwords above\n\n{}".format(passwords,backupi2,now)

                    file.write(content)
                    file.close()


                    print("-----\npasswords saved successfully.")
                    break
                except:
                    print("-----\nyou should enter a valid file name.")
                    continue


            elif savein == "n":
                break

            else:
                print("-----\n#unvalid input#")
                continue

  
    else:
        print("#unvalid input#")
