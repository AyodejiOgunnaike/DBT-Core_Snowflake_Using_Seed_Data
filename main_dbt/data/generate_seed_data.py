from faker import Faker
import csv

fake = Faker()
num_records = 1000

with open('seeds/customers.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'name', 'email', 'city'])
    for _ in range(num_records):
        writer.writerow([fake.unique.random_int(min=1, max=10000), fake.name(), fake.email(), fake.city()])