import unittest
import os
from random import randint
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import touch_action 

success = True
desired_caps={}
desired_caps['appium-version']="1.5.0"
desired_caps['platformName']='iOS'
desired_caps['platformVersion']='11.3'
desired_caps['deviceName']='iPhone Simulator'
desired_caps['app']='/Users/wangyu/Library/Developer/Xcode/DerivedData/Driver-gairfsuwqcdjwddhszzpqjfmtifj/Build/Products/Debug-iphonesimulator/Driver.app'
desired_caps['automationName']='XCUITest'
desired_caps['autoWebView']='true'
desired_caps['--bootstrap-port']='4723'
desired_caps['--webkit-debug-proxy-port']='27753'

class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
		self.login()
	def login(self):
		self.driver.implicitly_wait(40)
		button_login=self.driver.find_element_by_name(u'button_login')
		button_login.click()
		sleep(1)

		self.driver.find_element_by_xpath('//iOS.widget.EditText')[4].click()
		self.driver.find_element_by_name(u'Save').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name('Log In').click()
        self.driver.find_element_by_name('Change Login Mode').click()
        username = self.driver.find_element_by_name('21658782@student.uwa.edu.au')
        sleep(0.3)
        username.send_keys(YOUR_QQ)
        sleep(0.3)
        password = self.driver.find_elements_by_xpath('//iOS.widget.EditText')[1]
        sleep(0.3)
        password.send_keys(YOUR_PASSWORD)

        self.driver.find_element_by_name('Log In').click()
        self.driver.implicitly_wait(30)
        try:
            self.driver.find_element_by_name('No').click()
        except:
            pass
        self.driver.implicitly_wait(100)  # Must have it ? not sure

        self.driver.find_element_by_name('Discover').click()
        sleep(.1)
        self.driver.find_element_by_name('Moments').click()
        sleep(3)
        self.driver.quit()

        
if __name__ == '__main__':
    Wechat().__int__()
