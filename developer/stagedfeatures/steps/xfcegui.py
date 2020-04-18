from behave import *
from dogtail.procedural import *

@given('the xfce gui testing hotkeys are configured')
def step_impl(context):

    # TODO verify that the file stored at
    #
    #   /etc/xdg/xfce4/xfconf/xfce-perchannel-xml
    #
    # has the right hotkeys.

    ### another implementation would be to parse the file for the proper hotkeys (xml parser library?)
    # and then just use what is already written. it wouldn't work if the hotkey is unbound though

    pass

@when('I press the xfcegui hotkey {hotkey}')
def step_impl(context, hotkey):

    # TODO find the hotkey at 'hotkey', press the keycombo
    pass

@given('{application} is the focused window')
def step_impl(context, application):

    #TODO assert that application 'application' is in focus
    pass
