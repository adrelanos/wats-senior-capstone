# This file heavily calls upon the fixture use tutorials on behave's site
from behave import use_fixture
from behave.fixture import fixture, use_fixture_by_tag
import subprocess

#-- FIXTURE GENERATOR FUNCTIONS -- #
@fixture
def browser_tor(context, timeout=30, **kwargs):
    # SETUP-FIXTURE : called in the respective context layer (see behave lifecycle)
    context.browser = subprocess.Popen(torbrowser)
    yield context.browser

    # CLEANUP-FIXTURE : same as above, when these are called depends on the fixture scope
    context.browser.terminate()

    if context.browser.poll() is None:
        #the fixture ignored the terminate signal, kill it
        context.browser.kill()


# -- SIMPLE REGISTRY SCHEMA : fixture_func # add fixtures here as needed
fixture_registry = {
    "fixture.browser.tor": browser_tor,
}


# this fxn processes all tags used by wats, routing the calls as necessary
def before_tag(context_tag):
    if tag.startswith("fixture."):
        return use_fixture_by_tag(tag, context, fixture_registry)


