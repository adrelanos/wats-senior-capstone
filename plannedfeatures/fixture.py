# This file heavily calls upon the fixture use tutorials on behave's site

# searches the registry for the provided fixture, routes output
def use_fixture_by_tag(tag, context, fixture_registry):
    fixture_data = fixture_registry.get(tag, None)
    if fixture_data is None:
        raise LookupError("Unknown fixture-tag: %s" % tag)

    fixture_func = fixture_data
    return use_fixture(fixture_func, context)


