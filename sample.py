def fizz_buzz(integer):
    if type(integer) != int:
        return 0
    if integer % 3 == 0 and integer % 5 == 0:
        return "FizzBuzz"
    elif integer % 5 == 0:
         return "Buzz"
    elif integer % 3 == 0:
        return "Fizz"
    return integer