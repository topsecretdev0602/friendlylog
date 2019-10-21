# FriendlyLog: Python logging made simple

![FriendlyLog logo](https://github.com/SebiSebi/friendlylog/blob/master/icons/facebook_cover_photo_2.png)

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/SebiSebi/friendlylog/blob/master/LICENSE)
[![Build Status](https://travis-ci.com/SebiSebi/friendlylog.svg?branch=master)](https://travis-ci.com/SebiSebi/friendlylog)
[![codecov](https://codecov.io/gh/SebiSebi/friendlylog/branch/master/graph/badge.svg)](https://codecov.io/gh/SebiSebi/friendlylog)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/803817c9fe964b8b8b591112ab41e913)](https://www.codacy.com/manual/SebiSebi/friendlylog?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=SebiSebi/friendlylog&amp;utm_campaign=Badge_Grade)

[![Python Versions](https://img.shields.io/badge/python-2.7%20%7C%203.4%20%7C%203.5%20%7C%203.6%20%7C%203.7-blue)](https://pypi.org/project/friendlylog/)
[![Downloads](https://pepy.tech/badge/friendlylog/month)](https://pypistats.org/packages/friendlylog)

FriendlyLog is a simple, colorful, user-friendly, thread-safe logger for `Python` (`2` and `3`).

<img src="https://github.com/SebiSebi/friendlylog/blob/master/images/tutorial.gif">

Install
-------

```bash
pip install friendlylog
```


Usage
-----

1. Simple Logger

```python
import logging

from friendlylog import simple_logger as log

# Anything above or including DEBUG will be logged.
log.setLevel(logging.DEBUG) 

log.debug("debug message")
log.info("info message")
log.warning("warning message")
log.error("error message")
log.critical("critical message")
```

Will result in the following logs (`test.py` is the name of the file):
```
[07-Oct-19 11:06:06.107 in test.py - <module>:   3] DEBUG: debug message
[07-Oct-19 11:06:06.107 in test.py - <module>:   4] INFO: info message
[07-Oct-19 11:06:06.107 in test.py - <module>:   5] WARNING: warning message
[07-Oct-19 11:06:06.107 in test.py - <module>:   6] ERROR: error message
[07-Oct-19 11:06:06.107 in test.py - <module>:   7] CRITICAL: critical message
```

2. Colored Logger

```python
import logging

from friendlylog import colored_logger as log

# Anything above or including DEBUG will be logged.
log.setLevel(logging.DEBUG) 

log.debug("debug message")
log.info("info message")
log.warning("warning message")
log.error("error message")
log.critical("critical message")
```

Will result in the following logs (`test.py` is the name of the file):

<img src="https://github.com/SebiSebi/friendlylog/blob/master/images/colored_log.png" max-width="715" height="86"/>


Contributing
------------

1. Write the code for a new logger under `friendlylog`. It should export the following methods:
   	* `setLevel(level)`
	* `debug(msg: string)`
 	* `info(msg: string)`
 	* `warning(msg: string)`
  	* `error(msg: string)`
  	* `critical(msg: string)`
2. Write unit tests with `>92%` coverage under `tests`. You can run the tests locally
using this command: `bash run_tests.sh`. Make sure the new logger is thread-safe. Also,
add a unit test that checks thread-safety;
3. Submit a pull-request with your changes.
