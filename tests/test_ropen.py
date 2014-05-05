# coding=utf8

import os
from unittest import TestCase

import six

from simpletail import ropen


class RopenTestCase(TestCase):

    def test_simple(self):
        filename = os.path.join('tests', 'data', 'simple.txt')
        with ropen(filename) as f:
            self.assertEqual(f.next(), six.u('Line 7\n'))
            self.assertEqual(f.next(), six.u('Line 6\n'))
            self.assertEqual(f.next(), six.u('Line 5\n'))
            self.assertEqual(f.next(), six.u('Line 4\n'))
            self.assertEqual(f.next(), six.u('Line 3\n'))
            self.assertEqual(f.next(), six.u('Line 2\n'))
            self.assertEqual(f.next(), six.u('Line 1\n'))
            self.assertRaises(StopIteration, f.next)

    def test_small_buffer(self):
        filename = os.path.join('tests', 'data', 'simple.txt')
        with ropen(filename, bufsize=3) as f:
            self.assertEqual(f.next(), six.u('Line 7\n'))
            self.assertEqual(f.next(), six.u('Line 6\n'))
            self.assertEqual(f.next(), six.u('Line 5\n'))
            self.assertEqual(f.next(), six.u('Line 4\n'))
            self.assertEqual(f.next(), six.u('Line 3\n'))
            self.assertEqual(f.next(), six.u('Line 2\n'))
            self.assertEqual(f.next(), six.u('Line 1\n'))
            self.assertRaises(StopIteration, f.next)

    def _check_utf(self, s, length, end):
        self.assertEqual(len(s), length)
        self.assertTrue(s.endswith(end))

    def test_utf_noeol(self):
        filename = os.path.join('tests', 'data', 'utf_noeol.txt')
        with ropen(filename, encoding='utf8') as f:
            if six.PY2:
                self._check_utf(f.next(), 8, ' 7')
                self._check_utf(f.next(), 9, ' 6\n')
                self._check_utf(f.next(), 9, ' 5\n')
                self._check_utf(f.next(), 9, ' 4\n')
                self._check_utf(f.next(), 9, ' 3\n')
                self._check_utf(f.next(), 9, ' 2\n')
                self._check_utf(f.next(), 9, ' 1\n')
            else:
                self.assertEqual(f.next(), 'Γραμμή 7')
                self.assertEqual(f.next(), 'Γραμμή 6\n')
                self.assertEqual(f.next(), 'Γραμμή 5\n')
                self.assertEqual(f.next(), 'Γραμμή 4\n')
                self.assertEqual(f.next(), 'Γραμμή 3\n')
                self.assertEqual(f.next(), 'Γραμμή 2\n')
                self.assertEqual(f.next(), 'Γραμμή 1\n')
            self.assertRaises(StopIteration, f.next)

    def test_utf_noeol_small_buffer(self):
        filename = os.path.join('tests', 'data', 'utf_noeol.txt')
        with ropen(filename, encoding='utf8', bufsize=3) as f:
            if six.PY2:
                self._check_utf(f.next(), 8, ' 7')
                self._check_utf(f.next(), 9, ' 6\n')
                self._check_utf(f.next(), 9, ' 5\n')
                self._check_utf(f.next(), 9, ' 4\n')
                self._check_utf(f.next(), 9, ' 3\n')
                self._check_utf(f.next(), 9, ' 2\n')
                self._check_utf(f.next(), 9, ' 1\n')
            else:
                self.assertEqual(f.next(), 'Γραμμή 7')
                self.assertEqual(f.next(), 'Γραμμή 6\n')
                self.assertEqual(f.next(), 'Γραμμή 5\n')
                self.assertEqual(f.next(), 'Γραμμή 4\n')
                self.assertEqual(f.next(), 'Γραμμή 3\n')
                self.assertEqual(f.next(), 'Γραμμή 2\n')
                self.assertEqual(f.next(), 'Γραμμή 1\n')
            self.assertRaises(StopIteration, f.next)
