import os,sys
print("generate-all setup\n")
username=input("enter your username in session:")

try:
    file = open("/home/{}/.bashrc".format(username),"r")
    content = file.read()
    file.close()

except:
    print('something went wrong.')
    print('try execute again this script.')
    sys.exit()

here = os.getcwd()
new = '\nalias genall="python3 {}/generateall.py"'.format(here)
newcontent = content + new

file = open("/home/{}/.bashrc".format(username),"w")
file.write(newcontent)
file.close()

print("generate-all installed successfully.")
li = input("==========\npress enter to exit")
os.remove("stp.py")
