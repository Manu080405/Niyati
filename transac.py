import csv
import uuid
from datetime import datetime
from file_setup import transactions_file

class Transaction:
    def __init__(self, acc_no, amount, t_type):
        self.transaction_id = str(uuid.uuid4())[:8]
        self.acc_no = acc_no
        self.amount = amount
        self.t_type = t_type
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.status = "SUCCESS"

    def save(self):
        with open(transactions_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([self.transaction_id,
                             self.acc_no,
                             self.t_type,
                             self.amount,
                             self.date,
                             self.status])
