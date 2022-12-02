import unittest

from vending_machine import VendingMachine, CoinSlot


class TestVendingMachine_AcceptCoins(unittest.TestCase):
    """
    Test the following features:
        - Valid coins increase the balance by the value of their denomination.
        - Invalid coins do not increase the balance.
    """

    def setUp(self):
        self.vm = VendingMachine()

    def test__do_nothing__balance_is_0__display_shows_default_text(self):
        self.assertEqual(self.vm.coin_reservoir.total_coin_count, 0)
        self.assertEqual(self.vm.balance, 0)

    def test__add_a_penny__machine_rejects_penny__does_not_change_balance(self):
        balance_before_coin_added = self.vm.balance
        self.vm.coin_slot.drop_a_coin_in(
            weight=CoinSlot.AVERAGE_PENNY_WEIGHT_GRAMS)
        self.assertEqual(self.vm.balance, balance_before_coin_added)

    def test__add_nickel__machine_accepts_nickel__adds_5_cents_to_balance(self):
        balance_before_coin_added = self.vm.balance
        nickels_before_coin_added = self.vm.coin_reservoir.nickels
        self.vm.coin_slot.drop_a_coin_in(
            weight=CoinSlot.AVERAGE_NICKEL_WEIGHT_GRAMS)

        self.assertEqual(self.vm.balance, balance_before_coin_added + 0.05)
        self.assertEqual(self.vm.coin_reservoir.nickels,
                         nickels_before_coin_added + 1)

    def test__add_dime__machine_accepts_dime__adds_10_cents_to_balance(self):
        balance_before_coin_added = self.vm.balance
        dimes_before_coin_added = self.vm.coin_reservoir.dimes
        self.vm.coin_slot.drop_a_coin_in(
            weight=CoinSlot.AVERAGE_DIME_WEIGHT_GRAMS)

        self.assertEqual(self.vm.balance, balance_before_coin_added + 0.1)
        self.assertEqual(self.vm.coin_reservoir.dimes,
                         dimes_before_coin_added + 1)

    def test__add_quarter__machine_accepts_quarter__adds_25_cents_to_balance(self):
        balance_before_coin_added = self.vm.balance
        dimes_before_coin_added = self.vm.coin_reservoir.dimes
        self.vm.coin_slot.drop_a_coin_in(
            weight=CoinSlot.AVERAGE_QUARTER_WEIGHT_GRAMS)

        self.assertEqual(self.vm.balance, balance_before_coin_added + 0.25)
        self.assertEqual(self.vm.coin_reservoir.dimes,
                         dimes_before_coin_added + 1)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
