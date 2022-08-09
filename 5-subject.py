from faker import Faker
fake=Faker(["pl-PL"])
Faker.seed(0)
class Card:
    def __init__(self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name
class BaseContact(Card):
    def __init__(self,first_name,last_name, msisdn):
        self.first_name=first_name
        self.last_name=last_name
        self.msisdn=msisdn
    def contact(self):
        return f"Wybieram numer {self.msisdn} i dzwonię do {self.first_name} {self.last_name}."
    def __repr__(self):
        return f"{self.first_name} {self.last_name}, {self.msisdn}"
    def namelenght(self):
        return f"Imię ma: {len(self.first_name)} znaków. Nazwisko ma {len(self.last_name)} znaków."
class BusinessContact(BaseContact):
    def __init__(self, first_name, last_name, prv_number, phone_number, company, job, email):
        self.first_name=first_name
        self.last_name=last_name
        self.prv_number=prv_number
        self.phone_number=phone_number
        self.company=company
        self.job=job
        self.email=email
    def __repr__(self):
        return f"{self.first_name} {self.last_name}, {self.phone_number}, {self.company}, {self.job}, {self.email}"
    def contact(self):
        print(f"Wybieram numer {self.phone_number} i dzwonię do {self.first_name} {self.last_name}.")
    def namelenght(self):
        return f"Imię ma: {len(self.first_name)} znaków. Nazwisko ma {len(self.last_name)} znaków."
cardlist=[]        

def createcontacts():
    x=input("Jaką wizytówkę chcesz stworzyć? Prywatną, czy biznesową?[P/B]:")
    y=input("Ile wizytówek chcesz stworzyć?:")
    y=int(y)
    if x=="P":
        for _ in range(y):
            cardlist.append(BaseContact(fake.first_name(),fake.last_name(),fake.msisdn()[4:]))
        for obj in cardlist:
            print(obj.first_name, obj.last_name, obj.msisdn)
            print(obj.namelenght())
            print(obj.contact())
    elif x=="B":
        for _ in range(y):
            cardlist.append(BusinessContact(fake.first_name(),fake.last_name(),fake.msisdn()[4:], fake.phone_number(), fake.company(), fake.job(), fake.email()))
        for obj in cardlist:
            print(obj.first_name, obj.last_name, obj.phone_number, obj.company, obj.job, obj.email) 
            print(obj.namelenght())
            print(obj.contact())

createcontacts()


    



        
















    





