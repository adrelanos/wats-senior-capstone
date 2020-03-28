from behave import *
from dogtail.procedural import *

### BASIC ###
# this section contains basic checks, such as file io, install status, etc.

@given('the application {application} is installed')
def step_impl(context, application):
    # checks with DPKG that 'application' is installed
    # TODO
    pass

@given('{application} is running')
def step_impl(context, application):
    #checks that the application 'application' is running
    #TODO (assert application is running)
    pass

@given('{application} is not running')
def step_impl(context, application):
    #checks that the application 'application' is not running
    #TODO (assert application not running)
    pass

@then('{application} is running')
def step_impl(context, application):
    # checks that the application 'application' is running
    # TODO (assert application is running)

    # add PID to active applications
    pass

@then('{application} is not running')
def step_impl(context, application):
    #checks that the application 'application' is not running
    #TODO (assert application not running)
    pass

@when('I open the application {application} programmatically')
def step_impl(context, application):
    # TODO, open the application programmtically using python subprocess
    # save the active application's PID in context so that it can be closed if needed

    # personally, I think creating a context.activeprocesses list would be good
    # if it doesn't already exist, and to append the new PID to that list
    # I think this method is the most generic, and allows testers to just iterate through
    
    pass


### GUI ###
# this section contains GUI utils, such as typing arbitrary strings or pressing keys

@when('I press {key}')
def step_impl(context, key):
    # TODO emulate the user pressing the key 'key'
    pass

@when('I press the key combination {keycombo}')
def step_impl(context, keycombo):
    # TODO emulate the user pressing the keycombo 'keycombo'
    pass

@when('I type {text}'):
def step_impl(context, text):
    # TODO emulate the user typing the text 'text'
    pass
