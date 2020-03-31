from behave import *
from dogtail.procedural import *
import time 
import subprocess 
import re
import os.path

### BASIC ###
# this section contains basic checks, such as file io, install status, etc.

TIME_CONSTANT = 3

@given('the application "{application}" is installed')
def step_impl(context, application):
    # checks with DPKG that 'application' is installed
    # TODO
    output = subprocess.check_output(["dpkg", "--status", application], encoding='ascii')
    match = re.search(r'Status: install ok installed', output)
    if match is None:
        fail
    else:
        pass

@given('"{application}" is running')
def step_impl(context, application):
    #checks that the application 'application' is running
    #TODO (assert application is running)
    try:
        process = subprocess.check_output(["pidof", application])
    except subprocess.CalledProcessError:  #if an error code, it ain't running
        fail 
    pass

@given('"{application}" is not running')
def step_impl(context, application):
    #checks that the application 'application' is not running
    #TODO (assert application not running)
    try:
        process = subprocess.check_output(["pidof", application])
    except subprocess.CalledProcessError:  #if an error code, it ain't running
        pass 
    fail

@given('the file "{filepath}" does not exist')
def step_impl(context, filepath):
    #simply checks if the file at filepath exists
    if not os.path.isfile(filepath):
        pass
    else:
        fail

@given('the test file location is at "{filepath}"')
def step_impl(context, filepath):
    #simply set the context field appropriately
    context.testfilepath = filepath # (context.filepath is reserved, apparently)
    pass

@given('the test file does not exist')
def step_impl(context):
    try:
	os.remove(context.testfilepath)
	pass
    except:
	pass

@then('the file "{filepath}" exists')
def step_impl(context, filepath):
    if os.path.isfile(filepath):
        pass
    else:
        fail

@then('that file contains the "{oracletext}"')
def step_impl(context):
    with open(context.testfilepath, 'r') as textfile:
        text = textfile.read()
        textfile.close()
    if (re.search(oracletext)) is None:
        fail
    else:
        pass

@then('"{application}" is running')
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

@then('"{application}" is not running')
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
        

@when('I open the application "{application}" programmatically')
def step_impl(context, application):
    # TODO, open the application programmtically using python subprocess
    # save the active application's PID in context so that it can be closed if needed
	#currently done in the 'is running section'
	#change or modifty to your preference


    try:
        ## I also think we should have a subprocesses list passed around
        context.activesubprocesses.append(subprocess.Popen([application], shell=True))
    except:
        fail
    pass


### GUI ###
# this section contains GUI utils, such as typing arbitrary strings or pressing keys

@when('I press "{key}"')
def step_impl(context, key):
    # TODO emulate the user pressing the key 'key'
    # Assumes this a functional key rather than a letter
    # such as enter or alt
    time.sleep(TIME_CONSTANT)
    type("<" + key + ">")
    pass

@when('I press the key combination "{keycombo}"')
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

    time.sleep(TIME_CONSTANT)
    keyCombo(combo)
    
    pass

@when('I type "{text}"')
def step_impl(context, text):
    # TODO emulate the user typing the text 'text'

    time.sleep(TIME_CONSTANT)
    type(text)

    pass
