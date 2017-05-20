from src.Exceptions.invalid_person import InvalidPersonType
from src.Exceptions.user_exist import UserAlreadyExist
from src.persons import Staff, Fellow
from src.rooms import Office, LivingSpace


class Dojo(object):
    def __init__(self):
        self.list_of_staffs = []
        self.list_of_fellows = []
        self.staffs_and_fellows = []
        self.list_of_offices = []
        self.list_of_living_space = []

    def create_room(self, room_name, room_type):
        if room_type.lower() == "office":
            self.list_of_offices.append(Office(room_name))
        elif room_type.lower() == "livingspace":
            self.list_of_living_space.append(LivingSpace(room_name))

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
