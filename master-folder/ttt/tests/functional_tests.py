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

    def test_links(self):
        self.browser.get('http://localhost:8000')
        image = self.browser.find_element_by_xpath("//img[@title='logo']")
        image.click()
        self.assertIn('pmuldoon86/machine-learning: Makers Week 9', self.browser.title)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
