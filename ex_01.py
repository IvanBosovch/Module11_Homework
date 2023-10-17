from collections import UserDict
from datetime import datetime, date

class Field:
    def __init__(self, value:str):
        self.value = value
    
    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        self.value = value            


class Phone(Field):
    def __init__(self, value:str):
        if len(value) != 10 or not value.isdigit():
            raise ValueError
        self.value = value   

class Birthday(Field):
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        try:
            self._value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError('Not correct birthday')

    def __repr__(self):
        return f"{self.value}"


class Record:
    def __init__(self, name, birthday):
        self.name = Name(name)       
        self.phones = []
        self.birthday = birthday
       
    def add_phone(self, phone_add):
        self.phones.append(Phone(phone_add))
        x = [str(lt) for lt in self.phones]
       
    def remove_phone(self, phone_remove):
        self.phones.remove(self.find_phone(phone_remove))

    def find_phone(self, phone_find):
        for x in self.phones:
            if x.value == phone_find:
                return x

    def edit_phone(self, old_phone, new_phone):
        if self.find_phone(old_phone) in self.phones:
            lst_phones = [str(lt) for lt in self.phones]
            phone_index = lst_phones.index(old_phone)
            self.phones[phone_index] = Phone(new_phone)
        else: 
            raise ValueError
        
    def days_to_birthday(self):
        current_today = date.today()
        birth = self.birthday.value.replace(year=current_today.year)
        dif_date = birth - current_today
        if dif_date.days > 0:
            return dif_date.days
        else:
            birth = self.birthday.value.replace(year=current_today.year + 1)
            dif_date = birth - current_today
            return dif_date.days
        
    def __repr__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
        def add_record(self, record: Record):
            self[str(record.name)] = record

        def find(self, find_name) -> Record:
            if find_name in self.data.keys():
                return self.get(find_name)

        def delete(self, name):
            if name in self.data.keys():
                self.data.pop(name)

        def iterator(self, n=0):
            num = 0
            result = ''
            for k, v in self.data.items():
                
                result = f'Name: {k} | Phone: {v}'
                num += 1
                if num >= n:
                    yield result
                    

rc = Record('Ivan') 
print(rc.days_to_birthday())      





# rec1 = Record('Ivan')
# rec1.add_phone('1111111111')
# rec2 = Record('Sima')
# rec2.add_phone('2222222222')

# book.add_record(rec1)
# book.add_record(rec2)

# for app in book.iterator(1):
#     print(app)