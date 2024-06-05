from faker import Faker

fake = Faker()

print(fake.name())

__import__('pprint').pprint(fake.address())

