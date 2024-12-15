import csv
from datetime import datetime

# File to store transaction data
FILE_NAME = 'transactions.csv'

# Initialize the CSV file
def initialize_csv():
    try:
        with open(FILE_NAME, mode='x', newline='') as file:
            writer = csv.writer(file)
            # Writing headers to the CSV file
            writer.writerow(['Date', 'Category', 'Description', 'Amount'])
    except FileExistsError:
        pass  # File already exists, no need to initialize again

# Add a new transaction
def add_transaction(category, description, amount):
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), category, description, amount])
    print("Transaction added successfully.")

# View all transactions
def view_transactions():
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            print("\nTransactions:")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No transactions found. Please add a transaction first.")

# Calculate balance
def calculate_balance():
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            balance = 0.0
            for row in reader:
                balance += float(row[3])
            return balance
    except FileNotFoundError:
        return 0.0

# Main menu
def main():
    initialize_csv()
    while True:
        print("\nPersonal Financial Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. View Balance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter category (e.g., Food, Rent, Utilities): ")
            description = input("Enter description: ")
            amount = float(input("Enter amount (positive for income, negative for expense): "))
            add_transaction(category, description, amount)
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            balance = calculate_balance()
            print(f"Current Balance: ${balance:.2f}")
        elif choice == '4':
            print("Exiting tracker. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
