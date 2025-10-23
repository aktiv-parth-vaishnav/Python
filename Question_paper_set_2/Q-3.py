def extract_numbers(numbers):
    """
        this method return number where The number must be 4 digits long i.e (1000 to 9999)
        The first digit of the number must be odd and the last digit must be even.
        The number must be divisible by either 3 or 7.

    return result
    """
    result = []
    for num in numbers:
        if 1000 <= num <= 9999:
            num_str = str(num)
            if int(num_str[0]) % 2 != 0 and int(num_str[-1]) % 2 == 0:
                if num % 3 == 0 or num % 7 == 0:
                    result.append(num)
    return result

input_str = input("Enter a list of numbers separated by spaces: ")
numbers = [int(str) for str in input_str.split()]

result_numbers = extract_numbers(numbers)
print("Extracted numbers:", result_numbers)

