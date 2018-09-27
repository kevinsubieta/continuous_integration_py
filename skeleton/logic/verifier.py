from skeleton.models import Person


class Verifier:
    def __init__(self):
        self.errors = list()

    def verify(self, person: Person, date):
        if not person.name.replace(' ', '').isalpha():
            self.errors.append('Name must contain letters only')

        if len(person.name) > 50:
            self.errors.append('Name must be shorter than 51 characters')

        if not person.last_name.replace(' ', '').isalpha():
            self.errors.append('Last name must contain letters only')

        if len(person.last_name) > 50:
            self.errors.append('Last name must be shorter than 51 characters')

        if person.birthday >= date.today():
            self.errors.append('Birthday must be before today\'s date')
