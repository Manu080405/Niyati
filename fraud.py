class FraudDetection:
    @staticmethod
    def check(amount):
        if amount > 50000:
            print("⚠ Warning: High value transaction detected!")
