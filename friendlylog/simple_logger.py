import logging
import sys

from copy import copy
from friendlylog.constants import (
        LOG_LEVEL_LIST
)
from friendlylog.utils import do_not_propagate


# Where the logs should be sent.
_STREAM = sys.stdout


class _SimpleFormatter(logging.Formatter):

    def __init__(self, *args, **kwargs):
        super(_SimpleFormatter, self).__init__(*args, **kwargs)

    @staticmethod
    def _process(msg, loglevel):
        loglevel = str(loglevel).lower()
        if loglevel not in LOG_LEVEL_LIST:
            raise RuntimeError("{} should be oneof {}.".format(
                loglevel, LOG_LEVEL_LIST))  # pragma: no cover
        return str(loglevel).upper() + ": " + str(msg)

    def format(self, record):
        record = copy(record)
        loglevel = record.levelname
        record.msg = _SimpleFormatter._process(record.msg, loglevel)
        return super(_SimpleFormatter, self).format(record)


_logger = logging.getLogger("friendlyLog.SimpleLogger" + "-" + __name__)
do_not_propagate(_logger)

_stream_handler = logging.StreamHandler(_STREAM)
_formatter = _SimpleFormatter(
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
