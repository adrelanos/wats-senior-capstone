from behave import *
from dogtail.procedural import *
import time 
import subprocess 
import re
import os.path

def createUser():
    rootPW = "changeme"
    command = "sudo useradd" + " " + "testuser1234"
    termAppRoot = subprocess.Popen(command.split(),stdout=subprocess.PIPE)
    time.sleep(.5 )
    type(rootPW)
    time.sleep(.4)
    keyCombo("<enter>")
    termAppRoot.wait()


def delUser():
    command = "sudo userdel" + " " + "testuser1234"
    termAppRoot = subprocess.Popen(command.split(),stdout=subprocess.PIPE)
    time.sleep(.5)
    termAppRoot.wait()


def checkUser():
##check for the user
    user = "testuser1234"
    command = "id -u " + user
    out = subprocess.Popen(command.split(),stdout=subprocess.PIPE,stderr = subprocess.STDOUT)
    out = out.communicate()
    outString = str(out)
    print(outString)
    if(re.search("no such user", outString)):
        print("no one there")
    else:
        print("thar she blows")


def main():
    createUser()
    checkUser()
    delUser()
    checkUser()

main()


