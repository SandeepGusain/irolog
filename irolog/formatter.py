import logging
import sys

PALLETTE = ['black', 'red', 'green', 'yellow',
            'blue', 'magenta', 'cyan', 'white']

COLORS = dict(zip(PALLETTE, list(range(30, 38))))

RESET_CODE = "\033[0m"
COLOR_CODE = "\033[%dm"

if sys.version_info >= (3,4):
    LOG_LEVELS = logging._levelToName
else:
    LOG_LEVELS = logging._levelNames

LOG_LEVELS = [name for priority, name in sorted(LOG_LEVELS.items(), 
                                                key = lambda x: x[0], reverse=True)]

DEFAULT_COLORS = ['magenta', 'red', 'yellow', 'green', 'blue', 'white']

COLOR_MAPPING = dict(zip(LOG_LEVELS, map(lambda x: COLOR_CODE % COLORS.get(x), DEFAULT_COLORS)))

class ColoredLogFormatter(logging.Formatter):
    def format(self, record):
        """
            Uses ANSI escape sequences to color the log messages
            based on their log level.
            For now it only supports normal text in colored mode.
            Todo: Allow custom attributes like BOLD, ITALIC etc
            to be added to the log messages as per the log level.
            Also allow passing custom colors as per existing log
            levels.
        """
        log_level = record.levelname
        color_formatted_level = f"{COLOR_MAPPING[log_level]}{log_level}"
        record.levelname = color_formatted_level
        return super().format(record) + RESET_CODE