from behave import given, when, then
from os import remove
import subprocess
from dogtail.procedural import *


# TODO : fix this so that it properly detects if the context.browser already exists
@given('the tor browser is running')
def step_impl(context):
    # SETUP
    if not hasattr(context,'browser'):
        context.browser = subprocess.Popen(['torbrowser'])
        focus.application("torbrowser")

# TODO : find a way to have this run after the code runs, but hopefully not every time
#
# I want this to run after the feature finishes. IE - avoid reopening the browser N times for N tests
# 
# I have been unsuccessful at utilizing fixtures, I spent hours ;_;
#
@then('the tor browser closes successfully')
def step_impl(context):
    context.browser.terminate()
    
    if context.browser.poll() is None:
        #the fixture ignored the terminate signal, kill it
        context.browser.kill()

# OTHER BIG TODO : figure out why the testfile isn't being properly removed at the beginning of each scenario
#
# these given's are run at the beginning of each step, and I'm using the practice that it puts the system in
# a known state. So, rather than just checking things as we do in @thens, in an @given, we will set it up
#
