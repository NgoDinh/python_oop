class Animals:
    #class attribute
    home = 'zoo'

    #instance attribute
    def __init__(self, animal_name, animal_age):
        self.name = animal_name
        self.age = animal_age

    #class method:
    @classmethod
    def change_home_class(cls,animal_new_home):
        cls.home = animal_new_home

    @classmethod
    def change_name_class(cls,animal_new_name):
        cls.name = animal_new_name

    def change_name(self, animal_new_name):
        self.name = animal_new_name

    def change_home(self, animal_new_home):
        self.home = animal_new_home

        
