import csv
from file_setup import accounts_file

class AccountValidation:
    @staticmethod
    def get_account(acc_no):
        with open(accounts_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["account_number"] == acc_no and row["status"] == "active":
                    return row
        return None
