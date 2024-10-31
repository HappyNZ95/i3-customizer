import argparse
import os


parser = argparse.ArgumentParser(description="A simple CLI program to customize the colours in i3wm.")
i3_config_file_path = os.path.expanduser("~/.config/i3/config")
# ArgumentParser

parser.add_argument("colour", type=str, help="the colour you want")

args = parser.parse_args()

client_focused_line = ""

new_file_text = ""

def isComment(line):
    if line.lstrip()[0] == "#":
        return True
    return False

if args.colour == "blue":

    print("You selected the blue colour scheme!\n\n")

    original_file = open(i3_config_file_path, "r")

    lines = original_file.readlines()
    #for index, line in enumerate(lines):
    for line in lines:
        
        if "client.focused" in line and "_inactive" not in line and not isComment(line):
            line = "client.focused           #0096FF #0096FF #ffffff #0096FF ##0096FF\n"

        new_file_text += line
    
    original_file.close()

    new_file = open(i3_config_file_path, "w")
    new_file.write(new_file_text)
    new_file.close()

if args.colour == "green":

    print("You selected the green colour scheme!\n\n")

    original_file = open(i3_config_file_path, "r")

    lines = original_file.readlines()
    #for index, line in enumerate(lines):
    for line in lines:
        
        if "client.focused" in line and "_inactive" not in line:
            line = "client.focused          #2e6f40 #2e6f40 #000000 #2e6f40 #2e6f40 \n"

        new_file_text += line
    
    original_file.close()

    new_file = open(i3_config_file_path, "w")
    new_file.write(new_file_text)
    new_file.close()

if args.colour == "pywal":

    print("You selected the pywal colour scheme!\n\n")

    original_file = open(i3_config_file_path, "r")

    lines = original_file.readlines()
    #for index, line in enumerate(lines):
    for line in lines:
        
        if "client.focused" in line and "_inactive" not in line:
            line = "client.focused $bg $bg $fg $bg $bg\n"

        new_file_text += line
    
if args.colour == "pywal":

    print("You selected the pywal colour scheme!\n\n")

    original_file = open(i3_config_file_path, "r")

    lines = original_file.readlines()
    #for index, line in enumerate(lines):
    for line in lines:
        
        if "client.focused" in line and "_inactive" not in line:
            line = "client.focused $bg $bg $fg $bg $bg\n"

        new_file_text += line
    
    original_file.close()

    new_file = open(i3_config_file_path, "w")
    new_file.write(new_file_text)
    new_file.close()


def change_i3_titlebar_colours(colour):
    print(f"you have selected the {colour} scheme!")

    original_file = open(i3_config_file_path, "r")
    lines = original_file.readlines()

    for line in lines:
        if "client.focused" in line and "_inactive" not in line:
            line = "client.focused # # # # #"
        
        new_file_text += line

        original_file.close()

        new_file = open(i3_config_file_path, "w")
        new_file.write(new_file_text)
        new_file.close()

