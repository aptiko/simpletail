# coding=utf8

import os
import sys
from unittest import TestCase

from simpletail import ropen


class RopenTestCase(TestCase):
    def test_simple(self):
        filename = os.path.join("tests", "data", "simple.txt")
        with ropen(filename) as f:
            self.assertEqual(f.next(), "Line 7\n")
            self.assertEqual(f.next(), "Line 6\n")
            self.assertEqual(f.next(), "Line 5\n")
            self.assertEqual(f.next(), "Line 4\n")
            self.assertEqual(f.next(), "Line 3\n")
            self.assertEqual(f.next(), "Line 2\n")
            self.assertEqual(f.next(), "Line 1\n")
            self.assertRaises(StopIteration, f.next)

    def test_simple_readline(self):
        filename = os.path.join("tests", "data", "simple.txt")
        with ropen(filename) as f:
            self.assertEqual(f.readline(), "Line 7\n")
            self.assertEqual(f.readline(), "Line 6\n")
            self.assertEqual(f.readline(), "Line 5\n")
            self.assertEqual(f.readline(), "Line 4\n")
            self.assertEqual(f.readline(), "Line 3\n")
            self.assertEqual(f.readline(), "Line 2\n")
            self.assertEqual(f.readline(), "Line 1\n")
            self.assertEqual(f.readline(), "")
            self.assertEqual(f.readline(), "")
            self.assertEqual(f.readline(), "")

    def test_small_buffer(self):
        filename = os.path.join("tests", "data", "simple.txt")
        with ropen(filename, bufsize=3) as f:
            self.assertEqual(f.next(), "Line 7\n")
            self.assertEqual(f.next(), "Line 6\n")
            self.assertEqual(f.next(), "Line 5\n")
            self.assertEqual(f.next(), "Line 4\n")
            self.assertEqual(f.next(), "Line 3\n")
            self.assertEqual(f.next(), "Line 2\n")
            self.assertEqual(f.next(), "Line 1\n")
            self.assertRaises(StopIteration, f.next)

    def _check_utf(self, s, length, end):
        self.assertEqual(len(s), length)
        self.assertTrue(s.endswith(end))

    def test_utf_noeol(self):
        filename = os.path.join("tests", "data", "utf_noeol.txt")
        with ropen(filename, encoding="utf8") as f:
            if sys.version_info[0] <= 2:
                self._check_utf(f.next(), 8, " 7")
                self._check_utf(f.next(), 9, " 6\n")
                self._check_utf(f.next(), 9, " 5\n")
                self._check_utf(f.next(), 9, " 4\n")
                self._check_utf(f.next(), 9, " 3\n")
                self._check_utf(f.next(), 9, " 2\n")
                self._check_utf(f.next(), 9, " 1\n")
            else:
                self.assertEqual(f.next(), "Γραμμή 7")
                self.assertEqual(f.next(), "Γραμμή 6\n")
                self.assertEqual(f.next(), "Γραμμή 5\n")
                self.assertEqual(f.next(), "Γραμμή 4\n")
                self.assertEqual(f.next(), "Γραμμή 3\n")
                self.assertEqual(f.next(), "Γραμμή 2\n")
                self.assertEqual(f.next(), "Γραμμή 1\n")
            self.assertRaises(StopIteration, f.next)

    def test_utf_noeol_small_buffer(self):
        filename = os.path.join("tests", "data", "utf_noeol.txt")
        with ropen(filename, encoding="utf8", bufsize=3) as f:
            if sys.version_info[0] <= 2:
                self._check_utf(f.next(), 8, " 7")
                self._check_utf(f.next(), 9, " 6\n")
                self._check_utf(f.next(), 9, " 5\n")
                self._check_utf(f.next(), 9, " 4\n")
                self._check_utf(f.next(), 9, " 3\n")
                self._check_utf(f.next(), 9, " 2\n")
                self._check_utf(f.next(), 9, " 1\n")
            else:
                self.assertEqual(f.next(), "Γραμμή 7")
                self.assertEqual(f.next(), "Γραμμή 6\n")
                self.assertEqual(f.next(), "Γραμμή 5\n")
                self.assertEqual(f.next(), "Γραμμή 4\n")
                self.assertEqual(f.next(), "Γραμμή 3\n")
                self.assertEqual(f.next(), "Γραμμή 2\n")
                self.assertEqual(f.next(), "Γραμμή 1\n")
            self.assertRaises(StopIteration, f.next)
