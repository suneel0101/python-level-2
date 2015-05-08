from even_utils import is_even


def filter_out_odds(numbers):
    """
    Takes a list of numbers and returns
    just the evens.
    """
    evens = []
    # let's loop through all the numbers in the
    # `numbers` list
    for i in numbers:
        if is_even(i):
            evens.append(i)
    return evens