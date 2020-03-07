from behave import *
from dogtail.procedural import *
import subprocess
from subprocess import Popen, PIPE, STDOUT
import os
import tempfile

TEST_TEXT = "Hello world!"

@given('we have nano installed')
def step_impl(context):
    pass

@when('we open mousepad')
def step_impl(context):
    #
    # Two major options recognized for user input into a subprocess are recognized:
    # First, there is the option of capturing stdin from the parent process,
    # and redirecting it to the stdin of the child process.
    #
    # Secondly, there is the option of forking a new process completely, focusing
    # that process, and inputing stdin directly into that.
    #
    # this implementation uses the second option with Popen being a lowlevel
    # interface, accessed by the subprocess.run. Care must be taken to ensure
    # the created process actually exits.
    #
    
    mousepadproc = subprocess.Popen(["mousepad", "&"])
    context.testProcess=mousepadproc
    pass

@when('we write hello world')
def step_impl(context):
    focus.application("mousepad")
    type(TEST_TEXT)
    pass

@when('we quit and save the file')
def step_impl(context):
    context.dirname=tempfile.mkdtemp()
    context.filename = os.path.join(context.dirname, "hello.txt")
    keyCombo("<ctrl>s")
    type(context.filename)
    focus.widget("Save As")
    click.button("Save")

    # wait a little for it to finish
    try:
        context.wait(5)

    except subprocess.TimeoutExpired:
     # kills it, -9 style if it takes too long
        context.testProcess.kill()
    pass

@then('the file will exist')
def step_impl(context):
    # checks for the file
    if os.path.isfile(context.filename):
        pass
    else:
        # TODO (for John) throw an error
        pass

@then('the returncode was zero')
def step_impl(context):
    #cleans up
    os.remove(context.filename)
    os.rmdir(context.filename)
    context.completedProcess.check_returncode() #throws error if nonzero
