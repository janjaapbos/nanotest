import oi
from scheduler import setup_scheduler, scheduler
import logging
from .config import ctl_url


def main():
    program = oi.Program('example1', ctl_url)
    program.add_command('ping', lambda: 'pong')
    program.add_command('state', lambda: program.state)
    setup_scheduler(program)
    program.run()
    scheduler.shutdown()

if __name__ == '__main__':
    main()
