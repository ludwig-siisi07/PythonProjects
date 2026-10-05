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
            elif choice == '2':
                self.handle_momopay()
            elif choice == '3':
                self.handle_airtime()
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

    def handle_momopay(self):
        print("\nMomoPay/Paybill:")
        m_id = input("Enter the 6-digit Merchant ID: ")
        merchant_name = self.wallet.merchants.get(m_id, "Unknown Merchant")
        print(f"Proceed to make payment to merchant, {merchant_name}")
        amount = float(input("Enter the amount to pay: "))
        pin = input("Enter your MOMO PIN to authorize: ")
        success, msg = self.wallet.momo_pay(m_id, amount, pin)
        print(msg)

    def handle_airtime(self):
        print("\nAirtime and Bundles:\n1. Buy Airtime\n2. Buy Bundles")
        if input("Enter your choice: ") == '2':
            print("\nBundles:\n1. GHC 5 (280 MB)\n2. GHC 10 (667 MB)\n3. GHC 100 (10 GB)\n4. Flexi-Bundle (GHS 0 - GHS 400)")
            if input("Choose your bundle type: ") == '4':
                amount = float(input("Enter amount to purchase: "))
                success, msg = self.wallet.buy_flexi_bundle(amount)
                print(msg)