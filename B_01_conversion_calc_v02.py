# Generates headings
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

    print('''
Instructions:
- Enter a measurement(or abbreviation) that you are starting with.
- Then enter another measurement to convert to.
- Then enter the amount of the starting unit.
- To exit enter "xxx".
- The measurements are in the most common values in distance, time, mass and volume.
- The metric system is used and distance is spelt "meters".
- Have fun :)
    ''')


# checks numbers
def num_check(question):
    error = "Please enter a whole number that is more than 0\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # Ask user for a number
            response = float(response)

            # enter a number that is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# merges all dictionaries
def merge(dict1, dict2, dict3, dict4):
    # merges all dictionaries
    res = {**dict1, **dict2, **dict3, **dict4}
    return res


# checks units are valid
def unit_checker(question, every_unit):
    error_message = "Enter a valid unit"
    while True:
        response = input(question).lower()

        if response == "xxx":
            return response
        # check if the units are valid
        for item in every_unit:
            if response in item:
                # set unit to the first item of the 'valid' list
                response = item[0]

                return response
        print(error_message)


def dict_checker(starting_unit, ending_unit):
    valid_units = "pass"

    if starting_unit in mass_dict and ending_unit in mass_dict:
        pass

    elif starting_unit in distance_dict and ending_unit in distance_dict:
        pass

    elif starting_unit in time_dict and ending_unit in time_dict:
        pass

    elif starting_unit in volume_dict and ending_unit in volume_dict:
        pass

    elif starting_unit == ending_unit:
        print("\nPlease pick different measurements")
        valid_units = "fail"

    # if the response is invalid output error
    else:
        print("\nPlease pick units that measure the same measurement.\n")
        valid_units = "fail"

    return valid_units


distance_dict = {
    "mm": 1000000,
    "cm": 100000,
    "m": 1000,
    "km": 1
}


time_dict = {
    "ms": 36000,
    "s": 3600,
    "min": 60,
    "hr": 1
}

mass_dict = {
    "mg": 1000000000,
    "g": 1000000,
    "kg": 1000,
    "t": 1
}

volume_dict = {
    "ml": 1000,
    "l": 1
}

# All dictionaries combined
all_dicts = merge(distance_dict, time_dict, mass_dict, volume_dict)

# Lists used to check users enter a unit of mass

# Valid mass units
valid_tonne = ['t', 'tonne', 'tonnes']
valid_kg = ['kg', 'kilogram', 'kilograms']
valid_g = ['g', 'gram', 'grams']
valid_mg = ['mg', 'milligram', 'milligrams']

# Valid time units
valid_seconds = ['s', 'sec', 'second', 'seconds']
valid_min = ['min', 'minute', 'minutes', 'mins']
valid_hr = ['hr', 'hrs', 'hour', 'hours', 'h']

# Valid distance units
valid_km = ['km', 'kilometer', 'kilometers']
valid_m = ['m', 'meter', 'meters']
valid_cm = ['cm', 'centimeter', 'centimeters']
valid_mm = ['mm', 'millimeter', 'millimeters']

# Valid volume units
valid_l = ['l', 'litre', 'litres']
valid_ml = ['ml', 'millilitre', 'millilitres']

mass_all = [valid_kg, valid_tonne, valid_g, valid_mg]
time_all = [valid_seconds, valid_min, valid_hr]
distance_all = [valid_km, valid_m, valid_cm, valid_mm]
volume_all = [valid_l, valid_ml]

# put all the lists into a master list
all_units = time_all + mass_all + distance_all + volume_all

# Main routine goes here

# Display name
print(statement_generator("Ezra's Conversion Calculator", "*"))

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue. ")

if want_instructions == "":
    instructions("Instructions", "*")

while True:

    # get units and check them
    # classifies units
    from_unit = unit_checker("What unit do you have? ", all_units)
    if from_unit == "xxx":
        break

    to_unit = unit_checker("What unit do you want? ", all_units)
    if to_unit == "xxx":
        break

    same_domain = dict_checker(from_unit, to_unit)
    if same_domain == "fail":
        continue

    # get value of from_unit
    amount = num_check("Enter the value of the starting unit: ")
    if amount == "xxx":
        break

    # multiply to get our standard value
    multiply_by = all_dicts[to_unit]
    standard = amount * multiply_by

    # divide to get our desired value
    divide_by = all_dicts[from_unit]
    answer = standard / divide_by

    # answer
    print(f"There are {answer} {to_unit} in {amount} {from_unit}\n")

print("\nThank you for using Conversion Calculator. :)")
