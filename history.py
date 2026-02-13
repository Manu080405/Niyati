import csv
from file_setup import transactions_file

class TransactionHistory:
    @staticmethod
    def view(acc_no):
        with open(transactions_file, "r") as f:
            reader = csv.DictReader(f)
            print("\nTransaction History:")
            for row in reader:
                if row["account_number"] == acc_no:
                    print(row)
