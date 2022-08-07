from faker import Faker
fake=Faker(["pl-PL"])
Faker.seed(0)
class Card:
    def __init__(self, first_name, last_name, company, job, email):
        self.first_name=fake.first_name()
        self.last_name=fake.last_name()
        self.company=fake.company()
        self.job=fake.job()
        self.email=fake.email()

card_list=[]
card_list.append(Card(fake.first_name(),fake.last_name(),fake.company(),fake.job(),fake.email()))
card_list.append(Card(fake.first_name(),fake.last_name(),fake.company(),fake.job(),fake.email()))
card_list.append(Card(fake.first_name(),fake.last_name(),fake.company(),fake.job(),fake.email()))
card_list.append(Card(fake.first_name(),fake.last_name(),fake.company(),fake.job(),fake.email()))
card_list.append(Card(fake.first_name(),fake.last_name(),fake.company(),fake.job(),fake.email()))

for obj in card_list:
    print(obj.first_name,obj.last_name,",",obj.company,",",obj.job,",",obj.email)


    





