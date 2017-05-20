from src.Exceptions.invalid_person import InvalidPersonType
from src.Exceptions.user_exist import UserAlreadyExist
from src.persons import Staff, Fellow


class Dojo(object):
    def __init__(self):
        self.list_of_staffs = []
        self.list_of_fellows = []
        self.staffs_and_fellows = []

    def add_person(self, person_name, person_type, person_id, wants_accomm="N"):
        """
        Add a person into the Dojo
        :return: size of dojo incremented by one
        """
        if person_id in self.staffs_and_fellows:
            raise UserAlreadyExist
        else:
            if person_type.lower() == "staff":
                person = Staff(person_name, person_id)
                self.list_of_staffs.append(person)
                self.staffs_and_fellows.append(person.person_id)
            elif person_type.lower() == "fellow":
                person = Fellow(person_name, person_id, wants_accomm)
                self.list_of_fellows.append(person)
                self.staffs_and_fellows.append(person.person_id)
            else:
                raise InvalidPersonType
