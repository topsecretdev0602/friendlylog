import os
import sys

try:
    import friendlylog
except ModuleNotFoundError as ex:
    # Add the parent directory to the list of strings that specifies the
    # search path for modules.
    sys.path.insert(0, os.path.abspath(os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        "../"
    )))
