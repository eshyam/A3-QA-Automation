"""
All the classes and corresponding methods will be here ,all the methods are reusable components
These methods loosly couples so anyone can make use of them anytime
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import os
import sys
import time

# Getting Current working Folder
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

# Getting Parent folder ot he Current working Folder
folder_path = os.path.abspath(os.path.join(dir_path, os.pardir))
print(folder_path)

# Navigating  to desired folder
sys.path.insert(0, folder_path + "\Syslibrary")

# Importing module from Syslibrary
from Syslibrary.datadriver import readjson

# Creating class object and instance of that object
jsonread1 = readjson()


class launchapplication:
    def intializebrowser(self):
        env = jsonread1.jsonread(folder_path + '\Env\setup.json')
        if env['browser'] == 'chrome':
            # browser = webdriver.Chrome(folder_path + '\Env\chromedirver.exe')
            browser = webdriver.Chrome()
            browser.implicitly_wait(10)
            browser.maximize_window()
            return browser
        elif env['browser'] == 'firefox':
            browser = webdriver.Firefox()
            browser.implicitly_wait(10)
            browser.maximize_window()
            return browser
        elif env['browser'] == 'Ie':
            browser = webdriver.Ie()
            browser.implicitly_wait(10)
            browser.maximize_window()
            return browser
        elif env['browser'] == 'headlessChrome':
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--window-size =1920x1080')
            chrome_driver = folder_path + '\Env\chromedriver.exe'
            browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
            browser.implicitly_wait(10)
            return browser

    def closebrowser(self,browser):
        browser.close()

    def inputurl(self,browser):
        url = jsonread1.jsonread(folder_path + '\Env\setup.json')
        if url['url'] == 'Qa':
            stagurl = jsonread1.jsonread(folder_path + '\Env\setup.json')
            browser.get(stagurl['Qa'])
        elif url['url'] == 'Production':
            prestagurl = jsonread1.jsonread(folder_path + '\Env\setup.json')
            browser.get(prestagurl['Production'])

    def locators(self):
        locators = jsonread1.jsonread(folder_path + '\Object\locators.json')
        return locators

    def testdata(self):
        testdata = jsonread1.jsonread(folder_path + '\Object\locators.json')
        return testdata

class dashboard():
    def test_dashboard(self, browser):
        app_testdata = jsonread1.jsonread(folder_path + '\Data\Testdata.json')
        app_locators = jsonread1.jsonread(folder_path + '\Object\locators.json')

        userid = app_locators["uid"]
        password = app_locators['pwd']
        signin = app_locators["signin"]
        help = app_locators["help"]
        close = app_locators["close"]

        username = app_testdata["username"]
        passwd = app_testdata["passwd"]

        Uid = browser.find_element_by_id(userid)
        Uid.send_keys(username)

        Pwd = browser.find_element_by_id(password)
        Pwd.send_keys(passwd)

        Click_signin = browser.find_element_by_xpath(signin)
        Click_signin.click()







