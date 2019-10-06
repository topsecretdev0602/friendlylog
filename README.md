# FriendlyLog: Python logging made simple

![FriendlyLog logo](https://github.com/SebiSebi/friendlylog/blob/master/icons/facebook_cover_photo_2.png)

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/SebiSebi/friendlylog/blob/master/LICENSE)
[![Build Status](https://travis-ci.com/SebiSebi/friendlylog.svg?branch=master)](https://travis-ci.com/SebiSebi/friendlylog)
[![codecov](https://codecov.io/gh/SebiSebi/friendlylog/branch/master/graph/badge.svg)](https://codecov.io/gh/SebiSebi/friendlylog)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f38bee81cec2454c856ba499dfcb19e6)](https://www.codacy.com/manual/SebiSebi/friendlylog?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=SebiSebi/friendlylog&amp;utm_campaign=Badge_Grade)

FriendlyLog is a simple, colorful, user-friendly, thread-safe logger for `Python` (`2` and `3`).


Install
-------

```bash
pip install friendlylog
```


Usage
-----
TODO


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
