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
    context.completedProcess=subprocess.call(["xterm", "&"], shell=True) # behave hangs here until this process returns
    pass
    
@when('we open nano')
def step_impl(context):
    # the options on this are interesting.
    # shell=True executes the command in a true subshell, with corresponding security
    # implications.
    #
    # Two major options recognized for user input into a subprocess are recognized:
    # First, there is the option of capturing stdin from the parent process,
    # and redirecting it to the stdin of the child process.
    #
    # Secondly, there is the option of forking a new process completely, focusing
    # that process, and inputing stdin directly into that.
    #
    # This implementation uses the second option.
    pass


@when('we write some in nano and save it to a file')
def step_impl(context):
    input()
    type(TEST_TEXT)
    context.oracleText = TEST_TEXT
    pass

@then('that file will have the text we wrote')
def step_impl(context):
    assert context.failed is False
