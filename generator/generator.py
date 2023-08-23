from data.data import Person
from faker import Faker

fake_pl = Faker('pl_PL')

def generated_person():
    yield Person(
        full_name=fake_pl.name(),
        email=fake_pl.email(),
        current_address=fake_pl.address().replace('\n', ' '),
        permanent_address=fake_pl.address().replace('\n', ' '),
    )
