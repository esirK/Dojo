class Person(object):
    """
    Class Person that defines a person by name, type and id
    """
    def __init__(self, name="", person_type="", person_id=""):
        self.name = name
        self.person_type = person_type
        self.person_id = person_id


class Fellow(Person):
    """
    Class Fellow defines a person who can be given an accommodation in the dojo
    """
    def __init__(self, name, person_id, wants_accommodation="N"
                                                            ""):
        super(Fellow, self).__init__(name, "Fellow", person_id)
        self.wants_accommodation = wants_accommodation


class Staff(Person):
    """
    Staff Defines a Person who can't be accommodated in the dojo
    """
    def __init__(self, name, person_id):
        super(Staff, self).__init__(name, "Staff", person_id)
