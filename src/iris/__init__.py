"""Machine learning - Iris Setosa."""
from argparse import ArgumentParser
from configparser import ConfigParser
import logging
import logging.handlers
from pathlib import Path
import sys

from iris.model import run


def boot(config, logs, debug=False, verbose=False):
    """Start application."""
    LOG_FORMAT = '{asctime} {levelname:>8} - {name}({lineno}): {message}'

    fmt = logging.Formatter(fmt=LOG_FORMAT, style='{')
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG if debug else logging.INFO)

    if verbose:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(fmt)
        logger.addHandler(console_handler)

    if logs:
        file_handler = logging.handlers.RotatingFileHandler(
            filename=str(logs),
            backupCount=config.getint('logger', 'backup_file_rotation'),
            maxBytes=config.getint('logger', 'max_file_size')
        )
        file_handler.setFormatter(fmt)
        file_handler.setLevel(logging.INFO)

        logger.addHandler(file_handler)

    run()


def main(argv=None):
    """Entrypoint for service."""
    parser = ArgumentParser(description='Machine learning - Iris Setosa')

    parser.add_argument('-c', '--config', action='append', type=Path,
                        help='config file path')

    parser.add_argument('-l', '--logs', type=Path,
                        help='logs file path')

    parser.add_argument('-d', '--debug', action='store_true',
                        help='debug mode')

    parser.add_argument('-v', '--verbose', action='store_true',
                        help='verbose mode')

    args = parser.parse_args(argv or sys.argv[1:])

    config = ConfigParser()
    config.read(str(filepath) for filepath in args.config)

    boot(config, args.logs, args.debug, args.verbose)
