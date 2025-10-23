def valid_number(n):
    """
    this method check number is valid base on this condition

    The number must be 4 digits long i.e (1000 to 9999)
    The second digit of the number must be odd and the last digit must be even.
    The number must be divisible by either 8 or 5.

    return num
    """
    s = str(n)
    if not (1000 <= n <= 9999):
        return False
    if int(s[1]) % 2 == 0:
        return False
    if int(s[-1]) % 2 != 0:
        return False
    return (n % 8 == 0 or n % 5 == 0)


def extract_numbers(lst):
    """extract valid  numbers"""
    return [n for n in lst if isinstance(n, int) and valid_number(n)]


nums = [1024, 1235, 3456, 6780, 4328, 1350, 5678, 8750]
print(extract_numbers(nums))
