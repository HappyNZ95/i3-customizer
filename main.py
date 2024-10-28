import argparse

parser = argparse.ArgumentParser(description="A simple CLI program to customize the colours in i3wm.")

# ArgumentParser

parser.add_argument("colour", type=str, help="the colour you want")

args = parser.parse_args()

client_focused_line = ""

if args.colour == "blue":

    print("You selected the colour blue!\n\n")

    original_file = open("/home/hayden/.config/i3/config", "r")

    lines = original_file.readlines()
    for line in lines:
        
        if "client.focused" in line:
            lines[lines.index(line)] = "client.focused #0096FF #0096FF #000000 #0096FF"

    print(lines)
    file.close()
