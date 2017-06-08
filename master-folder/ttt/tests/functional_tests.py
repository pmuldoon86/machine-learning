from selenium import webdriver
import unittest


class NewGametest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_game(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('TTT', self.browser.title)
        self.fail('Finish the test!')

browser.quit()
