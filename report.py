import csv
from file_setup import transactions_file

class TransactionReport:
    @staticmethod
    def generate():
        total_deposit = 0
        total_withdraw = 0

        with open(transactions_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["type"] == "DEPOSIT":
                    total_deposit += float(row["amount"])
                elif row["type"] == "WITHDRAW":
                    total_withdraw += float(row["amount"])

        print("\n===== REPORT =====")
        print("Total Deposits:", total_deposit)
        print("Total Withdrawals:", total_withdraw)
