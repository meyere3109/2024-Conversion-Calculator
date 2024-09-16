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
- To exit press "xxx" as the amount.
- The measurements are in the most common values in distance, time, mass and volume.
- The metric system is used and distance is spelt "meters".
- Have fun :)
    ''')


# checks numbers
def num_check(question):
    error = "Please enter a whole number that is more than 0.\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # Ask user for a number
            response = int(response)

            # enter a number that is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def merge(dict1, dict2, dict3, dict4):
    # merges all dictionaries
    res = {**dict1, **dict2, **dict3, **dict4}
    return res


def dict_checker(question, other_question, every_unit):
    while True:
        error = "Potato"
        # get the units
        starting_unit = input(question).lower()

        if starting_unit in mass_dict:
            domain = mass_dict

        elif starting_unit in volume_dict:
            domain = volume_dict

        elif starting_unit in distance_dict:
            domain = distance_dict

        elif starting_unit in time_dict:
            domain = time_dict

        else:
            print(error)

        ending_unit = input(other_question).lower()

        # allows us to check if we have a valid unit
        unit_valid = "no"
        other_valid = "no"

        # check if the units are valid
        for item in every_unit:
            if starting_unit in item:
                # set unit to the first item of the 'valid' list
                starting_unit = item[0]
                unit_valid = "yes"

            if ending_unit in item:
                # set unit to the first item of the 'valid' list
                ending_unit = item[0]
                other_valid = "yes"

        # if starting_unit == "xxx" or starting_unit == "xxx":
        #     continue

        # tell user if not valid units
        if unit_valid == "no" or other_valid == "no":
            print("That is not a valid unit.")
            dict_checker(question, other_question, every_unit)

        # Check if the units measure the same thing (distance with distance etc.)
        elif starting_unit == ending_unit:
            print("\nPlease pick different units.\n")

        elif starting_unit in mass_dict and ending_unit in mass_dict:
            print()

        elif starting_unit in distance_dict and ending_unit in distance_dict:
            print()

        elif starting_unit in time_dict and ending_unit in time_dict:
            print()

        elif starting_unit in volume_dict and ending_unit in volume_dict:
            print()

        # if the response is invalid output error
        else:
            print("\nPlease pick units that measure the same measurement.\n")
            continue

        return starting_unit, ending_unit


distance_dict = {
    "mm": 1000,
    "cm": 100,
    "m": 1,
    "km": 0.001
}

time_dict = {
    "ms": 1000,
    "s": 1,
    "min": 60,
    "h": 3600,

}

mass_dict = {
    "mg": 1000,
    "g": 1,
    "kg": 0.001,
    "t": 0.000001
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
valid_min = ['min', 'minute', 'minutes']
valid_hr = ['hr', 'hrs', 'hour', 'hours']

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
    units_involved = dict_checker("Enter the unit do you want to convert from: ", "Enter the unit you want to end up "
                                                                                  "with: ", all_units)

    # classifies units
    from_unit = units_involved[0]
    to_unit = units_involved[1]

    # get value of from_unit
    amount = num_check("Enter the value of the starting unit: ")

    # check to break
    if amount == "xxx" or to_unit == "xxx" or from_unit == "xxx":
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
