from selenium import webdriver
import unittest
import time
import uuid


def generate_random_string():
    return uuid.uuid4().hex[:8].upper()


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

    def test_register_user(self):
        # Joe liked what he saw and wants to register
        self.browser.get('http://localhost:3000')

        # Joe decides to follow the register link
        register_link = self.browser.find_element_by_class_name('navbar__register-btn')
        register_link.click()
        time.sleep(1)

        register_page_title = self.browser.find_element_by_class_name('register__title')
        self.assertIn('Register', register_page_title.text)

        random_password = generate_random_string()
        random_username = generate_random_string()

        # he fills in username
        username_input = self.browser.find_element_by_css_selector('#id_username')
        username_input.send_keys(random_username)

        # and password
        password_input = self.browser.find_element_by_css_selector('#id_password1')
        password_input.send_keys(random_password)

        confirm_password_input = self.browser.find_element_by_css_selector('#id_password2')
        confirm_password_input.send_keys(random_password)

        # when ready he submits the form
        register_button = self.browser.find_element_by_class_name('register__submit-btn')
        register_button.click()
        time.sleep(1)

        # and is redirected to login page


if __name__ == '__main__':
    unittest.main(warnings='ignore')
