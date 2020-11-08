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
        quiz_title_input = self.browser.find_element_by_css_selector('.create-quiz__title-input')
        quiz_title_input.send_keys('History quiz')
        quiz_form_submit_button = self.browser.find_element_by_css_selector('.create-quiz__submit-btn')

        # He submits the form
        quiz_form_submit_button.click()
        time.sleep(1)

        # .. and sees the new title in the quiz table
        quiz_titles = self.browser.find_elements_by_class_name('quizes__list-item')
        self.assertTrue(any(['History quiz' in title.text for title in quiz_titles]))

    def test_visit_home_page(self):
        # Joe follow a link and finds himself on our app
        self.browser.get('http://localhost:3000')
        self.assertIn('Quiz', self.browser.title, 'Page title does not contain Quiz')

        home_page_title = self.browser.find_element_by_class_name('home__title')
        self.assertIn('Welcome to the Quiz App', home_page_title.text)

    # def test_register_user(self):
    #     # Joe liked what he saw and wants to register
    #     self.browser.get('http://localhost:3000')
    #
    #     register_button = self.browser.find_element_by_class_name('home__register-btn')
    #     register_button.click()
    #     time.sleep(1)
    #
    #     register_page_title = self.browser.find_element_by_class_name('register__title')
    #     self.assertIn('Welcome to the Quiz App', register_page_title.text)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
