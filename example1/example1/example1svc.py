import oi
import sys
import logging
from logging.handlers import SysLogHandler
import time
import service
from .config import ctl_url


def stop_function():
    ctl = oi.CtlProgram('ctl program', ctl_url)
    ctl.call('stop')
    ctl.client.close()

class Service(service.Service):
    def __init__(self, *args, **kwargs):
        super(Service, self).__init__(*args, **kwargs)
        self.syslog_handler = SysLogHandler(
            address=service.find_syslog(),
            facility=SysLogHandler.LOG_DAEMON
        )
        formatter = logging.Formatter(
            '%(name)s - %(levelname)s - %(message)s')
        self.syslog_handler.setFormatter(formatter)
        logging.getLogger().addHandler(self.syslog_handler)

    def run(self):
        from scheduler import setup_scheduler, scheduler
        while not self.got_sigterm():
            logging.info("Starting")
            self.program = oi.Program('example1', ctl_url)
            self.program.logger = self.logger
            self.program.add_command('ping', lambda: 'pong')
            self.program.add_command('state', lambda: self.program.state)
            setup_scheduler(self.program)
            self.program.run()
            scheduler.shutdown()
            #self.logger.info("Stopping")
            logging.info("Stopping")
        self.program.stop_function()

def main():
    import sys

    if len(sys.argv) < 2:
        sys.exit('Syntax: %s COMMAND' % sys.argv[0])

    cmd = sys.argv[1]
    sys.argv.remove(cmd)

    service = Service('example1', pid_dir='/tmp')

    if cmd == 'start':
        service.start()
    elif cmd == 'stop':
        service.stop()
        stop_function()
    elif cmd == 'restart':
        service.stop()
        stop_function()
        while service.is_running():
            time.sleep(0.1)
        service.start()
    elif cmd == 'status':
        if service.is_running():
            print "Service is running."
        else:
            print "Service is not running."
    else:
        sys.exit('Unknown command "%s".' % cmd)


if __name__ == '__main__':
    main()
