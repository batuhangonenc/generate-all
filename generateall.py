"""
 The MIT License (MIT)

Copyright © 2020 Batuhan Gonenc

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
seckiliste = ["&","$","'","|","1","2","3","4","5","6","7","8","9","0","-","=","!","@","#","%","^","*","(",")","+","q","w",
"e","r","t","y","u","i","o","p","[","]","Q","W","E","R","T","Y","U","I","O","P","{","}","a","s","d","f","g","h","j","k",
"l","A","S","D","F","G","H","J","K","L","z","x","c","v","b","n","m","?","/","~","Z","X","C","V","B","N","M",":",
";","<",">","~"]
secki1 = "1234567890-=!@#$%^&*()_+qwertyuiop[]QWERTYUIOP{}asdfghjkl'\ASDFGHJKL|zxcvbnm<>?/~ZXCVBNM"
secki2 = "1234567890-=!@#$%^&*()_+qwertyuiop[]{}asdfghjkl'\|zxcvbnm<>?/~"
secki3 = "1234567890-=!@#$%^&*()_+[]QWERTYUIOP{}'\ASDFGHJKL|<>?/~ZXCVBNM"
secki4 = "1234567890qwertyuiopQWERTYUIOPasdfghjklASDFGHJKLzxcvbnmZXCVBNM"
secki5 = "-=!@#$%^&*()_+[]{}'\|<>?/~"
from random import randint as rInt
from datetime import datetime
from time import time

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
                backuptimesinp = timesinp
                
                break
            except:
                print("-----\nthis input must be a positive integer .")
                continue

            if timesinp <= 0:
                print("-----\nthis input must be a positive integer .")
                continue

        i2 = input("how many characters will your password contain? :")
        
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
        
        time1 = time()
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
                
                time2 = time()
                
                break

            print("{}\n".format(newpassword))
            passwords += "{}\n\n".format(newpassword)
            timesinp -= 1

        while 1:
            savein = input("-----\n\ndo you want to save it ? ( y / n ) :")
            detailsinp = input("-----\ndo you want more details about passwords in your save? ( y / n ) :")


            if savein == "y":
                stats=""

                filename = input("write a file name:")

                try:
                    file = open("{}.txt".format(filename),"w")
                    
                    now = datetime.now()
                    now = now.strftime("%x %X")
                    

                    if detailsinp == "y":
                        comparedata = ""
                        comparelist = list()
                        highs="\n\nmost used characters"
                        lows="\n\nless used characters"
                        takes = time2 - time1

                        
                        raw_passwords = passwords.replace("\n","")

                        
                        backupsl = seckiliste.copy()
                        for i in seckiliste:
                            if (secki.count(i) == 0):
                                backupsl.remove(i)


                        for i in backupsl:
                            microstat1 = raw_passwords.count(i)

                            singlestat = "\n\n{}  , used for {} times".format(i,microstat1)

                            stats += singlestat
                            comparelist.append("{}ara{}".format(i,microstat1))
                            
                            
                        

                        #comparing
                        backupcomp = comparelist.copy()
                        backup2comp = comparelist.copy()

                        
                        bestchar = ""

                        
                        bestct = 5
                        while (bestct > 0):
                            best = 0
                            for i in backupcomp:
                                data = i.split("ara")
                                
                                
                                thechar = data[0]
                                timesforchar = int(data[1])

                                if (timesforchar > best):
                                    best = timesforchar
                                    bestchar = thechar


                            highs += "\n\n{}. {} , used for {} times".format(int(6-bestct),bestchar,best)

                            willRemoved = "{}ara{}".format(bestchar,best)
                            
                            backupcomp.remove(willRemoved)
                            bestct -= 1

                        worst = 10000000000
                        worstchar = ""
                        worstct = 5

                        while (worstct > 0):
                            worst = 10000000000
                            for i in backup2comp:
                                data = i.split("ara")

                                thechar = data[0]
                                timesforchar = int(data[1])

                                if timesforchar < worst:
                                    worst = timesforchar
                                    worstchar = thechar


                            lows += "\n\n{}. {} , used for {} times".format(int(6-worstct),worstchar,worst)

                            willRemoved = "{}ara{}".format(worstchar,worst)
                            backup2comp.remove(willRemoved)
                            worstct -= 1
                        comparedata = highs + lows

                        stats += comparedata
                    
                        stats += "\n\nit took about {} seconds to compute".format(takes)

                    content = "{}\n\n{} passwords above{}\n\n{}".format(passwords,backuptimesinp,stats,now)

                
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
                backuptimesinp = timesinp
                
                break
            except:
                print("-----\nthis input must be a positive integer .")
                continue

            if timesinp <= 0:
                print("-----\nthis input must be a positive integer .")
                continue

        i2 = input("how many characters will your password contain? :")
        
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
        
        time1 = time()
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
                
                time2 = time()
                
                break

            print("{}\n".format(newpassword))
            passwords += "{}\n\n".format(newpassword)
            timesinp -= 1

        while 1:
            savein = input("-----\n\ndo you want to save it ? ( y / n ) :")
            detailsinp = input("-----\ndo you want more details about passwords in your save? ( y / n ) :")


            if savein == "y":
                stats=""

                filename = input("write a file name:")

                try:
                    file = open("{}.txt".format(filename),"w")
                    
                    now = datetime.now()
                    now = now.strftime("%x %X")
                    

                    if detailsinp == "y":
                        comparedata = ""
                        comparelist = list()
                        highs="\n\nmost used characters"
                        lows="\n\nless used characters"
                        takes = time2 - time1

                        
                        raw_passwords = passwords.replace("\n","")

                        
                        backupsl = seckiliste.copy()
                        for i in seckiliste:
                            if (secki.count(i) == 0):
                                backupsl.remove(i)


                        for i in backupsl:
                            microstat1 = raw_passwords.count(i)

                            singlestat = "\n\n{}  , used for {} times".format(i,microstat1)

                            stats += singlestat
                            comparelist.append("{}ara{}".format(i,microstat1))
                            
                            
                        
                        #comparing
                        backupcomp = comparelist.copy()
                        backup2comp = comparelist.copy()

                        
                        bestchar = ""

                        
                        bestct = 5
                        while (bestct > 0):
                            best = 0
                            for i in backupcomp:
                                data = i.split("ara")
                                
                                
                                thechar = data[0]
                                timesforchar = int(data[1])

                                if (timesforchar > best):
                                    best = timesforchar
                                    bestchar = thechar


                            highs += "\n\n{}. {} , used for {} times".format(int(6-bestct),bestchar,best)

                            willRemoved = "{}ara{}".format(bestchar,best)
                            
                            backupcomp.remove(willRemoved)
                            bestct -= 1

                        worst = 10000000000
                        worstchar = ""
                        worstct = 5

                        while (worstct > 0):
                            worst = 10000000000
                            for i in backup2comp:
                                data = i.split("ara")

                                thechar = data[0]
                                timesforchar = int(data[1])

                                if timesforchar < worst:
                                    worst = timesforchar
                                    worstchar = thechar


                            lows += "\n\n{}. {} , used for {} times".format(int(6-worstct),worstchar,worst)

                            willRemoved = "{}ara{}".format(worstchar,worst)
                            backup2comp.remove(willRemoved)
                            worstct -= 1
                        comparedata = highs + lows

                        stats += comparedata
                    
                        stats += "\n\nit took about {} seconds to compute".format(takes)

                    content = "{}\n\n{} passwords above{}\n\n{}".format(passwords,backuptimesinp,stats,now)

                
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
                backuptimesinp = timesinp
                
                break
            except:
                print("-----\nthis input must be a positive integer .")
                continue

            if timesinp <= 0:
                print("-----\nthis input must be a positive integer .")
                continue

        i2 = input("how many characters will your password contain? :")
        
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
        
        time1 = time()
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
                
                time2 = time()
                
                break

            print("{}\n".format(newpassword))
            passwords += "{}\n\n".format(newpassword)
            timesinp -= 1

        while 1:
            savein = input("-----\n\ndo you want to save it ? ( y / n ) :")
            detailsinp = input("-----\ndo you want more details about passwords in your save? ( y / n ) :")


            if savein == "y":
                stats=""

                filename = input("write a file name:")

                try:
                    file = open("{}.txt".format(filename),"w")
                    
                    now = datetime.now()
                    now = now.strftime("%x %X")
                    

                    if detailsinp == "y":
                        comparedata = ""
                        comparelist = list()
                        highs="\n\nmost used characters"
                        lows="\n\nless used characters"
                        takes = time2 - time1

                        
                        raw_passwords = passwords.replace("\n","")

                        
                        backupsl = seckiliste.copy()
                        for i in seckiliste:
                            if (secki.count(i) == 0):
                                backupsl.remove(i)


                        for i in backupsl:
                            microstat1 = raw_passwords.count(i)

                            singlestat = "\n\n{}  , used for {} times".format(i,microstat1)

                            stats += singlestat
                            comparelist.append("{}ara{}".format(i,microstat1))
                            
                            
                        
                        #comparing
                        backupcomp = comparelist.copy()
                        backup2comp = comparelist.copy()

                        
                        bestchar = ""

                        
                        bestct = 5
                        while (bestct > 0):
                            best = 0
                            for i in backupcomp:
                                data = i.split("ara")
                                
                                
                                thechar = data[0]
                                timesforchar = int(data[1])

                                if (timesforchar > best):
                                    best = timesforchar
                                    bestchar = thechar


                            highs += "\n\n{}. {} , used for {} times".format(int(6-bestct),bestchar,best)

                            willRemoved = "{}ara{}".format(bestchar,best)
                            
                            backupcomp.remove(willRemoved)
                            bestct -= 1

                        worst = 10000000000
                        worstchar = ""
                        worstct = 5

                        while (worstct > 0):
                            worst = 10000000000
                            for i in backup2comp:
                                data = i.split("ara")

                                thechar = data[0]
                                timesforchar = int(data[1])

                                if timesforchar < worst:
                                    worst = timesforchar
                                    worstchar = thechar


                            lows += "\n\n{}. {} , used for {} times".format(int(6-worstct),worstchar,worst)

                            willRemoved = "{}ara{}".format(worstchar,worst)
                            backup2comp.remove(willRemoved)
                            worstct -= 1
                        comparedata = highs + lows

                        stats += comparedata
                    
                        stats += "\n\nit took about {} seconds to compute".format(takes)

                    content = "{}\n\n{} passwords above{}\n\n{}".format(passwords,backuptimesinp,stats,now)

                
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
                backuptimesinp = timesinp
                
                break
            except:
                print("-----\nthis input must be a positive integer .")
                continue

            if timesinp <= 0:
                print("-----\nthis input must be a positive integer .")
                continue

        i2 = input("how many characters will your password contain? :")
        
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
        
        time1 = time()
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
                
                time2 = time()
                
                break

            print("{}\n".format(newpassword))
            passwords += "{}\n\n".format(newpassword)
            timesinp -= 1

        while 1:
            savein = input("-----\n\ndo you want to save it ? ( y / n ) :")
            detailsinp = input("-----\ndo you want more details about passwords in your save? ( y / n ) :")


            if savein == "y":
                stats=""

                filename = input("write a file name:")

                try:
                    file = open("{}.txt".format(filename),"w")
                    
                    now = datetime.now()
                    now = now.strftime("%x %X")
                    

                    if detailsinp == "y":
                        comparedata = ""
                        comparelist = list()
                        highs="\n\nmost used characters"
                        lows="\n\nless used characters"
                        takes = time2 - time1

                        
                        raw_passwords = passwords.replace("\n","")

                        
                        backupsl = seckiliste.copy()
                        for i in seckiliste:
                            if (secki.count(i) == 0):
                                backupsl.remove(i)


                        for i in backupsl:
                            microstat1 = raw_passwords.count(i)

                            singlestat = "\n\n{}  , used for {} times".format(i,microstat1)

                            stats += singlestat
                            comparelist.append("{}ara{}".format(i,microstat1))
                            
                            
                        
                        #comparing
                        backupcomp = comparelist.copy()
                        backup2comp = comparelist.copy()

                        
                        bestchar = ""

                        
                        bestct = 5
                        while (bestct > 0):
                            best = 0
                            for i in backupcomp:
                                data = i.split("ara")
                                
                                
                                thechar = data[0]
                                timesforchar = int(data[1])

                                if (timesforchar > best):
                                    best = timesforchar
                                    bestchar = thechar


                            highs += "\n\n{}. {} , used for {} times".format(int(6-bestct),bestchar,best)

                            willRemoved = "{}ara{}".format(bestchar,best)
                            
                            backupcomp.remove(willRemoved)
                            bestct -= 1

                        worst = 10000000000
                        worstchar = ""
                        worstct = 5

                        while (worstct > 0):
                            worst = 10000000000
                            for i in backup2comp:
                                data = i.split("ara")

                                thechar = data[0]
                                timesforchar = int(data[1])

                                if timesforchar < worst:
                                    worst = timesforchar
                                    worstchar = thechar


                            lows += "\n\n{}. {} , used for {} times".format(int(6-worstct),worstchar,worst)

                            willRemoved = "{}ara{}".format(worstchar,worst)
                            backup2comp.remove(willRemoved)
                            worstct -= 1
                        comparedata = highs + lows

                        stats += comparedata

                        stats += "\n\nit took about {} seconds to compute".format(takes)                    

                    content = "{}\n\n{} passwords above{}\n\n{}".format(passwords,backuptimesinp,stats,now)

                
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
                backuptimesinp = timesinp
                
                break
            except:
                print("-----\nthis input must be a positive integer .")
                continue

            if timesinp <= 0:
                print("-----\nthis input must be a positive integer .")
                continue

        i2 = input("how many characters will your password contain? :")
        
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
        
        time1 = time()
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
                
                time2 = time()
                
                break

            print("{}\n".format(newpassword))
            passwords += "{}\n\n".format(newpassword)
            timesinp -= 1

        while 1:
            savein = input("-----\n\ndo you want to save it ? ( y / n ) :")
            detailsinp = input("-----\ndo you want more details about passwords in your save? ( y / n ) :")


            if savein == "y":
                stats=""

                filename = input("write a file name:")

                try:
                    file = open("{}.txt".format(filename),"w")
                    
                    now = datetime.now()
                    now = now.strftime("%x %X")
                    

                    if detailsinp == "y":
                        comparedata = ""
                        comparelist = list()
                        highs="\n\nmost used characters"
                        lows="\n\nless used characters"
                        takes = time2 - time1

                        
                        raw_passwords = passwords.replace("\n","")

                        
                        backupsl = seckiliste.copy()
                        for i in seckiliste:
                            if (secki.count(i) == 0):
                                backupsl.remove(i)


                        for i in backupsl:
                            microstat1 = raw_passwords.count(i)

                            singlestat = "\n\n{}  , used for {} times".format(i,microstat1)

                            stats += singlestat
                            comparelist.append("{}ara{}".format(i,microstat1))
                            
                            

                        #comparing
                        backupcomp = comparelist.copy()
                        backup2comp = comparelist.copy()

                        
                        bestchar = ""

                        
                        bestct = 5
                        while (bestct > 0):
                            best = 0
                            for i in backupcomp:
                                data = i.split("ara")
                                
                                
                                thechar = data[0]
                                timesforchar = int(data[1])

                                if (timesforchar > best):
                                    best = timesforchar
                                    bestchar = thechar


                            highs += "\n\n{}. {} , used for {} times".format(int(6-bestct),bestchar,best)

                            willRemoved = "{}ara{}".format(bestchar,best)
                            
                            backupcomp.remove(willRemoved)
                            bestct -= 1

                        worst = 10000000000
                        worstchar = ""
                        worstct = 5

                        while (worstct > 0):
                            worst = 10000000000
                            for i in backup2comp:
                                data = i.split("ara")

                                thechar = data[0]
                                timesforchar = int(data[1])

                                if timesforchar < worst:
                                    worst = timesforchar
                                    worstchar = thechar


                            lows += "\n\n{}. {} , used for {} times".format(int(6-worstct),worstchar,worst)

                            willRemoved = "{}ara{}".format(worstchar,worst)
                            backup2comp.remove(willRemoved)
                            worstct -= 1
                        comparedata = highs + lows

                        stats += comparedata

                        stats += "\n\nit took about {} seconds to compute".format(takes)

                    

                    content = "{}\n\n{} passwords above{}\n\n{}".format(passwords,backuptimesinp,stats,now)

                
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
        continue
