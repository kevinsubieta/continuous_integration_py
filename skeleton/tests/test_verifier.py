from datetime import date
from unittest import TestCase
from unittest.mock import Mock

from skeleton.logic.verifier import Verifier
from skeleton.models import Person


class TestVerifier(TestCase):
    def test_verify_when_numbers_as_name_given_result_errors_appear(self):
        p = Person()
        p.name = 'asdf1234'
        p.last_name = 'asfasdf'
        p.birthday = date(1991, 9, 12)
        v = Verifier()
        m = Mock()
        m.today.return_value = date(2000, 9, 9)
        v.verify(p, date)
        self.assertTrue(len(v.errors))
