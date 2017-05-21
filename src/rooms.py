from src.Exceptions.room_exceptions import OfficeFull, LivingSpaceFull


class Room(object):
    def __init__(self, name, room_type, capacity):
        self.name = name
        self.type = room_type
        self.capacity = capacity


class Office(Room):
    def __init__(self, name):
        super(Office, self).__init__(name, "Office", 6)
        self.__persons = []

    def add_person(self, person):
        if len(self.__persons) > 6:
            raise OfficeFull
        else:
            self.__persons.append(person)

    def get_allocated_space(self):
        # Return how many people have been allocated into this room
        return len(self.__persons)


class LivingSpace(Room):
    def __init__(self, name):
        super(LivingSpace, self).__init__(name, "LivingSpace", 4)
        self.__fellows = []

    def add_fellow(self, fellow):
        if len(self.__fellows) > 4:
            raise LivingSpaceFull
        else:
            self.__fellows.append(fellow)
