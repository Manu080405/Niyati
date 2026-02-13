import csv
import os
from datetime import datetime
import uuid

accounts_file = "accounts.csv"
transactions_file = "transactions.csv"
notifications_file = "notifications.csv"

# ================= FILE CREATION ================= #
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
            writer.writerow(["transaction_id", "account_number", "type", "amount", "date", "status"])

    if not os.path.exists(notifications_file):
        with open(notifications_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["notification_id", "account_number", "message", "date"])


# ================= ACCOUNT VALIDATION ================= #
class AccountValidation:
    @staticmethod
    def get_account(acc_no):
        with open(accounts_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["account_number"] == acc_no and row["status"] == "active":
                    return row
        return None


# ================= BALANCE MANAGEMENT ================= #
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
            writer = csv.DictWriter(f, fieldnames=["account_number","name","balance","status"])
            writer.writeheader()
            writer.writerows(rows)


# ================= BASE TRANSACTION CLASS ================= #
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
            writer.writerow([self.transaction_id, self.acc_no,
                             self.t_type, self.amount,
                             self.date, self.status])


# ================= NOTIFICATION MODULE ================= #
class Notification:
    @staticmethod
    def send(acc_no, message):
        with open(notifications_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([str(uuid.uuid4())[:8], acc_no,
                             message, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
        print("Notification:", message)


# ================= FRAUD DETECTION MODULE ================= #
class FraudDetection:
    @staticmethod
    def check(amount):
        if amount > 50000:   # Simple rule for beginners
            print("⚠ Warning: High value transaction detected!")


# ================= DEPOSIT MODULE ================= #
class Deposit(Transaction):
    def process(self):
        acc = AccountValidation.get_account(self.acc_no)
        if not acc:
            print("Invalid account")
            return

        if self.amount <= 0:
            print("Invalid deposit amount")
            return

        FraudDetection.check(self.amount)

        new_balance = float(acc["balance"]) + self.amount
        BalanceManagement.update_balance(self.acc_no, new_balance)

        self.save()
        Notification.send(self.acc_no,
            f"Deposited {self.amount}. New Balance: {new_balance}")


# ================= WITHDRAWAL MODULE ================= #
class Withdrawal(Transaction):
    def process(self):
        acc = AccountValidation.get_account(self.acc_no)
        if not acc:
            print("Invalid account")
            return

        if self.amount <= 0:
            print("Invalid withdrawal amount")
            return

        if float(acc["balance"]) < self.amount:
            print("Insufficient balance")
            return

        FraudDetection.check(self.amount)

        new_balance = float(acc["balance"]) - self.amount
        BalanceManagement.update_balance(self.acc_no, new_balance)

        self.save()
        Notification.send(self.acc_no,
            f"Withdrawn {self.amount}. New Balance: {new_balance}")


# ================= FUND TRANSFER MODULE ================= #
class FundTransfer:
    @staticmethod
    def transfer(sender, receiver, amount):
        s_acc = AccountValidation.get_account(sender)
        r_acc = AccountValidation.get_account(receiver)

        if not s_acc or not r_acc:
            print("Invalid sender or receiver")
            return

        if float(s_acc["balance"]) < amount:
            print("Insufficient balance")
            return

        FraudDetection.check(amount)

        BalanceManagement.update_balance(sender,
            float(s_acc["balance"]) - amount)

        BalanceManagement.update_balance(receiver,
            float(r_acc["balance"]) + amount)

        Transaction(sender, amount, "TRANSFER_DEBIT").save()
        Transaction(receiver, amount, "TRANSFER_CREDIT").save()

        Notification.send(sender, f"Transferred {amount} to {receiver}")
        Notification.send(receiver, f"Received {amount} from {sender}")


# ================= TRANSACTION HISTORY ================= #
class TransactionHistory:
    @staticmethod
    def view(acc_no):
        with open(transactions_file, "r") as f:
            reader = csv.DictReader(f)
            print("\nTransaction History:")
            for row in reader:
                if row["account_number"] == acc_no:
                    print(row)


# ================= TRANSACTION REVERSAL ================= #
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


# ================= TRANSACTION REPORT ================= #
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


# ================= MAIN MENU ================= #
if __name__ == "__main__":
    create_files()

    while True:
        print("\n===== ABC BANKING SYSTEM =====")
        print("1 Deposit")
        print("2 Withdraw")
        print("3 Transfer")
        print("4 History")
        print("5 Reverse Transaction")
        print("6 Report")
        print("7 Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            acc = input("Account No: ")
            amt = float(input("Amount: "))
            Deposit(acc, amt, "DEPOSIT").process()

        elif ch == "2":
            acc = input("Account No: ")
            amt = float(input("Amount: "))
            Withdrawal(acc, amt, "WITHDRAW").process()

        elif ch == "3":
            s = input("Sender: ")
            r = input("Receiver: ")
            amt = float(input("Amount: "))
            FundTransfer.transfer(s, r, amt)

        elif ch == "4":
            acc = input("Account No: ")
            TransactionHistory.view(acc)

        elif ch == "5":
            tid = input("Transaction ID: ")
            TransactionReversal.reverse(tid)

        elif ch == "6":
            TransactionReport.generate()

        elif ch == "7":
            break

        else:
            print("Invalid choice")
