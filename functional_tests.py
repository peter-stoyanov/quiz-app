from selenium import webdriver
import unittest
import time

from selenium.webdriver.common.keys import Keys


class UserVisitTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_create_quiz_page(self):
        # Joe wants to create a quiz to challenge his friends and visits our cool app
        self.browser.get('http://localhost:3000/quiz')
        self.assertIn('Quiz', self.browser.title, 'Page title does not contain Quiz')

        # Joe puts in a title for the whole quiz
        quiz_title_input = self.browser.find_element_by_css_selector('.quiz-title-input')
        quiz_title_input.send_keys('History quiz')
        quiz_title_input.send_keys(Keys.ENTER)
        time.sleep(1)

        quiz_title = self.browser.find_element_by_css_selector('.quiz-title').text
        self.assertIn('History quiz', quiz_title)

    # def test_opens_quiz_page(self):
    #     # Joe has received a link to a quiz sent over from a friend
    #     self.browser.get('http://localhost:3000/quiz/075194d3-6885-417e-a8a8-6c931e272f00')
    #     self.assertIn('Quiz', self.browser.title, 'Page title does not contain Quiz')
    #
    #     # Joe sees a quiz and reads its title to see if he's interested
    #     quiestion_text = self.browser.find_element_by_tag_name('.quiz-title').text
    #     self.assertTrue(quiestion_text, 'No question content displayed')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
