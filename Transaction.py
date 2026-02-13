import csv
import os
from datetime import datetime
import uuid

accounts_file = "accounts.csv"
transactions_file = "transactions.csv"
notifications_file = "notifications.csv"


def create_files():
    if not os.path.exists(accounts_file):
        with open(accounts_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["account_number", "name", "balance", "status"])
            writer.writerow(["1001", "John", "10000", "active"])
            writer.writerow(["1002", "Mary", "8000", "active"])

    if not os.path.exists(transactions_file):
        with open(transactions_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["transaction_id", "account_number", "type", "amount", "date"])

    if not os.path.exists(notifications_file):
        with open(notifications_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["notification_id", "account_number", "message", "date"])


def get_account(account_number):
    with open(accounts_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["account_number"] == account_number and row["status"] == "active":
                return row
    return None


def update_balance(account_number, new_balance):
    rows = []
    with open(accounts_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["account_number"] == account_number:
                row["balance"] = str(new_balance)
            rows.append(row)

    with open(accounts_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["account_number", "name", "balance", "status"])
        writer.writeheader()
        writer.writerows(rows)


def add_transaction(account_number, t_type, amount):
    with open(transactions_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            str(uuid.uuid4())[:8],
            account_number,
            t_type,
            amount,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ])


def deposit(account_number, amount):
    if amount <= 0:
        print("Amount must be positive")
        return

    account = get_account(account_number)
    if not account:
        print("Invalid or inactive account")
        return

    new_balance = float(account["balance"]) + amount
    update_balance(account_number, new_balance)
    add_transaction(account_number, "DEPOSIT", amount)

    print("Deposit successful")
    print("New Balance:", new_balance)


def withdraw(account_number, amount):
    if amount <= 0:
        print("Amount must be positive")
        return

    account = get_account(account_number)
    if not account:
        print("Invalid or inactive account")
        return

    if float(account["balance"]) < amount:
        print("Insufficient balance")
        return

    new_balance = float(account["balance"]) - amount
    update_balance(account_number, new_balance)
    add_transaction(account_number, "WITHDRAW", amount)

    print("Withdrawal successful")
    print("New Balance:", new_balance)


def check_balance(account_number):
    account = get_account(account_number)
    if not account:
        print("Invalid or inactive account")
        return

    print("Account Holder:", account["name"])
    print("Current Balance:", account["balance"])


# ================= MAIN PROGRAM ================= #

if __name__ == "__main__":
    create_files()

    while True:
        print("\n===== Banking System =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            acc = input("Enter account number: ")
            try:
                amt = float(input("Enter amount to deposit: "))
                deposit(acc, amt)
            except ValueError:
                print("Invalid amount")

        elif choice == "2":
            acc = input("Enter account number: ")
            try:
                amt = float(input("Enter amount to withdraw: "))
                withdraw(acc, amt)
            except ValueError:
                print("Invalid amount")

        elif choice == "3":
            acc = input("Enter account number: ")
            check_balance(acc)

        elif choice == "4":
            print("Exiting system...")
            break

        else:
            print("Invalid choice. Try again.")
