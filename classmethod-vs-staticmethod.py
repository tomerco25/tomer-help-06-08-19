from datetime import date
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("self.name:", self.name)
        print("self.age:", self.age)
        print("------------------------------")
        # a class method to create a Person object by birth year.
    def double(self,double):
            self.double= double
            print("running function double in class person:")
            print("self.double:", self.double)
            self.double = double * 2
            print("self.double*2:", self.double)
            print("-------------------")
            return self.double
    @classmethod
    def fromBirthYear(cls, name, year):
        print ("class name:",cls)
        print ("name in classmethod:",name)
        print ("year in classmethod:",year)
        print("------------------------------")
        print("running __init__ :")
        return cls(name, date.today().year - year)
        # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18
print("person-1-instance:")
person1 = Person('person-1-name', 21)
person1.double(33)
print("person-2-instance:")
person2 = Person.fromBirthYear('person2-name', 1996)
print ("instance outside class:",person1.age)
print ("-----------")
print ("@classmethod in program:",person2.age)
print ("-----------")
print ("@staticmethod in program:",Person.isAdult(22))