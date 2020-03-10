from sample import fizz_buzz

def test_basics():
    assert fizz_buzz(3) == "Fizz"
    assert fizz_buzz(5) == "Buzz"
    assert fizz_buzz(0) == "FizzBuzz"
    assert fizz_buzz("string") == 0
    assert fizz_buzz(1) == 1

def test_divisible_by_three():
    assert fizz_buzz(6) == "Fizz"
    assert fizz_buzz(-6) == "Fizz"
    assert fizz_buzz(9) == "Fizz"
    assert fizz_buzz(-9) == "Fizz"
    assert fizz_buzz(12) == "Fizz"
    assert fizz_buzz(-12) == "Fizz"

def test_divisible_by_five():
    assert fizz_buzz(10) == "Buzz"
    assert fizz_buzz(-10) == "Buzz"
    assert fizz_buzz(20) == "Buzz"
    assert fizz_buzz(-20) == "Buzz"
    assert fizz_buzz(40) == "Buzz"
    assert fizz_buzz(-40) == "Buzz"

def test_divisible_by_both():
    assert fizz_buzz(30) == "FizzBuzz"
    assert fizz_buzz(-30) == "FizzBuzz"
    assert fizz_buzz(45) == "FizzBuzz"
    assert fizz_buzz(-45) == "FizzBuzz"
    assert fizz_buzz(60) == "FizzBuzz"
    assert fizz_buzz(-60) == "FizzBuzz"

def test_dibisible_by_other():
    assert fizz_buzz(1) == 1
    assert fizz_buzz(-1) == -1
    assert fizz_buzz(2) == 2
    assert fizz_buzz(-2) == -2

def test_divisible_by_string():
    assert fizz_buzz('a') == 0
    assert fizz_buzz('b') == 0
    assert fizz_buzz('c') == 0
    assert fizz_buzz('string') == 0
    
def test_extensively():
    high = 1_000_000
    fizzbuzz = range(0, high + 1, 15)
    fizz = range(0, high + 1, 3)
    buzz = range(0, high + 1, 5)
    other = range(high + 1)

    for i in fizzbuzz:
        assert fizz_buzz(i) == "FizzBuzz"
        assert fizz_buzz(-i) == "FizzBuzz"

    for i in fizz:
        if i not in fizzbuzz:
            assert fizz_buzz(i) == "Fizz"
            assert fizz_buzz(-i) == "Fizz"
    
    for i in buzz:
        if i not in fizzbuzz:
            assert fizz_buzz(i) == "Buzz"
            assert fizz_buzz(-i) == "Buzz"

    for i in other:
        if i not in fizz:
            if i not in buzz:
                assert fizz_buzz(i) == i
                assert fizz_buzz(-i) == -i

    for i in other:
        if chr(i).isalpha():
            assert fizz_buzz(chr(i)) == 0
