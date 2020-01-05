"""
pylab.entry_points.py
~~~~~~~~~~~~~~~~~~~~~~

This module contains the entry-point functions for the pylab module,
that are referenced in setup.py.
"""

from sys import argv


def main() -> None:
    """Main package entry point.

    Delegates to other functions based on user input.
    """

    try:
        user_cmd = argv[1]
        if user_cmd == 'install':
            pass
        else:
            RuntimeError('please supply a command for pylab - e.g. install.')
    except IndexError:
        RuntimeError('please supply a command for pylab - e.g. install.')
    return None


def install_template_from_github() -> None:
    return None
