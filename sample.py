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

    # Extensive test
    high = 1_000_000
    fizzbuzz = range(0, high + 1, 15)
    fizz = range(0, high + 1, 3)
    buzz = range(0, high + 1, 5)

    for i in fizzbuzz:
        assert fizz_buzz(i) == "FizzBuzz"

    for i in fizz:
        if i not in fizzbuzz:
            assert fizz_buzz(i) == "Fizz"
    
    for i in buzz:
        if i not in fizzbuzz:
            assert fizz_buzz(i) == "Buzz"

    for i in range(101):
        if i not in fizz:
            if i not in buzz:
                assert fizz_buzz(i) == i

    for i in "this is a test":
        assert fizz_buzz(i) == 0