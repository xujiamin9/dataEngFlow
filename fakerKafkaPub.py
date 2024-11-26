from faker import Faker
import random
from datetime import datetime, timedelta
from kafka import KafkaProducer
import json

fake = Faker()
fake.seed_instance(0)

def generate_transaction():
    amount = round(random.uniform(10, 5000), 2)
    
    date = fake.date_time_between(start_date="-1y", end_date="now")
    
    return {
        "transaction_id": fake.uuid4(),
        "date": date.isoformat(),
        "amount": amount,
        "description": fake.bs(),
        "account_number": fake.bban(),
        "merchant": fake.company(),
        "category": fake.word(ext_word_list=["food", "transport", "entertainment", "utilities", "shopping"])
    }

# Generate 10 transactions
transactions = [generate_transaction() for _ in range(10)]

# Sort transactions by date
transactions.sort(key=lambda x: x['date'])

for transaction in transactions:
    # print(f"Date: {transaction['date']}")
    # print(f"Amount: {transaction['amount']}")
    # print(f"Description: {transaction['description']}")
    # print(f"Merchant: {transaction['merchant']}")
    # print(f"Category: {transaction['category']}")
    print(transaction)
    print('\n')

producer = KafkaProducer(bootstrap_servers='localhost:9092')

# producer.send('transactions', b'Hello, Kafka!')