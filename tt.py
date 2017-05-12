class Person:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''

    @property
    def full_name(self):
        '''
        Return the fullname of the person.
        :return: Fullname of a person
        '''
        return self.first_name + ' ' + self.last_name


p.first_name = 'Bad'
p.last_name = 'Ass'
print(p.full_name)
import os
print(os.getlogin())
