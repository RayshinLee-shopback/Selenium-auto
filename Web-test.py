#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on wednesday Nov 03/11/20 12:46:35 2020

@author: Rayshin Lee
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import unittest


class Home(unittest.TestCase):  

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.shopback.com.tw/") 

    def test_referral(self):
        
        while True:
            try:
               ad = self.driver.find_element_by_xpath('//*[@id="lightbox1603954982260"]/a/img')#.is_displayed():
               x = self.driver.find_element_by_xpath('//*[@id="lightbox1603954982260"]/div').click()
               time.sleep(1)
               break
            except NoSuchElementException:
                break

        elem = self.driver.find_element_by_xpath('//*[@id="header"]/div/header/div[1]/div[1]/div[1]/div[3]/div/span/div[contains(text(),"/")]')
        logoutsite = 'https://www.shopback.com.tw/login?redirect=%2Freferral%2Finvite'
        if elem.is_displayed():
            referralxpath = self.driver.find_element_by_xpath('//*[@id="header"]/div/header/div[1]/div[1]/div[1]/div[3]/div/a').click()
            time.sleep(1)
        '''if logoutsite:
            print('pass')
            time.sleep(1)
            '''
        logo = self.driver.find_element_by_xpath('//*[@id="header"]/div/header/div[1]/div[1]/div[1]/a').click()
        time.sleep(0.5)

        while True:
            try:
               ad = self.driver.find_element_by_xpath('//*[@id="lightbox1603954982260"]/a/img')#.is_displayed():
               x = self.driver.find_element_by_xpath('//*[@id="lightbox1603954982260"]/div').click()
               time.sleep(1)
               break
            except NoSuchElementException:
                break

   
    def tearDown(self):
        self.driver.close()
        

class Search(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.shopback.com.tw/")

    def test_login(self):

        #self.driver.get("https://www.shopback.com.tw/")
        #Find login path
        while True:
            try:
               ad = self.driver.find_element_by_xpath('//*[@id="lightbox1603954982260"]/a/img')#.is_displayed():
               x = self.driver.find_element_by_xpath('//*[@id="lightbox1603954982260"]/div').click()
               time.sleep(1)
               break
            except NoSuchElementException:
                break

        login1 = self.driver.find_element_by_xpath("//div[@id='header']/div/header/div/div/div/div[3]/div/span/div").click()
        time.sleep(0.5)
        log2 = self.driver.find_element_by_xpath("//div[@id='auth-popup-container']/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/span").click()
        time.sleep(0.5)
        log3 =self.driver.find_element_by_xpath("//div[@id='auth-popup-container']/div/div[2]/div[2]/div/div/div[2]/div/div/div/div/div").click()
        time.sleep(0.5)
        
        #email 
        email1 = self.driver.find_element_by_xpath("//div[@id='auth-popup-container']/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]/input")
        email1.send_keys("allen@shopback.com") 
        time.sleep(0.5)
        email2 =self.driver.find_element_by_xpath("//div[@id='auth-popup-container']/div/div[2]/div[2]/div/div/div[2]/div/div/button").click()
        time.sleep(1)
        
        #password
        pw1 = self.driver.find_element_by_xpath("//div[@id='auth-popup-container']/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]/input")
        pw1.send_keys("123")
        time.sleep(0.5)
        pw2 =self.driver.find_element_by_xpath("//div[@id='auth-popup-container']/div/div[2]/div[2]/div/div/div[2]/div/div/button").click()       
        time.sleep(1)

        while True:
            try:
               ad = self.driver.find_element_by_xpath('//*[@id="lightbox1603954982260"]/a/img')#.is_displayed():
               x = self.driver.find_element_by_xpath('//*[@id="lightbox1603954982260"]/div').click()
               time.sleep(1)
               break
            except NoSuchElementException:
                break

    #def test_searchbar(self):

        search = self.driver.find_element_by_xpath('//*[@id="header"]/div/header/div[1]/div[1]/div[1]/div[2]/div[1]/input')
        time.sleep(1)
        search.send_keys("iphone")
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        logo = self.driver.find_element_by_xpath('//*[@id="__next"]/div/nav/div/div[1]/div/div[2]/a/img').click()
        time.sleep(0.5)

        while True:
            try:
               ad = self.driver.find_element_by_xpath('//*[@id="lightbox1603954982260"]/a/img')#.is_displayed():
               x = self.driver.find_element_by_xpath('//*[@id="lightbox1603954982260"]/div').click()
               time.sleep(1)
               break
            except NoSuchElementException:
                break

   #def test_earncashback(self):

        earn = self.driver.find_element_by_xpath('//*[@id="header"]/div/header/div[1]/div[1]/div[1]/div[3]/div/div[1]/div[1]/div').click()
        time.sleep(1)
        learn_more = self.driver.find_element_by_xpath('//*[@id="header"]/div/header/div[1]/div[1]/div[1]/div[3]/div/div[1]/div[2]/div/div[4]/a').click()
        time.sleep(2)
        logo = self.driver.find_element_by_xpath('//*[@id="header"]/div/header/div[1]/div[1]/div[1]/a').click()
        time.sleep(0.5)

        while True:
            try:
               ad = self.driver.find_element_by_xpath('//*[@id="lightbox1603954982260"]/a/img')#.is_displayed():
               x = self.driver.find_element_by_xpath('//*[@id="lightbox1603954982260"]/div').click()
               time.sleep(1)
               break
            except NoSuchElementException:
                break

#def test_referral(self):

        elem = self.driver.find_element_by_xpath('//*[@id="header"]/div/header/div[1]/div[1]/div[1]/div[3]/div/div[2]/div[1]/div')
        logoutsite = 'https://www.shopback.com.tw/referral/invite'
        if elem.is_displayed():
            referralxpath = self.driver.find_element_by_xpath('//*[@id="header"]/div/header/div[1]/div[1]/div[1]/div[3]/div/a').click()
            time.sleep(1)
        if logoutsite:
            print('pass')
            time.sleep(1)
        logo = self.driver.find_element_by_xpath('//*[@id="header"]/div/header/div[1]/div[1]/div[1]/a').click()
        time.sleep(0.5)

        while True:
            try:
               ad = self.driver.find_element_by_xpath('//*[@id="lightbox1603954982260"]/a/img')#.is_displayed():
               x = self.driver.find_element_by_xpath('//*[@id="lightbox1603954982260"]/div').click()
               time.sleep(1)
               break
            except NoSuchElementException:
                break
    


def tearDown(self):
        # Note close() will close the current tab; quit() will close the entire browser
        self.driver.close()
    
       
if __name__ == '__main__':
   unittest.main()

    
