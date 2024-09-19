from model.da.person_da import personDa
from model.entity.person import Person



class PersonBl:
    @staticmethod
    def save(person):
        person_da = personDa()
        return person_da.save(person)