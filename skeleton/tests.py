import unittest
import transaction

from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner
from pyramid import testing

if __name__ == '__main__':
    unittest.main(testRunner=TeamcityTestRunner())


def dummy_request(dbsession):
    return testing.DummyRequest(dbsession=dbsession)


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp(settings={
            'sqlalchemy.url': 'sqlite:///:memory:'
        })
        self.config.include('skeleton.models')
        settings = self.config.get_settings()

        from skeleton.models import (
            get_engine,
            get_session_factory,
            get_tm_session,
        )

        self.engine = get_engine(settings)
        session_factory = get_session_factory(self.engine)

        self.session = get_tm_session(session_factory, transaction.manager)

    def init_database(self):
        from skeleton.models.meta import Base
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        from skeleton.models.meta import Base

        testing.tearDown()
        transaction.abort()
        Base.metadata.drop_all(self.engine)




class TestMyViewSuccessCondition(BaseTest):

    def setUp(self):
        super(TestMyViewSuccessCondition, self).setUp()
        self.init_database()

        from skeleton.models import Person

        # model = MyModel(name='one', value=55)
        # self.session.add(model)

    def test_passing_view(self):
        from skeleton.views.peopleController import PeopleController
        req = dummy_request(self.session)
        c = PeopleController(req)
        info = c.people()
        # info = my_view(dummy_request(self.session))
        self.assertEqual(info['one'].name, 'one')
        self.assertEqual(info['project'], 'skeleton')



class TestMyViewFailureCondition(BaseTest):

    def test_failing_view(self):
        from .views.default import my_view
        info = my_view(dummy_request(self.session))
        self.assertEqual(info.status_int, 500)



#
#if __name__ == '__main__':
#    if is_running_under_teamcity():
#        runner = TeamcityTestRunner()
#    else:
#        runner = unittest.TextTestRunner()
#    unittest.main(testRunner=runner)