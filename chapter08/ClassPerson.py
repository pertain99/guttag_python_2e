import datetime
class Person(object):

    def __init__(self, name):
        """Create a person"""
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name
        self.birthday = None

    def getName(self):
        """Returns self's full name"""
        return self.name

    def getLastName(self):
        """Returns self's last name"""
        return self.lastName

    def setBirthday(self, birthdate):
        """Assumes birthdate is of type datetime.date
        sets self's birthday to birthdate"""
        self.birthday = birthdate

    def getAge(self):
        """Returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return int((datetime.date.today() - self.birthday).days / 365)

    def __lt__(self, other):
        """Returns True if self precedes other in alphabetical
           order, and False otherwise.  Comparison is based on last
           names, but if these are the same full names are
           compared"""
        if self.lastName == other.lastName:
            return self.name < other.lastName
        return self.lastName < other.lastName

    def __str__(self):
        """Returns self's name"""
        return self.name

me = Person('Michael Guttag')
him = Person('Jhon Doll')
her = Person('Madonna')
print(him.getLastName())
him.setBirthday(datetime.date(1969, 8, 8))
her.setBirthday(datetime.date(1958, 8, 16))
print(him.getName(), 'is', him.getAge(), 'years old')
print(her.getName(), 'is', her.getAge(), 'years old')

print('\n------------\n')
pList = [me, him, her]

for p in pList:
    print(p)

print('\n------------\n')
pList.sort()

for p in pList:
    print(p)

