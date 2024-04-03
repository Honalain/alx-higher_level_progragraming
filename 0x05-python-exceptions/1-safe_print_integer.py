#!/usr/bin/python3

def safe_print_integer(value):
    """Prints an integer using "{:d}".format().

    Args:
        value: The value to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        return (False)
