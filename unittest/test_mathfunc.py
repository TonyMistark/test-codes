#!/usr/bin/env python
# encoding: utf-8

import unittest
from mathfunc import *
from HTMLTestRunner import HTMLTestRunner


class TestMathFunc(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("This setUpClass() method only clalled once.")

    @classmethod
    def tearDownClass(self):
        print("This tearDownClass() method only clalled once.")

    def setUp(self):
        print("do something before test.Prepare environment.")

    def tearDown(self):
        print("do someting after test.Clean up.")

    @unittest.skip("I don't want to run this case.")
    def test_add(self):
        self.assertEqual(3, add(1, 2))
        self.assertEqual(3, add(2, 2))

    def test_minus(self):
        self.assertEqual(1, minus(3, 2))

    def test_multi(self):
        self.assertEqual(6, multi(2, 3))

    def test_divide(self):
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))


if __name__ == "__main__":
    unittest.main(verbosity=2)
