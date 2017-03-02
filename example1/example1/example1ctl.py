import oi
try:
    import config
except ImportError:
    import example1.config as config


def main():
    ctl = oi.CtlProgram('ctl program', config.ctl_url)
    ctl.run()

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
