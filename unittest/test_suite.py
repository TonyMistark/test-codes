#!/usr/bin/env python
# encoding: utf-8

import unittest
from test_mathfunc import TestMathFunc
from HTMLTestRunner import HTMLTestRunner

if __name__== "__main__":
    print("*"*20)
    suite = unittest.TestSuite()
    tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
    suite.addTests(tests)
    print("-=-=--")
    with open("/Users/tony_mistark/projects/test-codes/unittest/HTMLReport.html", "w") as f:
        print("l0-0-0-l")
        runner = HTMLTestRunner(
            stream=f,
            title="MathFun Test Report",
            description="generated by HTMLTestTestRunner.",
            verbosity=2)
        runner.run(suite)