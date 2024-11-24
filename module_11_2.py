import inspect


def introspection_info(obj):
    return f'{type(obj)}\n{dir(obj)}\n{inspect.getmodule(introspection_info)}'


info = introspection_info(['info', 'инфо'])
print(info)