import logging

from colored import fg, attr
from copy import copy


class _ColoredFormatter(logging.Formatter):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def _colorize(msg, loglevel):
        DEBUG = "debug"
        INFO = "info"
        WARNING = "warning"
        ERROR = "error"
        CRITICAL = "critical"

        loglevel = str(loglevel).lower()
        assert(loglevel in [DEBUG, INFO, WARNING, ERROR, CRITICAL])
        msg = str(loglevel).upper() + ": " + msg
        if loglevel == DEBUG:
            return "{}{}{}{}{}".format(fg(14), attr(1), msg, attr(21), attr(0))  # noqa: E501
        if loglevel == INFO:
            return "{}{}{}{}{}".format(fg(46), attr(1), msg, attr(21), attr(0))  # noqa: E501
        if loglevel == WARNING:
            return "{}{}{}{}{}".format(fg(214), attr(1), msg, attr(21), attr(0))  # noqa: E501
        if loglevel == ERROR:
            return "{}{}{}{}{}".format(fg(202), attr(1), msg, attr(21), attr(0))  # noqa: E501
        assert(loglevel == CRITICAL)
        return "{}{}{}{}{}".format(fg(196), attr(1), msg, attr(21), attr(0))

    def format(self, record):
        record = copy(record)
        loglevel = record.levelname
        record.msg = _ColoredFormatter._colorize(record.msg, loglevel)
        return super().format(record)


_logger = logging.getLogger("shared.logging" + "-" + __name__)
_stream_handler = logging.StreamHandler()
_formatter = _ColoredFormatter(
        fmt='[%(asctime)s.%(msecs)03d in %(pathname)s - %(funcName)s:%(lineno)4d] %(message)s',  # noqa: E501
        datefmt='%d-%b-%y %H:%M:%S'
)
_stream_handler.setFormatter(_formatter)
_logger.addHandler(_stream_handler)
_logger.setLevel(logging.DEBUG)


# Export functions and objects.
inner_logger = _logger  # Don't use this except if you know what you are doing.
inner_stream_handler = _stream_handler  # Same thing for this object.
inner_formatter = _formatter  # Same thing for this object.


setLevel = _logger.setLevel
debug = _logger.debug
info = _logger.info
warning = _logger.warning
error = _logger.error
critical = _logger.critical