list_30_days = ['April', 'June', 'September', 'November']
list_31_days = ['January', 'March', 'May', 'July', 'August', 'October', 'December']


month = input("Please enter a month (in text format):\n").capitalize()
if month not in list_30_days and month not in list_31_days and month != "February":
    print("Entered value is invalid.")
    month = input("Please enter a valid month in text format:\n").capitalize()
if month not in list_30_days and month not in list_31_days:
    year = input("Please enter a year (4 digits):\n")
    if year.isdigit() is False:
        print("Entered value is invalid.")
        year = input("Please enter a valid year (4 digits):\n")
    year = int(year)


def is_leap_year(int):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Number of days: 29.")
            else:
                print("Number of days: 28.")
        else:
            print("Number of days: 29.")
    else:
        print("Number of days: 28.")


if month in list_30_days:
    print("Number of days: 30.")
elif month in list_31_days:
    print("Number of days: 31.")
else:
    is_leap_year(year)










