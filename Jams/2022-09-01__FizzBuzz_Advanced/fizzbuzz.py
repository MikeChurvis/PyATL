def generate_fizzbuzz_output_from_int(i: int) -> str:
    """Solve the FizzBuzz for a given integer.
    
    Returns "Fizz" if `i` is evenly divisible by 3 or contains 3 as a digit.
    Returns "Buzz" if `i` is evenly divisible by 5 or contains 5 as a digit.
    Returns "FizzBuzz" if `i` matches both of the above conditions.
    Returns `i` as a string if `i` matches none of the above conditions.
    """
    output = ""
    
    if i % 3 == 0 or "3" in str(i):
        output += "Fizz"
        
    if i % 5 == 0 or "5" in str(i):
        output += "Buzz"
        
    if len(output) == 0:
        output = str(i)
        
    return output


# if __name__ == "__main__":
#     for i in range(1, 101):
#         output = generate_fizzbuzz_output_from_int(i)
#         print(output)
