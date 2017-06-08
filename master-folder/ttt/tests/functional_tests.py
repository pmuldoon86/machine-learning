from selenium import webdriver
import unittest


class NewGametest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()




browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'TTT' in browser.title, "Browser title was " + browser.title

browser.quit()
