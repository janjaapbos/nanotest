"""
If this config file is placed in the same directory as the
frozen binary, is will be loaded instead of the frozen config.
"""

ctl_url = 'ipc:///tmp/oi-ibeodwugtk.sock'


def main_hook(ctx=None):
    """
    Custom hook to be executed. A return value other than None
    will stop further execution.
    """
    pass
