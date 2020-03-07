from behave import *
from dogtail.procedural import *
import re
import subprocess

##
# file name: terminalapplications.py
# 
# description: this feature file is intended to test basic terminal application functionality
#     more complex functionality should be segregated into it's own feature file
##

DEBUG_MODE = True

TEST_TEXT = "Hello world!"
    
@given('we are testing nano and xterm')
def step_impl(context):
    # applications placed here can be increased, just don't spell it wrong
    context.testApplications = ["nano","xterm"]
    
@given('the application(s) to be tested are installed')
def step_impl(context):
    # execute dpkg on each application to check if it's installed
    
    for application in context.testApplications :
        # execute, capture output and error
        output = subprocess.check_output(["dpkg", "--status", application], encoding='ascii')
        match=re.search(r'Status: install ok installed', output)

        #no output found, throw an error
        if match is None:
            print(output)
            raise RuntimeError('Success message not found in dpkg status output!')
        else:
            print("for program: %s dpkg found status %s" % (application, match.string)) if (DEBUG_MODE) else print("")            
    pass

@when('we open a new xterm terminal')
def step_impl(context):

    #
    # TODO: use similar Popen structure as in helloworld.py to avoid process hang,
    # handle exit scenarios properly
    #
    # open in a separate terminal window
    #
    context.completedProcess=subprocess.call(["xterm", "&"], shell=True) # behave hangs here until this process returns
    pass
    
@when('we open nano')
def step_impl(context):
    #
    # TODO: focus xterm window, type nano into that window, press enter
    #
    # Don't worry too much about handling errors, the test simply fails if an exception throws
    # since xterm is not used by default on this machine, it should be unique
    # HOWEVER we will need to test the xfce terminal too, which presents problems
    #
    
    pass


@when('we write some in nano and save it to a file')
def step_impl(context):
    #
    # TODO: grab focus of nano running in xterm  not already grabbed
    # type into nano
    # send <ctrl>+x and then y to save and quit, test of course manually
    #
    # ALSO, these will need to be written into behave, since they don't work I haven't written them in
    # simply add "When we write some in nano and save it to a file" - spelling matters
    # if you see the word "And" in behave, it's just copying the last line's first word, more readable,
    # you can do that as well
    #
    # when should be test actions, then should be the oracle section
    #
    
    type(TEST_TEXT)
    context.oracleText = TEST_TEXT
    pass

@then('that file will have the text we wrote')
def step_impl(context):
    #
    # TODO: the whole thing, I can do this if you don't do it, just
    # read the file from python, and check against - context.test_text, or whatever you use
    # the context object is passed from step to step, so use it to hold variables, objects, etc
    #
    
    assert context.failed is False
