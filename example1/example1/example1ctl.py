import oi
from .config import ctl_url


def main():
    ctl = oi.CtlProgram('ctl program', ctl_url)
    ctl.run()

if __name__ == '__main__':
    main()
