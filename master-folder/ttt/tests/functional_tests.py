from selenium import webdriver
import unittest
from splinter import Browser


class NewGametest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_game(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('TTT', self.browser.title)

    def test_links(self):
        self.browser.get('http://localhost:8000')
        self.browser.find_element_by_xpath("//img[@title='logo']").click()
        self.browser.get('https://github.com/pmuldoon86/machine-learning')
        self.assertEqual(self.browser.title, 'GitHub - pmuldoon86/machine-learning: Makers Week 9')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
