import importlib
import sys


def execute(script_param):
    module, name = script_param.split(':')
    exec_object = getattr(importlib.import_module(module), name)
    exec_object()


if __name__ == '__main__':
    args = sys.argv[1]
    execute(script_param=args)
