def merge(dict1, dict2, dict3, dict4):
    # merges all dictionaries so we can...
    res = {**dict1, **dict2, **dict3, **dict4}
    return res


distance_dict = {
    "mm": 1000,
    "cm": 100,
    "m": 1,
    "km": 0.001
}

time_dict = {
    "ms": 0.001,
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

unit = input("Enter a measurement abbreviation: ")
next_unit = input("Enter a measurement abbreviation: ")


# Check if the units measure the same thing (distance with distance etc.)
if unit in mass_dict and next_unit in mass_dict:
    print("Both in mass_dict")

elif unit in distance_dict and next_unit in distance_dict:
    print("Both in distance_dict")

elif unit in time_dict and next_unit in time_dict:
    print("Both in time_dict")

elif unit in volume_dict and next_unit in volume_dict:
    print("Both in volume_dict")

else:
    print("Please pick units that measure the same measurement.")
