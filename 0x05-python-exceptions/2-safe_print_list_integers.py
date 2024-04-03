#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x integers of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to access.

    Returns:
        The number of integers printed.
    """
    printed_count = 0

    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed_count += 1
        except (ValueError, TypeError):
            continue    
    print("")
    return (printed_count)
