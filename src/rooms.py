class Room(object):
    def __init__(self, name, room_type):
        self.name = name
        self.type = room_type


class Office(Room):
    def __init__(self, name):
        super(Office, self).__init__(name, "Office")
        self.office_size = 6


class LivingSpace(Room):
    def __init__(self, name):
        super(LivingSpace, self).__init__(name, "LivingSpace")
        self.living_space_size = 4
