from behave import *
from dogtail.procedural import *
## issue: python3-dogtail is only in debian-testing
## this distro is running debian stable
## there is no python2.7 behave, so we're stuck in python3
import subprocess
TEST_TEXT = "Hello world!"

@given('we are testing nano and xterm')
def step_impl(context):
    context.testApplications = ["nano","xterm"]
    
@given('and the application(s) to be tested are installed')
def step_impl(context):
    # execute dpkg on each application to check if it's installed
    for each application in context.testApplications :
        # execute, capture output and error
        context.myCompletedProcess=subprocess.call(["dpkg", "-l", application],stdout=PIPE,stderr=PIPE, encoding=U)
        context.myCompletedProcess.check_returncode() #throws error if nonzero
        context.myCompletedProcess.
    pass

@when('we open a new xterm terminal')
def step_impl(context):
    context.completedProcess=subprocess.call(["xterm", "&"])
    
    
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


@when('we write hello world')
def step_impl(context):
    input()
    type(TEST_TEXT)
    context.oracleText = TEST_TEXT
    pass

@when('we quit and save the file')
def step_impl(context):
    keyCombo('<Control>x')
    type("y")
    pass

@then('the file will exist')
def step_impl(context):
    assert context.failed is False

@then('the returncode was zero')
def step_impl(context):
    context.completedProcess.check_returncode() #throws error if nonzero
