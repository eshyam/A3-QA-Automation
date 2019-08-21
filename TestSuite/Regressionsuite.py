import os
import unittest
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from Library.HTMLTestRunner import HTMLTestRunner

from Testscripts.test_testCaseNo1001 import TestcaseNo1001
from Testscripts.test_testCaseNo1002 import TestcaseNo1002
from Testscripts.test_testCaseNo1003 import TestcaseNo1003
from Testscripts.test_testCaseNo1004 import TestcaseNo1004
from Testscripts.test_testCaseNo1005 import TestcaseNo1005
# from Testscripts.test_testCaseNo1006 import TestcaseNo1006

dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path = os.path.abspath(os.path.join(dir_path, os.pardir))


# importing individual test scripts
""" Note: Reason for making individual test scripts - s
As per standard framework guidelines - Each test script should be independent one
"""
suite = unittest.TestSuite()

suite.addTest(TestcaseNo1001('test_TestcaseNo1001'))
suite.addTest(TestcaseNo1002('test_TestcaseNo1002'))
suite.addTest(TestcaseNo1003('test_TestcaseNo1003'))
suite.addTest(TestcaseNo1004('test_TestcaseNo1004'))
suite.addTest(TestcaseNo1005('test_TestcaseNo1005'))
# suite.addTest(TestcaseNo1006('test_TestcaseNo1006'))

outfile = open(folder_path + '\Regressionreport\Regressionreport.html', 'w+')
runner = HTMLTestRunner(stream=outfile, verbosity=1, title=' Core Compete A3', description='Regressionreport', dirTestScreenshots =folder_path + '\\Screenshots')
runner.run(suite)
outfile.close()
