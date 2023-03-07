def find_max(numbers):
    """
    Finds the maximum number in a list of integers.

    Args:
        numbers: a list of integers

    Returns:
        The maximum number in the list.
    """
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
