class VendingMachine:

    INSERT_COIN = 'Insert Coin'
    CHANGE = 2.00

    # Note that pennies are not accepted
    ACCEPTED_COINS = {
        'quarter': 0.25,
        'nickel': 0.05,
        'dime': 0.10
    }

    # cola for $1.00, chips for $0.50, and candy for $0.65.
    PRODUCTS = ['cola', 'chips', 'candy']
    PRICES = {
        'cola': 1.0,
        'chips': 0.50,
        'candy': 0.65
    }
    INVENTORY = {
        'cola': 3,
        'chips': 5,
        'candy': 9
    }

    def __init__(self):
        # money available to return change to customers
        self.change_total = self.CHANGE
        # keep track of coins inserted
        self.transaction_change = []
        # keep track of value of coins inserted
        self.transaction_total = 0
        # will display value of change_total if transaction_total > 0
        self.display = self.INSERT_COIN

    def get_product(self, product_name):
        product = {}
        product['name'] = product_name

        for k, v in self.PRICES.items():
            if product_name == k:
                product['price'] = v

        for k, v in self.INVENTORY.items():
            if product_name == k:
                product['inventory'] = v

        return product

    def product_available(self, product_name):
        product = self.get_product(product_name)
        return product['inventory'] > 0

    def insert_coin(self, coin):
        if coin in self.ACCEPTED_COINS.keys():
            self.transaction_total += self.ACCEPTED_COINS[coin]
            self.transaction_change.append(coin)
