def FizzBuzz(integer):
    if integer % 3 == 0 and integer % 5 == 0:
        return "FizzBuzz"
    elif integer % 5:
        return "Buzz"
    elif integer % 5:
        return "Fizz"
    return integer