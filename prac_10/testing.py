"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""
import doctest
from car import Car

def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    if n > 1 :
        return  s + ' ' + repeat_string(s, n-1)
    return s


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # TODO: 1. fix the repeat_string function above so that it passes the test
    # Hint: "-".join(["yo", "yo"] -> "yo-yo"
    print(repeat_string('yo', 2))
    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    # TODO: 2. write assert statements to show if Car sets the fuel correctly
    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these
    assert test_car.fuel == 0
    test_car = Car(fuel=10)
    assert test_car.fuel


run_tests()

# TODO: 3. Uncomment the following line and run the doctests
doctest.testmod()

# TODO: 4. Fix the failing is_long_word function
# (don't change the tests, but the function!)
print(is_long_word("Python", 6))
assert is_long_word("Python", 6)
# TODO: 5. Write and test a function to format a phrase as a sentence,
# starting with a capital and ending with a single full stop.
# Important: start with a function header and just use pass as the body
# then add doctests so that:
# 'hello' -> ''Hello.'
# 'It is an ex parrot.' -> 'It is an ex parrot.'
# and one more you decide (that's valid!)
def format_sentence(sentence):
    sentence = sentence.capitalize()
    if sentence[len(sentence)-1] != '.':
        sentence = sentence + '.'
    return "This is the formatted sentence -> {}".format(sentence)
# then write the body of the function so that the tests pass
print (format_sentence('hello'))
print(format_sentence('It is an ex parrot.'))
print(format_sentence("oh where in the world is here"))

def squares(number):
    if number > 0:
        print(number ** 2)
        squares(number - 1)
        print(number ** 2)
    else:
        print(number)

squares(6)

def pyramid(rows, height):
    if ( rows > 0):
        pyramid(rows-1, height)
        if 6 - rows > 0:
            for i in range(0, 6 - rows, 1):
               print(' ' , end = '')
        for i in range(0, rows, 1):
            print('[]', end = '')
        print()

pyramid(6, 0)