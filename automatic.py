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
desired_caps['app']='/Users/wangyu/Library/Developer/Xcode/DerivedData/Driver-gairfsuwqcdjwddhszzpqjfmtifj/Build/Products/Debug-iphonesimulator/uwarideshare.app'
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


        #test with correct username and password
        self.driver.find_element_by_name('Log In').click()
        self.driver.find_element_by_name('Change Login Mode').click()
        username = self.driver.find_element_by_name('21658782@student.uwa.edu.au')
        sleep(0.3)
        username.send_keys(YOUR_Email)
        sleep(0.3)
        password = self.driver.find_elements_by_xpath('//iOS.widget.EditText')[1]
        sleep(0.3)
        password.send_keys('welcomeuwarideshare123')
        driver.find_element_by_id('uwarideshare.app:id/login_button').click()
        time.sleep(3)
        # login successfully, swap down to get the button
        driver.swipe(500, 200, 500, 800, 0)
        time.sleep(2)
        name = driver.find_element_by_id('uwarideshare.app:id/login_username_tv').text
        #add assert, if the name is incoorect, print error information
        try:
            assert 'No_matter' in name
            print 'loginUser is right'
        except AssertionError as e:
            print 'loginUser is Error'

        #test with incorrect username and password
        self.driver.find_element_by_name('Log In').click()
        self.driver.find_element_by_name('Change Login Mode').click()
        username = self.driver.find_element_by_name('123@student.uwa.edu.au')
        sleep(0.3)
        username.send_keys(YOUR_Email)
        sleep(0.3)
        password = self.driver.find_elements_by_xpath('//iOS.widget.EditText')[1]
        sleep(0.3)
        password.send_keys('welcomeuwarideshare123')
        driver.find_element_by_id('uwarideshare.app:id/login_button').click()
        time.sleep(3)
        # login successfully, swap down to get the button
        driver.swipe(500, 200, 500, 800, 0)
        time.sleep(2)
        name = driver.find_element_by_id('uwarideshare.app:id/login_username_tv').text
        #add assert, if the name is incoorect, print error information
        try:
            assert 'valid' in name
            print 'Incorrect username and password test pass'
        except AssertionError as e:
            print 'Incorrect username and password test fail'

    def register(self):
        #test with correct username and password
        self.driver.find_element_by_name('Sign up').click()
        username = self.driver.find_element_by_name('21658782@student.uwa.edu.au')
        sleep(0.3)
        username.send_keys(YOUR_Email)
        sleep(0.3)
        password = self.driver.find_elements_by_xpath('//iOS.widget.EditText')[1]
        sleep(0.3)
        password.send_keys('welcomeuwarideshare123')
        driver.find_element_by_id('uwarideshare.app:id/signup_button').click()
        time.sleep(3)
        #when regester successfully, it should come back to the main interface
        name=self.driver.find_element_by_name('Sign up').text
        #add assert, if regester fail, print error information
        try:
            assert 'Sign' in name
            print ' regester successfully'
        except AssertionError as e:
            print 'regester fail'
        #test with invalid username and password
        self.driver.find_element_by_name('Sign up').click()
        username = self.driver.find_element_by_name('21658782@student')
        sleep(0.3)
        username.send_keys(YOUR_Email)
        sleep(0.3)
        password = self.driver.find_elements_by_xpath('//iOS.widget.EditText')[1]
        sleep(0.3)
        password.send_keys('welcomeuwarideshare123')
        driver.find_element_by_id('uwarideshare.app:id/signup_button').click()
        time.sleep(3)
        #when regester successfully, it should come back to the main interface
        name=find_element_by_xpath('uwarideshare.app:id/signup_button').click()
        #add assert, if regester fail, print error information
        try:
            assert 'invalid' in name
            print ' invalid input regester test pass'
        except AssertionError as e:
            print 'invalid input regester test pass fail'

    def swipe_left(self,driver):
        '''swipe_left'''
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        driver.swipe(x*3/4,y/4,x/4,y/4)

    def swipe_right(self,driver):
        '''swipe_right'''
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        driver.swipe(x/4,y/4,x*3/4,y/4)

    def swipe_down(self,driver):
        '''swipe_down'''
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        driver.swipe(x/2,y*3/4,x/2,y/4)

    def swipe_up(self,driver):
        '''swipe up'''
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        driver.swipe(x/2,y/4,x/2,y*3/4)

if __name__ == '__main__':
    Wechat().__int__()
