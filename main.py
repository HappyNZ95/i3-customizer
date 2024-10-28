import argparse
import os

parser = argparse.ArgumentParser(description="A simple CLI program to customize the colours in i3wm.")
i3_config_file_path = os.path.expanduser("~/.config/i3/config")
# ArgumentParser

parser.add_argument("colour", type=str, help="the colour you want")

args = parser.parse_args()

client_focused_line = ""

new_file_text = ""

if args.colour == "blue":

    print("You selected the colour blue!\n\n")

    original_file = open(i3_config_file_path, "r")

    lines = original_file.readlines()
    #for index, line in enumerate(lines):
    for line in lines:
        
        if "client.focused" in line and "_inactive" not in line:
            line = "client.focused           #0096FF #0096FF #000000 #0096FF\n"

        new_file_text += line
    
    original_file.close()

    new_file = open(i3_config_file_path, "w")
    new_file.write(new_file_text)
    new_file.close()
