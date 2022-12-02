import unittest

from vending_machine import VendingMachine


class TestVendingMachine(unittest.TestCase):

    def setUp(self):
        self.vending_machine = VendingMachine()

    def test_vending_machine_initial_state(self):

        self.assertEqual(self.vending_machine.transaction_total, 0)
        self.assertEqual(self.vending_machine.display, 'Insert Coin')

    def test_vending_machine_available_product(self):
        self.assertTrue(self.vending_machine.product_available('cola'))

    def test_vending_machine_insert_coin(self):
        coin = 'quarter'
        self.vending_machine.insert_coin(coin)
        self.assertEqual(self.vending_machine.transaction_total, 0.25)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
