import inspect
from pprint import pprint


def introspection_info(obj):
    info = {}

    type_ = type(obj).__name__

    attributes = []
    methods = []
    for n in dir(obj):
        if not callable(getattr(obj, n)):
            attributes.append(n)
        else:
            methods.append(n)

    module = inspect.getmodule(introspection_info)

    info['type'] = type_
    info['attributes'] = attributes
    info['methods'] = methods
    info['module'] = module

    return pprint(info)



number_info = introspection_info(42)