"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    print(n)
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# TODO: 1. write down what you think the output of this will be,
#output will be 3 as it just adds together the results of the % operator
# TODO: 2. use the debugger to step through and see what's actually happening
print(do_it(5))

def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n > 0:
        print(n ** 2)
        return do_something(n - 1)
    return 0


# TODO: 3. write down what you think the output of this will be,
# output = 16, 9, 4, 1
# TODO: 4. use the debugger to step through and see what's actually happening
do_something(4)

# TODO: 5. fix do_something() so that it works the way it probably should :)
