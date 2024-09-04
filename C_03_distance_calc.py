# dictionary for distance units
distance_dict = {
    "mm": 1000,
    "cm": 100,
    "m": 1,
    "km": 0.001
}

# Ask user for units
starting_unit = input("Enter the unit do you want to convert from: ").lower()
ending_unit = input("Enter the unit you want to end up with: ").lower()
amount = float(input("Enter the value of the starting unit: "))

# multiply to get our standard value
multiply_by = distance_dict[ending_unit]
standard = amount * multiply_by


# divide to get our desired value
divide_by = distance_dict[starting_unit]
answer = standard / divide_by

print(f"There are {answer} {ending_unit} in {amount} {starting_unit}")
