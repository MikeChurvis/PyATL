# Vending Machine System Test Design

def validate_coin(weight_grams: float, diameter_mm: float, thickness_mm: float)
- return CoinType.NICKEL
- return CoinType.DIME
- return CoinType.QUARTER
- raise InvalidCoinType

def reject_coin_in_slot()
def accept_coin_in_slot()

def add_coin_to_balance(coin_type: CoinType)

CoinType
- Penny
- Nickel
- Dime
- Quarter

def select_product(product_code: str)
- return ProductData
- raise ProductOutOfStock

def put_coin_in_coin_slot(vending_machine, coin_data: dict)

def press_button(vending_machine, button_code: ButtonCode)

ButtonCode
- Cola
- Chips
- Candy
- Cancel
