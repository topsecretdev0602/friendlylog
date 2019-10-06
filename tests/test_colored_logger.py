import io
import logging
import random
import six
import string
import unittest

from friendlylog import colored_logger as logger
from threading import Thread


# Tests cannot be executed in parallel due to the hack in the setUp method.
class TestColoredLogger(unittest.TestCase):

    def setUp(self):
        # Remove handler that outputs to STDERR.
        logger.inner_logger.removeHandler(logger.inner_stream_handler)

        # Add handler that outputs to StringIO.
        if six.PY2:
            self.log_capture = io.BytesIO()
        else:
            self.log_capture = io.StringIO()
        handler = logging.StreamHandler(self.log_capture)
        handler.setFormatter(logger.inner_formatter)
        logger.inner_logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)

    def tearDown(self):
        pass

    def last_line(self):
        log = self.log_capture.getvalue().splitlines()
        if len(log) == 0:
            return []
        return log[-1]

    def last_n_lines(self, n):
        log = self.log_capture.getvalue().splitlines()
        return log[-n:]

    def num_lines(self):
        return len(self.log_capture.getvalue().splitlines())

    def test_level_is_logged(self):
        logger.debug("message 1")
        self.assertIn("DEBUG", self.last_line())
        logger.info("message 2")
        self.assertIn("INFO", self.last_line())
        logger.warning("message 3")
        self.assertIn("WARNING", self.last_line())
        logger.error("message 4")
        self.assertIn("ERROR", self.last_line())
        logger.critical("message 5")
        self.assertIn("CRITICAL", self.last_line())

    def test_function_is_logged(self):
        logger.debug("message 1")
        self.assertIn(" test_function_is_logged", self.last_line())
        logger.info("message 2")
        self.assertIn(" test_function_is_logged", self.last_line())
        logger.warning("message 3")
        self.assertIn(" test_function_is_logged", self.last_line())
        logger.error("message 4")
        self.assertIn(" test_function_is_logged", self.last_line())
        logger.critical("message 5")
        self.assertIn(" test_function_is_logged", self.last_line())

    def test_filepath_is_logged(self):
        logger.debug("message 1")
        self.assertIn("test_colored_logger.py", self.last_line())
        logger.info("message 2")
        self.assertIn("test_colored_logger.py", self.last_line())
        logger.warning("message 3")
        self.assertIn("test_colored_logger.py", self.last_line())
        logger.error("message 4")
        self.assertIn("test_colored_logger.py", self.last_line())
        logger.critical("message 5")
        self.assertIn("test_colored_logger.py", self.last_line())

    def test_message_is_logged(self):
        logger.debug("message 1")
        self.assertIn("message 1", self.last_line())
        logger.info("message 2")
        self.assertIn("message 2", self.last_line())
        logger.warning("message 3")
        self.assertIn("message 3", self.last_line())
        logger.error("message 4")
        self.assertIn("message 4", self.last_line())
        logger.critical("message 5")
        self.assertIn("message 5", self.last_line())

    def test_levels(self):
        def log_all():
            logger.debug("message 1")
            logger.info("message 2")
            logger.warning("message 3")
            logger.error("message 4")
            logger.critical("message 5")

        def test_last(expected):
            self.assertIsInstance(expected, list)
            last_n = self.last_n_lines(len(expected))
            self.assertEqual(len(last_n), len(expected))
            for output, exp in zip(last_n, expected):
                self.assertIn(exp, output)

        expected_logs = [
                "DEBUG: message 1",
                "INFO: message 2",
                "WARNING: message 3",
                "ERROR: message 4",
                "CRITICAL: message 5"
        ]

        # Debug.
        logger.setLevel(logging.DEBUG)
        log_all()
        self.assertEqual(self.num_lines(), 5)
        test_last(expected_logs)

        # Info.
        logger.setLevel(logging.INFO)
        log_all()
        self.assertEqual(self.num_lines(), 5 + 4)
        test_last(expected_logs[1:])

        # Warning.
        logger.setLevel(logging.WARNING)
        log_all()
        self.assertEqual(self.num_lines(), 5 + 4 + 3)
        test_last(expected_logs[2:])

        # Error.
        logger.setLevel(logging.ERROR)
        log_all()
        self.assertEqual(self.num_lines(), 5 + 4 + 3 + 2)
        test_last(expected_logs[3:])

        # Critical.
        logger.setLevel(logging.CRITICAL)
        log_all()
        self.assertEqual(self.num_lines(), 5 + 4 + 3 + 2 + 1)
        test_last(expected_logs[4:])

    def test_multi_threaded_is_ok(self):
        num_threads = 75

        def log_all(msg):
            for _ in range(0, 11):
                logger.debug(msg)
                logger.info(msg)
                logger.warning(msg)
                logger.error(msg)
                logger.critical(msg)

        # Generate a random long message for each thread.
        messages = []
        for _ in range(0, num_threads):
            msg = []
            length = random.randint(500, 2000)
            alphabet = string.punctuation + string.ascii_letters + string.digits  # noqa: E501
            for i in range(0, length):
                msg.append(random.choice(list(alphabet)))
            messages.append(''.join(msg))
            self.assertNotIn('\n', messages[-1])
        self.assertEqual(len(messages), num_threads)

        # Create, start and stop threads.
        threads = []
        for i in range(0, num_threads):
            threads.append(Thread(target=log_all, args=(messages[i],)))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        # Check the output.
        self.assertEqual(self.num_lines(), num_threads * 11 * 5)
        log = self.log_capture.getvalue().splitlines()
        for line in log:
            self.assertEqual(line[0], '[')
            self.assertGreater(len(line), 500)

        # Counts in how many elements of @array, @substr can be found.
        def count_in(array, substr):
            cnt = 0
            for el in array:
                if substr in el:
                    cnt += 1
            return cnt

        for msg in messages:
            self.assertEqual(count_in(log, msg), 11 * 5)
            for level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
                self.assertEqual(count_in(log, level + ": " + msg), 11)

    def test_terminal_logging(self):
        logger.info("message to terminal device")
        self.assertIn("INFO", self.last_line())
        # 118 (the length without colors) + 4 coloring characters.
        self.assertGreaterEqual(len(self.last_line()), 118 + 4)


if __name__ == '__main__':
    unittest.main()
