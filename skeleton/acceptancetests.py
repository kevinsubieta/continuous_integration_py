from unittest import TestCase
from urllib import request


class TestVerifications(TestCase):
    def test_insert_when_name_has_number_a_error_appears(self):
        html = request.urlopen(
            'http://localhost:6543/add_person?inputId=1&inputName=name2&inputLastname=last_name&inputBirthday=1994-12-10'). \
            read().decode('utf-8')
        self.assertIn('errors_div', html)
