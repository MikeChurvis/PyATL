from fizzbuzz import generate_fizzbuzz_output_from_int as fizzbuzz_fn


def test__input_divisible_by_3_and_not_5__returns_fizz():
    assert fizzbuzz_fn(3) == "Fizz"


def test__input_divisible_by_5_and_not_5__returns_buzz():
    assert fizzbuzz_fn(5) == "Buzz"


def test__input_divisible_by_3_and_5__returns_fizzbuzz():
    assert fizzbuzz_fn(15) == "FizzBuzz"


def test__input_divisible_by_neither_3_nor_5__returns_input():
    assert fizzbuzz_fn(1) == "1"


def test__input_string_contains_3_and_not_5__returns_fizz():
    # 13 is the lowest int with digit 5 and not 5 that is not divisible by
    # 3 or 5.
    assert fizzbuzz_fn(13) == "Fizz"


def test__input_string_contains_5_and_not_3__returns_buzz():
    # 52 is the lowest int with digit 5 and not 3 that is not divisible by
    # 3 or 5.
    assert fizzbuzz_fn(52) == "Buzz"
    

def test__input_string_contains_3_and_5__returns_fizzbuzz():
    # 53 is the lowest int with both digits 3 and 5 that is not divisible
    # by 3 or 5.
    assert fizzbuzz_fn(53) == "FizzBuzz"
    
    
def test__input_string_contains_neither_3_nor_5__returns_input():
    assert fizzbuzz_fn(299) == "299"
