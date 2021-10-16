#!/usr/bin/env python
# coding: utf-8
import unittest
import sample_ctl


class TestA(unittest.TestCase):
    def test_exit_if_no_args(self):
        with self.assertRaises(SystemExit):
            sample_ctl.parse_arguments([])

    def test_x(self):
        self.assertTrue(False)
