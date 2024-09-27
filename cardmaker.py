import pygsheets
import os

def generate_svgs():

    #authorization
    gc = pygsheets.authorize(service_file='berniesspiel-ea15d08842d8.json')

    sh = gc.open_by_url("https://docs.google.com/spreadsheets/d/1KVf36ymTBfr-Kp7_cWn2pi6vYIWnrMUkxOETIpsk_TE")

    #select the first sheet 
    wks = sh[0]


    for k in range(4, 20):
        with open("Weapon Template Veteran.svg", "r") as f:
            svg = f.read()

        for X in "BCDEFGHIMOA":
            print(value := wks.get_value(X+str(k)))
            svg = svg.replace(f".{X}.", value)

        with open(f"Weapons/{value}.svg", "w+", encoding = "utf-8") as f:
            f.write(svg)


def convert_svgs():
    for file in os.listdir("Weapons"):
        if file.endswith(".svg"):
            command = r'inkscape.com --export-type=png -d 300 "Weapons/' + file + r'"'
            #command = r'inkscape.com -?'
            print(command)
            os.system(command)

generate_svgs()
convert_svgs()