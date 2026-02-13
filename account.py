import csv
import os

accounts_file = "accounts.csv"
transactions_file = "transactions.csv"
notifications_file = "notifications.csv"

class FileSetup:
    @staticmethod
    def create_files():
        if not os.path.exists(accounts_file):
            with open(accounts_file, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["account_number", "name", "balance", "status"])
                writer.writerow(["1001", "John", "10000", "active"])
                writer.writerow(["1002", "Adi", "8000", "active"])

        if not os.path.exists(transactions_file):
            with open(transactions_file, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["transaction_id", "account_number", "type", "amount", "date", "status"])

        if not os.path.exists(notifications_file):
            with open(notifications_file, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["notification_id", "account_number", "message", "date"])
