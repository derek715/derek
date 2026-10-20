# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.


def star_names(targets):
    # Iterates through targets and prints the name of each star (nested dictionary names).
    for star in targets:
        print(star)
star_names(targets)
# 2) Write a function that uses a loop to print the name of each star with its spectral type.

def star_and_spectral_type(targets):
    # Iterates through targets and prints the star name with the value of the "Spectral Type" key.
    for star in targets:
        print(f"Star: {star}; Spectral Type: {targets[star]["Spectral Type"]}")
star_and_spectral_type(targets)
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.

def magnitudes(targets):
    # Iterates through each target, checks if magnitude is greater than 0.1. If it is, adds a copy of the target to the new dictionary {stars_grater_mag}, otherwise skips that target.
    stars_greater_mag = {}
    for star_name, star in targets.items():
        mag = star["Magnitude"]
        if mag > 0.1:
            stars_greater_mag[star_name] = star
        else:
            continue
    return stars_greater_mag
stars_greater_mag = magnitudes(targets)
print(magnitudes(targets))

# 4) Look up another target, add all the necessary information to the targets list. 

targets["Arcturus"] = {
    "RA": "14h 15m 40s",
    "Dec": "+19° 10′ 57″",
    "Magnitude": -0.30,
    "Spectral Type": "K1.5 III"
}
print(f"'Targets' after adding Arcturus:\n{targets}, \n")

# 5) Write a function that finds the brightest star whose Declination is closest to 20°.

def closest_brightest_star(targets):
    # Finds the star closest to 20° Dec., if two are equally close, chooses the brightest.
    smallest_difference = float("inf") # Starting value for difference from 20°, initially set to infinity since zero would be a star at 20° Dec.
    brightest_mag = float("inf") # Starting value for magnitude, initially set to inifinity since smaller visual magnitude = brighter.
    name_of_star = None
    for star_name, star in targets.items():

        dec_string = star["Dec"]
        dec_string = (dec_string # Gets rid of degrees / arcminutes / arcseconds symbols.
        .replace("°", "") 
        .replace("′", "")
        .replace("″", "")
        .replace("−", "-") # Replaces unicode minus symbol with hyphen-minus symbol.
        )
        dec_parts = dec_string.split() # Splits string into a list of substrings ['degrees', 'arcminutes', 'arcseconds']
        # print(dec_parts)

        degrees = float(dec_parts[0]) # Converts the first substring string to a float, then assigns to variable 'degrees'.
        minutes = float(dec_parts[1]) # " " second " " 'minutes'
        seconds = float(dec_parts[2]) # " " third " " 'seconds'

        if degrees >= 0: # Checks whether float(degrees) is positive or negative: converts to a decimal value of dec. accordingly.
            decimal_degrees = degrees + minutes / 60 + seconds / 3600
        else:
            decimal_degrees = degrees - minutes / 60 - seconds / 3600

        difference = abs(decimal_degrees - 20) # Absolute difference, in degrees, (rounded to 3 decimal places) between target dec. and 20°

        if difference < smallest_difference: # Checks whether current difference is less than the previous, if so reassigns to the current target. 
            smallest_difference = difference
            brightest_mag = star["Magnitude"]
            name_of_star = star_name

        elif difference == smallest_difference: # Checks whether the current difference is equal to the previous.
            if star["Magnitude"] < brightest_mag: # If yes, checks whether the current magnitude is less than (brigher) than the current, if so reassigns to the brighter of the two targets.
                brightest_mag = star["Magnitude"] 
                name_of_star = star_name

    return f"{name_of_star} is the closest star from targets at Dec: {star["Dec"]} (a difference of ~ {smallest_difference:.3f}° from 20°) with visual magnitude: {brightest_mag}"
print(closest_brightest_star(targets))

# 6) What is your favorite constellation?
    # Orion.