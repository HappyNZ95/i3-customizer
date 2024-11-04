import argparse
import os


parser = argparse.ArgumentParser(description="A simple CLI program to customize the colours in i3wm.")
i3_config_file_path = os.path.expanduser("~/.config/i3/config")
# ArgumentParser

parser.add_argument("colour", type=str, help="the colour you want")

args = parser.parse_args()

client_focused_line = ""

#new_file_text = ""

colour_schemes = {

        "blue": {
            "client.focused": "client.focused       #7189FF#7189FF#7189FF#7189FF #C1CEFE \n"
            },
        "green": {
            "client.focused": "client.focused       #2e6f40 #2e6f40 #000000 #2e6f40 #2e6f40 \n"
            },
        "lavendar": {
            "client.focused": "client.focused       #624CAB#624CAB#624CAB #624CAB #ffffff \n"
            },

        "pywal": {
            "client.focused": "client.focused       $bg $bg $fg $bg $bg \n"
            }
        }


def isComment(line):
    if line.lstrip()[0] == "#":
        return True
    return False

def change_i3_titlebar_colours(colour):


    print(f"you have selected the {colour} scheme!")

    original_file = open(i3_config_file_path, "r")
    lines = original_file.readlines()
    new_file_text = ""

    for line in lines:
        if "client.focused" in line and "_inactive" not in line and not isComment(line):
            line = colour_schemes[colour]["client.focused"]
        
        new_file_text += line

        original_file.close()

        new_file = open(i3_config_file_path, "w")
        new_file.write(new_file_text)
        new_file.close()

change_i3_titlebar_colours(args.colour)

