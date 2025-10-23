def is_armstrong(number):
    """
    this method take number as a argument and check
    that number is armstrong ot not

    return total
    """
    digits = str(number)
    num_digits = len(digits)
    total = 0
    for d in digits:
        total += int(d) ** num_digits
    return total == number

num = int(input("Enter an integer: "))

if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is NOT an Armstrong number.")