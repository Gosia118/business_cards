from faker import Faker

fake = Faker('pl_PL')


class BaseContact:
    def __init__(self, first_name, last_name, private_phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.private_phone = private_phone
        self.email = email

    def contact(self):
        return f"Wybieram numer {self.private_phone} i dzwonię do {self.first_name} {self.last_name}"

    @property
    def label_length(self):
        total = len(self.first_name) + len(self.last_name)
        return f"Ilość znaków: {total}"
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.private_phone} {self.email}'


class BusinessContact(BaseContact):
    def __init__(self, company, job, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.job = job
        self.bussines_phone = business_phone

    def contact(self):
        return f"Wybieram numer {self.bussines_phone} i dzwonię do {self.first_name} {self.last_name}"


def create_contacts():
    a = int(input("Wpisz cyfrę: "))
    card = int(input("Wybierz: 1 - Base lub 2 - Business: "))
    for i in range(0, a):
        if card == 1:
            print(BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), private_phone=fake.phone_number(), email=fake.email()))
        elif card == 2:
            print(BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), private_phone=fake.phone_number(), company=fake.company(), job=fake.job(), email=fake.email(), business_phone=fake.phone_number()))


if __name__ == "__main__":
    card2 = BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), private_phone=fake.phone_number(), email=fake.email())
    card3 = BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), private_phone=fake.phone_number(), company=fake.company(), job=fake.job(), email=fake.email(), business_phone=fake.phone_number())
    print(card2.contact())
    print(card3.contact())
    print(card2.label_length)
    print(card3.label_length)
    create_contacts()
