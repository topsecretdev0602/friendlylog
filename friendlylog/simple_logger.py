import logging
import sys

from copy import copy


# Where the logs should be sent.
_STREAM = sys.stdout

class _SimpleFormatter(logging.Formatter):

    def __init__(self, *args, **kwargs):
        super(_SimpleFormatter, self).__init__(*args, **kwargs)

    @staticmethod
    def _process(msg, loglevel):
        DEBUG = "debug"
        INFO = "info"
        WARNING = "warning"
        ERROR = "error"
        CRITICAL = "critical"

        loglevel = str(loglevel).lower()
        if loglevel not in [DEBUG, INFO, WARNING, ERROR, CRITICAL]:
            raise RuntimeError("{} should be oneof {}.".format(
                loglevel, [DEBUG, INFO, WARNING, ERROR, CRITICAL]))  # pragma: no cover
        msg = str(loglevel).upper() + ": " + msg

        return msg

    def format(self, record):
        record = copy(record)
        loglevel = record.levelname
        record.msg = _SimpleFormatter._process(record.msg, loglevel)
        return super(_SimpleFormatter, self).format(record)


_logger = logging.getLogger("friendlyLog.SimpleLogger" + "-" + __name__)
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
