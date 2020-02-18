from behave import *
#from dogtail import rawinput
## issue: python3-dogtail is only in debian-testing
## this distro is running debian stable
## there is no python2.7 behave, so we're stuck in python3
import subprocess


@given('we have nano installed')
def step_impl(context):
    pass

@when('we open nano')
def step_impl(context):
    subprocess.call("nano")

@when('we write hello world')
def step_impl(context):
    #dogtail.rawinput.typeText("hello world")

@when('we quit and save the file')
def step_impl(context):
    #dogtail.rawinput.keyCombo('<Control>x')
    #dogtail.rawinput.pressKey('y')

@then('the file will exist')
def step_impl(context):
    assert context.failed is False
