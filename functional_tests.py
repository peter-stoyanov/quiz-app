from selenium import webdriver
import unittest


class UserVisitTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_opens_quiz_page(self):
        # Joe har received a link to a quiz sent over from a friend
        self.browser.get('http://localhost:3000/quiz/075194d3-6885-417e-a8a8-6c931e272f00')
        self.assertIn('Quiz', self.browser.title)

        # Joe sees a question and reads it
        # quiestion_text = self.browser.find_element_by_tag_name('.question-content').text
        # self.assertIn('To-Do', quiestion_text)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
