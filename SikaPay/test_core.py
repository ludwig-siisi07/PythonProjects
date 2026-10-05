import unittest
from sikapay.core import SikaPayWallet

class TestSikaPayWallet(unittest.TestCase):
    def setUp(self):
        self.wallet = SikaPayWallet()
        self.wallet.customers = {"0591847222": "ASARE, Solomon"}
        self.wallet.merchants = {"558032": "ALL IS WELL BAKERIES"}

    def test_transfer_money(self):
        success, msg = self.wallet.transfer_money("0591847222", 50, "7290")
        self.assertTrue(success)
        self.assertIn("949", msg) 

    def test_momo_pay(self):
        success, msg = self.wallet.momo_pay("558032", 100, "7290")
        self.assertTrue(success)
        self.assertIn("899", msg) 

    def test_buy_flexi_bundle(self):
        success, msg = self.wallet.buy_flexi_bundle(15)
        self.assertTrue(success)
        self.assertIn("840.6", msg) 

if __name__ == '__main__':
    unittest.main()