from file_setup import FileSetup
from deposit import Deposit
from withdrawal import Withdrawal
from transfer import FundTransfer
from history import TransactionHistory
from reversal import TransactionReversal
from report import TransactionReport

class BankingSystem:

    @staticmethod
    def run():
        FileSetup.create_files()

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
                print("Exiting...")
                break

            else:
                print("Invalid choice")


if __name__ == "__main__":
    BankingSystem.run()
