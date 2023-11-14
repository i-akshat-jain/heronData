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


def is_valid_transaction(transaction):
    # Check if the transaction dictionary contains all necessary keys
    required_keys = ['description', 'amount', 'date']
    return all(key in transaction for key in required_keys)

def load_transactions_from_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        json_transactions = data.get("transactions", [])
        return [Transaction(**transaction) for transaction in json_transactions if is_valid_transaction(transaction)]

def main():
    file_path = "example.json"
    transactions = load_transactions_from_json(file_path)

    if not transactions:
        print("No valid transactions found.")
        return
    result = identify_recurring_transactions(transactions)

    recurring_transactions_list = []

    for key, dates in result.items():
        description, amount = key.split('_')
        amount = float(amount)

        # Calculated the approximate date for the next month's transaction
        last_date = max(dates, key=lambda x: datetime.strptime(x, '%Y-%m-%d'))
        last_date = datetime.strptime(last_date, '%Y-%m-%d')
        # Assuming a month is approximately 30 days
        next_date = last_date + timedelta(days=30)  

        # Created a dictionary for the recurring transaction
        recurring_transaction = {
            'name': description,
            'amount': amount,  
            'pastTransactions': [date for date in sorted(dates, reverse=True)],
            'nextTransactionDate': next_date.strftime('%Y-%m-%d'),
        }

        # Append the dictionary to the list
        recurring_transactions_list.append(recurring_transaction)

    # Created dictionary with the list of recurring transactions
    result_json = {'RecurringTransactions': recurring_transactions_list}


    print(json.dumps(result_json, indent=2))


if __name__ == "__main__":
    main()