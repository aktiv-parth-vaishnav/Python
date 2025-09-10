from datetime import datetime


def calculate_age(birth_year, current_year):
    """
    this method calculate age in year  from current year

    return year
    """
    if birth_year == current_year:
        return 0
    elif birth_year > current_year:
        return print("please enter a valid year your birthday year must not greater than current year")

    return 1 + calculate_age(birth_year + 1, current_year)


def find_leap_years(start_year, end_year, leap_years=None):
    """
    this method return list of leapyear form curent year

    return list
    """
    if leap_years is None:
        leap_years = []

    if start_year > end_year:
        return leap_years

    if (start_year % 4 == 0 and (start_year % 400 == 0 or start_year % 100 != 0)):
        leap_years.append(start_year)

    return find_leap_years(start_year + 1, end_year, leap_years)


birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")

birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
birth_year = birthdate.year

today = datetime.today()
current_year = today.year

age = calculate_age(birth_year, current_year)
leap_years_list = find_leap_years(birth_year + 1, current_year)

# Output results
print(f"Your current age is: {age} years")
print("Leap years after your birth year are:")
print(leap_years_list)
