import json
from difflib import SequenceMatcher
from datetime import datetime, timedelta


# Define the Transaction class
class Transaction:
    def __init__(self, description, amount, date):
        self.description = description
        self.amount = amount
        self.date = date

    def as_dict(self):
        return {
            'description': self.description,
            'amount': self.amount,
            'date': self.date
        }


def calculate_similarity(str1, str2):
    return SequenceMatcher(None, str1, str2).ratio()

# Function to identify recurring transactions
def identify_recurring_transactions(transactions):
    recurring_transactions = {}

    for transaction in transactions:
        for key in recurring_transactions:
            stored_description, stored_amount = key.split('_')
            description_similarity = calculate_similarity(
                transaction.description, stored_description)

            if description_similarity > 0.66 and transaction.amount == float(stored_amount):
                recurring_transactions[key].append(transaction.date)
                break
        else:
            key = f"{transaction.description}_{transaction.amount}"
            recurring_transactions[key] = [transaction.date]

    recurring_transactions = {
        key: dates for key, dates in recurring_transactions.items() if len(dates) > 1
    }

    return recurring_transactions


# Read transaction data from a JSON file
with open("example.json", "r") as file:
    data = json.load(file)

# Assuming data is in the format of your provided JSON
json_transactions = data["transactions"]

# Convert JSON transactions to Transaction objects
transactions = [Transaction(**transaction)
                    for transaction in json_transactions]

# Identify recurring transactions
result = identify_recurring_transactions(transactions)

recurring_transactions_list = []

for key, dates in result.items():
    description, amount = key.split('_')
    amount = float(amount)

    # Calculate the approximate date for the next month's transaction
    last_date = max(dates, key=lambda x: datetime.strptime(x, '%Y-%m-%d'))
    last_date = datetime.strptime(last_date, '%Y-%m-%d')
    next_date = last_date + timedelta(days=30)  # Assuming a month is approximately 30 days

    # Create a dictionary for the recurring transaction
    recurring_transaction = {
        'name': description,
        'amount': amount,  
        'pastTransactions': [date for date in sorted(dates, reverse=True)],
        'nextTransactionDate': next_date.strftime('%Y-%m-%d'),
    }

    # Append the dictionary to the list
    recurring_transactions_list.append(recurring_transaction)

# Create a dictionary with the list of recurring transactions
result_json = {'RecurringTransactions': recurring_transactions_list}

# Print the result in JSON format
print(json.dumps(result_json, indent=2))
