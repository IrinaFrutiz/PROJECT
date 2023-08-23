from data.data import Person
from faker import Faker

fake_en = Faker()

def generated_person():
    yield Person(
        full_name=fake_en.name(),
        email=fake_en.email(),
        current_address=fake_en.address(),
        permanent_address=fake_en.address(),
    )
