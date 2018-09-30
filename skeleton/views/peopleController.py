from datetime import datetime, date

from pyramid.httpexceptions import HTTPFound
from pyramid.renderers import render_to_response
from pyramid.request import Request
from pyramid.view import view_config

from skeleton.logic.verifier import Verifier
from skeleton.models import Person


class PeopleController:
    def __init__(self, req: Request):
        self.req = req
        self.db = self.req.dbsession

    @view_config(route_name='people', renderer='people.jinja2')
    def people(self):
        return {'people': self.db.query(Person).all()}

    @view_config(route_name='person', renderer='person.jinja2')
    def person(self):
        id_ = self.req.params.get('id')
        if id_ is None:
            return {'person': None}
        person = self.db.query(Person).get(id_)
        print(person.birthday.strftime('%Y-%m-%d'))
        return {'person': person, 'errors': []}

    @view_config(route_name='add_person', renderer='people.jinja2', request_method=['POST'])
    def update(self):
        person = Person()
        id_ = self.req.params.get('inputId')
        if id_ is not None and len(id_) > 0:
            person.id = id_
        person.name = self.req.params.get('inputName')
        person.last_name = self.req.params.get('inputLastname')
        birthday = self.req.params.get('inputBirthday')
        person.birthday = datetime.strptime(birthday, '%Y-%m-%d').date()
        v = Verifier()
        v.verify(person, date)
        if len(v.errors) > 0:
            return render_to_response(
                'person.jinja2',
                {'person': person, 'errors': v.errors},
                request=self.req
            )
        self.db.merge(person)
        return HTTPFound(location='/people')

    @view_config(route_name='delete_person', renderer='people.jinja2')
    def delete(self):
        id_ = self.req.params.get('id')
        self.db.query(Person).filter(Person.id == id_).delete()
        return HTTPFound(location='/people')
