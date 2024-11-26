from faker import Faker
import random
from datetime import datetime, timedelta
from kafka import KafkaProducer
import json

fake = Faker()
fake.seed_instance(random.randint(0, 20))

def generate_transaction():
    amount = round(random.uniform(10, 5000), 2)
    
    date = fake.date_time_between(start_date="-1y", end_date="now")
    
    return {
        "transaction_id": fake.uuid4(),
        "customer_name":fake.name(),
        "date": date.isoformat(),
        "amount": amount,
        "description": fake.bs(),
        "account_number": fake.bban(),
        "merchant": fake.company(),
        "category": fake.word(ext_word_list=["food", "transport", "entertainment", "utilities", "shopping"])
    }

def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

def on_send_error(excp):
    log.error('I am an errback', exc_info=excp)

# Generate 10 transactions
transactions = [generate_transaction() for _ in range(100)]

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

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',

)

for transaction in transactions:
    producer.send('transactions', json.dumps(transaction).encode('utf-8')).add_callback(on_send_success).add_errback(on_send_error)

    # block until all async messages are sent
    producer.flush()

    # configure multiple retries
    producer = KafkaProducer(retries=5)
