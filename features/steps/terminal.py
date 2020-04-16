from behave import *
from dogtail.procedural import *
import time 
import subprocess 
import re
import os.path


#@given('"{application}" is running')
#def step_impl(context, application):


@when('I run the command "{cmd}" with the options "{params}" programmatically')
def step_impl(context, cmd, params):
    #executes the command with the parameters
    command = cmd + " " + params
    context.termApp = subprocess.Popen(command.split(),stdout=subprocess.PIPE)
    context.termApp.wait()
    time.sleep(.5 * context.sleepmult)
    pass


#todo use the CLI output to verfiy possible issues
@then('there is CLI output')
def step_impl(context):
    output = context.termApp.communicate

    pass

#might be an unneeded implementation here
#could use the util with the @when keyCombo
#but there isn't a @then currently
#possible change for todo
#another thing to note is that the GUI check
#window may not always comeplete as quickly
#as the console portion and I'm unsure how 
#the repsonsiveness will work.
#REQUIRES FURTHER TESTING
@then('the GUI window appears and is dismissed')
def step_impl(context):
    time.sleep(.5 * context.sleepmult)
    keyCombo("<enter>")
