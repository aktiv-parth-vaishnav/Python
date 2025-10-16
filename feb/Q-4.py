from datetime import datetime, date


def days_until_next_birthday(birthdate_str):
    """
    calculate days from today to  the upcoming next birthday and
    also calculate next leapyer from current year

    """
    today = date.today()
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()

    next_birthday = date(today.year, birthdate.month, birthdate.day)

    if next_birthday < today:
        next_birthday = date(today.year + 1, birthdate.month, birthdate.day)

    return (next_birthday - today).days


def next_leap_year(current_year):
    """Find next leap year after given year
    """
    year = current_year + 1
    while True:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return year
        year += 1


birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")

days_left = days_until_next_birthday(birthdate_input)
leap_year = next_leap_year(datetime.today().year)

print(f"Days left until your next birthday: {days_left} days")
print(f"Next leap year after the current year: {leap_year}")
