import csv
from file_setup import accounts_file

class BalanceManagement:
    @staticmethod
    def update_balance(acc_no, new_balance):
        rows = []
        with open(accounts_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["account_number"] == acc_no:
                    row["balance"] = str(new_balance)
                rows.append(row)

        with open(accounts_file, "w", newline="") as f:
            writer = csv.DictWriter(f,
                fieldnames=["account_number","name","balance","status"])
            writer.writeheader()
            writer.writerows(rows)
