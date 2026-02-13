import csv
from file_setup import transactions_file

class TransactionReversal:
    @staticmethod
    def reverse(transaction_id):
        rows = []
        found = False

        with open(transactions_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["transaction_id"] == transaction_id:
                    row["status"] = "REVERSED"
                    found = True
                rows.append(row)

        if found:
            with open(transactions_file, "w", newline="") as f:
                writer = csv.DictWriter(f,
                    fieldnames=["transaction_id","account_number","type","amount","date","status"])
                writer.writeheader()
                writer.writerows(rows)
            print("Transaction Reversed")
        else:
            print("Transaction not found")
