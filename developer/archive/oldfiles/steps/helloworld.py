from behave import *
from dogtail.procedural import *
import subprocess
from subprocess import Popen, PIPE, STDOUT
import os
import tempfile
import time

@given('I have {application} installed')
def step_impl(context, application):
    # TODO, remove
    pass

@when('I open the application {application} programmatically')
def step_impl(context, application):

    # open application as a separately managed process
    mousepadproc = subprocess.Popen([application])
    context.testProcess=mousepadproc
    focus.application("mousepad")
    pass

@when('I type {text}')
def step_impl(context, text):
    time.sleep(.5)
    type(text)
    pass

@when('I quit and save the file')
def step_impl(context):
    context.dirname=tempfile.mkdtemp()
    context.filename = os.path.join(context.dirname, "hello.txt")
    keyCombo("<ctrl>s")
    time.sleep(.1)
    type(context.filename)
    time.sleep(.1)
    keyCombo("<enter>")
    time.sleep(.1)
    keyCombo("<ctrl>q")

    # wait a little for it to finish
    #try:
    #   context.wait(5)

    #except subprocess.TimeoutExpired:
    #  kills it, -9 style if it takes too long
    #    context.testProcess.kill()
    pass

@then('the file will exist')
def step_impl(context):
    # checks for the file
    assert os.path.isfile(context.filename)
    pass

@then('the returncode was zero')
def step_impl(context):
    #cleans up
    os.remove(context.filename)
    os.rmdir(context.filename)
    context.completedProcess.check_returncode() #throws error if nonzero
