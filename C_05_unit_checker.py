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


# Main code
unit = (input("Unit: "))

# allows us to check if we have a valid unit
is_valid = "no"

for item in all_units:
    if unit in item:
        # set unit to the first item of the 'valid' list
        unit = item[0]
        print(f"Unit is actually {unit}")
        is_valid = "yes"

if is_valid == "no":
    print("oops - that is not valid")
