def fizz_buzz(integer):
    # if integer % 3 == 0 and integer % 5 == 0:
    #     return "FizzBuzz"
    if integer % 5 == 0:
         return "Buzz"
    elif integer % 3 == 0:
        return "Fizz"
    return integer
    
def test_fizz_buzz():
    assert fizz_buzz(1) == 1
    assert fizz_buzz(3) == "Fizz"
    assert fizz_buzz(5) == "Buzz"
    assert fizz_buzz(15) == "FizzBuzz"
    
    assert fizz_buzz("lol") == 0
    assert fizz_buzz(2) == 2
    assert fizz_buzz(7) == 7
    
    assert fizz_buzz(6) == "Fizz"
    assert fizz_buzz(9) == "Fizz"
    assert fizz_buzz(12) == "Fizz"

    assert fizz_buzz(10) == "Buzz"
    assert fizz_buzz(20) == "Buzz"
    assert fizz_buzz(40) == "Buzz"

    assert fizz_buzz(30) == "FizzBuzz"
    assert fizz_buzz(45) == "FizzBuzz"
    assert fizz_buzz(60) == "FizzBuzz"