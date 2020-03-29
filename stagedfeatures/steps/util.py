from behave import *
from dogtail.procedural import *
import time 
import subprocess 
import re 

### BASIC ###
# this section contains basic checks, such as file io, install status, etc.

@given('the application {application} is installed')
def step_impl(context, application):
    # checks with DPKG that 'application' is installed
    # TODO
    output = subprocess.check_output(["dpkg", "--status", application], encoding='ascii')
    match = re.search(r'Status: install ok installed', output)
    if match is None:
        fail
    else:
        pass

@given('{application} is running')
def step_impl(context, application):
    #checks that the application 'application' is running
    #TODO (assert application is running)
    try:
        process = subprocess.check_output(["pidof", application])
    except subprocess.CalledProcessError:  #if an error code, it ain't running
        fail 
    pass

@given('{application} is not running')
def step_impl(context, application):
    #checks that the application 'application' is not running
    #TODO (assert application not running)
    try:
        process = subprocess.check_output(["pidof", application])
    except subprocess.CalledProcessError:  #if an error code, it ain't running
        pass 
    fail

@then('{application} is running')
def step_impl(context, application):
    # checks that the application 'application' is running
    # TODO (assert application is running)
    try:
        process = subprocess.check_output(["pidof", application])
    except subprocess.CalledProcessError:  #if an error code, it ain't running
        fail 
    
    # add PID to active applications
    process = str(process)
    process = process.replace("\n", "")
    process = process.replace("\\", "")
    temp = process.find("\'")
    temp2 = ""
    counter = temp
    for char in process[temp+1:len(process)]:
        if char == "\'":
            temp2 = counter
            break
        counter +=1
    process = process[temp+1:temp2]
    process = "mousepad: " + process

    #may need to some more magic here if we have more than one instances running

    try:
        context.activeApplications += [process]
    except:
        context.activeApplications = []
        context.activeApplications += [process]
    pass

@then('{application} is not running')
def step_impl(context, application):
    #checks that the application 'application' is not running
    #TODO (assert application not running)
    try:
        for app in context.activeApplications:
            if application in app:
                fail
    except:
	pass
    pass

@when('I open the application {application} programmatically')
def step_impl(context, application):
    # TODO, open the application programmtically using python subprocess
    # save the active application's PID in context so that it can be closed if needed
	#currently done in the 'is running section'
	#change or modifty to your preference

    # personally, I think creating a context.activeprocesses list would be good
    # if it doesn't already exist, and to append the new PID to that list
    # I think this method is the most generic, and allows testers to just iterate through
	#as meantioned before, done in the 'is running section'
	#however this may be the optimal place

    try:
        subprocess.Popen([application], shell=True)
    except:
        fail
    pass


### GUI ###
# this section contains GUI utils, such as typing arbitrary strings or pressing keys

@when('I press {key}')
def step_impl(context, key):
    # TODO emulate the user pressing the key 'key'
    # Assumes this a functional key rather than a letter
    # such as enter or alt
    time.sleep(.1)
    type("<" + key + ">")
    pass

@when('I press the key combination {keycombo}')
def step_impl(context, keycombo):
    # TODO emulate the user pressing the keycombo 'keycombo'
    # this assumes each key press is separated by a space 
    # ie I press the key combo Alt F4 will become <alt>f4 or ctrl s becomes <ctrl>s 
    # note the lack of a space in the output
    tokens = keycombo.split(" ")
    combo = ""
    for tok in tokens:
        if len(tok) > 2:                  #normal keys are 2 or less a b F1 F2 F3
            combo += "<" + tok + ">"      #otherwise they're alt ctrl enter etc.
        else:
            combo += tok

    time.sleep(.1)
    keyCombo(combo)
    
    pass

@when('I type {text}'):
def step_impl(context, text):
    # TODO emulate the user typing the text 'text'

    time.sleep(.1)
    type(text)

    pass
