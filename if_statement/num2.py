#!/usr/bin/python3
month = input("Enter full name of the month: ").title()
month_dictionary = {
    'January': '31 days',
    'February': '28 or 29 days',
    'March': '31 days',
    'April': '30 days',
    'May': '31 days',
    'June': '30 days',
    'July': '31 days',
    'August': '31 days',
    'September': '30 days',
    'October': '31 days',
    'November': '30 days',
    'December': '31 days'
}
num_of_days = month_dictionary.get(month)
print(f"The month of {month} has {num_of_days}.")
