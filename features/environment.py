# -- FILE: features/environment.py
# -- much of this file is ripped from behave tutorials, edits to come

BEHAVE_DEBUG_ON_ERROR = False

def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")

def before_all(context):
    userdata = context.config.userdata
    setup_debug_on_error(context.config.userdata)
    
    # set the sleep multiplier from the CLI
    context.sleepmult = userdata.getfloat("SLEEPMULT", 1.0)

def after_step(context, step):
    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        # -- ENTER DEBUGGER: Zoom in on failure location.
        # NOTE: Use IPython debugger, same for pdb (basic python debugger).
        import pdb
        pdb.post_mortem(step.exc_traceback)
