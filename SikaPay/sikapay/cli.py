from sikapay.core import SikaPayWallet

class SikaPayCLI:
    def __init__(self):
        self.wallet = SikaPayWallet()

    def run(self):
        while True:
            print("\nWelcome to Telestar Mobile Money! Please select an option:")
            print("1. Transfer Money\n2. MOMO Pay\n3. Airtime and Bundles\n4. Allow Cash Out\n6. My Wallet\n0. Exit")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.handle_transfer()
            elif choice == '0':
                break
            
            if input("\nDo you want to perform another operation? (yes/no): ").lower() != 'yes':
                break

    def handle_transfer(self):
        print("\nTransfer Money:\n1. TeleStar Network\n2. Other Networks")
        input("Enter your transfer choice: ")
        phone1 = input("Enter the recipient's TeleStar phone number (should start with 059): ")
        phone2 = input("Verify the phone number by entering it again: ")
        
        if phone1 != phone2:
            print("Numbers do not match.")
            return
            
        amount = float(input("Enter the amount to transfer: "))
        recipient_name = self.wallet.customers.get(phone1, "Unknown")
        pin = input(f"Enter your MOMO pin to authorize transfer to {recipient_name}: ")
        
        success, msg = self.wallet.transfer_money(phone1, amount, pin)
        print(msg)