from selenium import webdriver
import unittest
import os
import traceback
import time

from Syslibrary.datadriver import readjson
jsonread1 = readjson()

from Library.Launchapplication import launchapplication
application = launchapplication()

from Library.Launchapplication import dashboard
dashboard_test = dashboard()

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

folder_path = os.path.abspath(os.path.join(dir_path, os.pardir))
print(folder_path)

tf = 'test_TestcaseNo1004'

# Validate Performance Audit
class TestcaseNo1004(unittest.TestCase):
    def test_TestcaseNo1004(self):
        try:
            browser = application.intializebrowser()
            application.inputurl(browser)
            dashboard_test.test_dashboard(browser)

            app_locators = jsonread1.jsonread(folder_path + '\Object\locators.json')
            app_testdata = jsonread1.jsonread(folder_path + '\Data\Testdata.json')

            db_l_db_performanceaudit = app_locators["db_performanceaudit"]
            db_d_db_performanceaudit = app_testdata["db_performanceaudit"]

            time.sleep(3)
            db_costoptimizatin_xpath = browser.find_element_by_xpath(db_l_db_performanceaudit)
            print(db_costoptimizatin_xpath.text)
            self.assertEqual(db_costoptimizatin_xpath.text, db_d_db_performanceaudit)

        except Exception:
            traceback.print_exc()
            browser.save_screenshot(folder_path + '\Screenshots\Testcase-%s.png' % tf)
            self.fail('Test case No : 1004 is failed')
        finally:
            application.closebrowser(browser)


if __name__ == '__main__':
    unittest.main()


