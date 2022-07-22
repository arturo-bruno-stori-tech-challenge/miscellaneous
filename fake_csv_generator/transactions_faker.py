#!python
"""
Quick and dirty script to create n random CSV transaction files
"""

import csv

from faker import Faker
from pathlib import Path
from random import randint, choice

fake = Faker()

for _ in range(100):
    client = fake.name()
    client_transactions_file = Path(Path(__file__).parent, 'transactions_csvs', f'{client.replace(" ", "_")}.csv')

    transactions = randint(1, 10000)
    balance = 0
    client_transactions_file.touch()

    print(client, client_transactions_file)

    with client_transactions_file.open(mode='w') as csv_file:
        fields = ['Id', 'Date', 'Transaction']
        writer = csv.DictWriter(csv_file, fieldnames=fields)

        writer.writeheader()

        for id in range(0, transactions):
            amount = fake.pyfloat(right_digits=2, max_value=1000, positive=True)

            kind = choice(['debit', 'credit'])
            if kind == 'debit':
                sign = '-'
                balance -= amount
            elif kind == 'credit':
                sign = '+'
                balance += amount

            month = randint(1, 12)
            day = randint(1, 28)  # KISS: Just to avoid issues with more days than in month
            date = f'{month}/{day}'

            writer.writerow({'Id': id, 'Date': date, 'Transaction': f'{sign}{amount}'})
        print('\t\t', balance)
