from sikuli import*
import HTMLTestRunner 
reload(HTMLTestRunner)
import unittest
import os,sys
import xlrd
import datetime

userdir = os.path.expanduser('~')
userdir.replace("//", "////")
RootFolder = userdir + "/Desktop/PRE_Sikuli_Automation"

if not RootFolder in sys.path: 
    sys.path.append(RootFolder)

from TestScripts import Constants as Constants
reload(Constants)
from Effects import *
from Transitions import *
from GlassPane_GE import *

workbook = xlrd.open_workbook(Constants.PRE_Test_Execution_Data)
worksheet = workbook.sheet_by_index(0)

testcase_list = []
for row in range(worksheet.nrows):
    area_flag = worksheet.cell(row, 4).value
    if area_flag == 1:
        testcase_list.append((str(worksheet.cell(row, 1).value)) + ',' + (str(worksheet.cell(row, 2).value)))

suite = unittest.TestSuite()

for testcase in testcase_list:
    testCase = testcase.split(",")
    className = testCase[0]
    functionName = testCase[1]
    suite.addTest(eval(className)(functionName))

now = datetime.datetime.now()
outputfilename = Constants.RootFolder + "/Output/TestReport_" + str(now.day) + str(now.month) + str(now.year) + "_" + str(now.hour) + str(now.minute) + str(now.second) + ".html"
outfile = file(outputfilename, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='PRE UI Tests Execution Report', verbosity=3, dirTestScreenshots=Constants.ScreenshotsFolder, description='This is test report for test execution of UI tests for Premiere Elements application.' )
runner.run(suite)