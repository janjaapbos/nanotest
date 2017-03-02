import oi
try:
    import config
except ImportError:
    import example1.config as config


def main():
    program = oi.Program('example1', config.ctl_url)
    program.add_command('ping', lambda: 'pong')
    program.add_command('state', lambda: program.state)
    try:
        from scheduler import setup_scheduler, scheduler
    except ImportError: 
        from example1.scheduler import setup_scheduler, scheduler
    setup_scheduler(program)
    if hasattr(config, 'register_hook'):
        config.register_hook(
            ctx=dict(
                locals=locals(),
                globals=globals(),
                program=program
            )
        )
    program.run()
    scheduler.shutdown()


if __name__ == '__main__':
    if hasattr(config, 'main_hook'):
        if not config.main_hook(
            ctx=dict(
                locals=locals(),
                globals=globals()
            )
        ):
            main()
    else:
        main()
