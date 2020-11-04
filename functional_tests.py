from selenium import webdriver
import unittest


class UserVisitTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_opens_home_page(self):
        self.browser.get('http://localhost:3000')
        self.assertIn('Quiz', self.browser.title)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
