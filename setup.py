import sys
import os

username = input("GenerateAll\nenter your username in session:")
try:
	file = open("/home/{}/.bashrc".format(username),"r")
	content = file.read()
	file.close()
except:
	print("something went wrong.")
	sys.exit()

here = os.getcwd()
new='\nalias genall="cd {} && python3 generateall.py"'.format(here)

newcontent = content + new

file = open("/home/{}/.bashrc".format(username),"w")
file.write(newcontent)
file.close()

print("GenerateAll installed successfully.\njust write genall in terminal to use.\nstay safe")