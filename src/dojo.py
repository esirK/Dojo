from src.Exceptions.invalid_person import InvalidPersonType
from src.Exceptions.room_exceptions import OfficeFull, LivingSpaceFull, NoRoomAvailable
from src.Exceptions.user_exist import UserAlreadyExist
from src.persons import Staff, Fellow
from src.rooms import Office, LivingSpace
import colorama
from termcolor import colored

colorama.init()


class Dojo(object):
    def __init__(self):
        self.list_of_staffs = []
        self.list_of_fellows = []
        self.staffs_and_fellows = []
        self.list_of_offices = []
        self.list_of_living_space = []
        self.available_living_space = []
        self.available_offices = []

    def create_room(self, room_name, room_type):
        if room_type.lower() == "office":
            self.list_of_offices.append(Office(room_name))
            self.available_offices.append(Office(room_name))
            print()
            print(colored("Office " + room_name + " Added Successfully into The Dojo", 'green'))
        elif room_type.lower() == "livingspace":
            self.available_living_space.append(LivingSpace(room_name))
            self.list_of_living_space.append(LivingSpace(room_name))
            print(colored("Living Space " + room_name
                          + " Added Successfully into The Dojo", 'green'))

    def add_person(self, person_name, person_type, person_id, wants_accomm="N"):
        """
        Add a person into the Dojo... in a room
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
                self.allocate_random_room(person)
                self.staffs_and_fellows.append(person.person_id)
            else:
                raise InvalidPersonType

    def allocate_random_room(self, person):
        from random import randint
        if person.person_type.lower() == "fellow":
            if len(self.available_living_space) > 0:  # Living space(s) available
                # Pick a random room from list of available rooms
                room = (randint(0, len(self.available_living_space)))
                random_room = self.available_living_space[room - 1]
                random_room.add_fellow(person)
                print(colored(person.name + " Added Successfully "
                                            "into Living Space " +
                              random_room.name, 'green'))
                # Check if room is full and if so remove it from list of
                # available rooms
                if random_room.get_allocated_space() == random_room.capacity:
                    del self.available_living_space[random_room]
            else:
                raise NoRoomAvailable
