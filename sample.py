def fizz_buzz(integer):
    # if integer % 3 == 0 and integer % 5 == 0:
    #     return "FizzBuzz"
    # elif integer % 5:
    #     return "Buzz"
    # elif integer % 5:
    #     return "Fizz"
    return integer
    
def test_fizz_buzz():
    assert fizz_buzz(0) == 0
    assert fizz_buzz(3) == "Buzz"
    assert fizz_buzz(5) == "Fizz"
    assert fizz_buzz(15) == "FizzBuzz"
    
    assert fizz_buzz("lol") == 0
    assert fizz_buzz(2) == 2
    assert fizz_buzz(7) == 7
    
    assert fizz_buzz(6) == "Buzz"
    assert fizz_buzz(9) == "Buzz"
    assert fizz_buzz(12) == "Buzz"

    assert fizz_buzz(10) == "Fizz"
    assert fizz_buzz(20) == "Fizz"
    assert fizz_buzz(40) == "Fizz"

    assert fizz_buzz(30) == "FizzBuzz"
    assert fizz_buzz(45) == "FizzBuzz"
    assert fizz_buzz(60) == "FizzBuzz"