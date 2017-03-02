"""
If this config file is placed in the same directory as the
frozen binary, is will be loaded instead of the frozen config.
"""

ctl_url = 'ipc:///tmp/oi-syqvwbnjzk.sock'

import logging

def main_hook(ctx=None):
    """
    Custom hook to be executed. A return value other than None
    will stop further execution.
    """
    # logging.basicConfig(level=logging.DEBUG)
    # logging.debug('config.main_hook')

def register_hook(ctx=None):
    """
    Custom hook to extend and register commands with the program.
    ctx is a dict with locals, globals and program object
    """
    # logging.debug('config.register_hook')
    ctx['program'].add_command('hello', lambda: 'world')
