def is_armstrong_number(num):
    # Convert the number to a string to easily get digits
    num_str = str(num)
    # Get the number of digits
    num_digits = len(num_str)

    sum_of_powers = 0
    # Iterate through each digit
    for digit_char in num_str:
        digit = int(digit_char)
        sum_of_powers += digit ** num_digits
    if sum_of_powers == num:
        print("It Is Armstrong Numbr")
    else:
        print("It Is Not Armstrong")


num=int(input("enter a number: "))
is_armstrong_number(num)
