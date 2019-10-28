# Do not pass events logged to this logger to the handlers of higher level
# (ancestor) loggers.
# Fixes: https://github.com/abseil/abseil-py/issues/99
def do_not_propagate(logger):
    logger.propagate = False
