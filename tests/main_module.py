import logging
from irolog.formatter import ColoredLogFormatter

def configure_logging():
    fh = logging.StreamHandler()
    f = ColoredLogFormatter('%(asctime)s|%(levelname)s|%(message)s|',
                                  '%d/%m/%Y %H:%M:%S')
    fh.setFormatter(f)
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    root.addHandler(fh)


def main():
    configure_logging()
    logging.info('Sample message')
    logging.warning('Sample message')
    logging.debug('Sample message')
    logging.error('Sample message')
    logging.critical('Sample message')
    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        logging.exception('ZeroDivisionError: %s', e)


if __name__ == '__main__':
    main()