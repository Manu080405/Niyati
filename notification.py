import csv
import uuid
from datetime import datetime
from file_setup import notifications_file

class Notification:
    @staticmethod
    def send(acc_no, message):
        with open(notifications_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([str(uuid.uuid4())[:8],
                             acc_no,
                             message,
                             datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
        print("Notification:", message)
