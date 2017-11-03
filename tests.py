#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import logging
import unittest

from readable_log_formatter import ReadableFormatter

log = logging.getLogger()
log.setLevel(logging.NOTSET)
hndl = logging.StreamHandler()
hndl.setFormatter(ReadableFormatter())
log.addHandler(hndl)


class ReadableLogTests(unittest.TestCase):
    """
    These tests are just to make sure nothing crashes. Visual confirmation
    can be done with the console output.
    """
    def setUp(self):
        # start with a newline so the test output doesn't mess with alignment
        print("")

    def test_levels(self):
        for level in ['debug', 'info', 'warning', 'error', 'critical']:
            getattr(log, level)('this is a %s log message', level)

    def test_extras(self):
        log.info('this has some extras', extra={'THING1': 'value',
                                                'THING2': object,
                                                'THING3': 20,
                                                4: 'integer keys too 😲'})

    def test_traceback(self):
        try:
            1/0
        except ZeroDivisionError:
            log.exception("You can't divide by zero!")

    def test_unicode(self):
        log.debug('Thís has some unicode: ¯\_(ツ)_/¯')

    def test_multiline(self):
        log.warning("This\nis\na\nfew\nlines.")


class ClassSetupTests(unittest.TestCase):
    def test_args(self):
        """Verify the hard-coding of the format works"""
        arg = ReadableFormatter('no')
        self.assertEqual(arg._fmt, ReadableFormatter.fmt.format(
            ReadableFormatter.indent, ReadableFormatter.separator))
        kwarg = ReadableFormatter(fmt='no')
        self.assertEqual(kwarg._fmt, ReadableFormatter.fmt.format(
            ReadableFormatter.indent, ReadableFormatter.separator))


if __name__ == '__main__':
    unittest.main()
