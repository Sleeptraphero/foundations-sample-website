import json

# This file should contain a function called get_color_code().
# This function should take one argument, a color name,
# and it should return one argument, the hex code of the color,
# if that color exists in our data. If it does not exist, you should
# raise and handle an error that helps both you as a developer,
# for example by logging the request and error, and the user,
# letting them know that their color doesn't exist.

def get_color_code(color_name):
    # this is where you should add your logic to check the color.
    # Open the file at data/css-color-names.json, and return the hex code
    # The file can be considered as JSON format, or as a Python dictionary.
    
    color = open("css-color-names.json",)       #filepath maybe wrong
    colors_dict = (json.loads(color.read()))

    if color_name in colors_dict.keys():
        hex_code = color_name.value()
    else:
        hex_code = "color does not exist" 

    color.close()
    return hex_code