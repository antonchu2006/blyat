#!/usr/bin/python3
import sys

if len(sys.argv) < 2:
    print("\n[!] Usage: blyat <filename>")
    sys.exit(0)

filename = sys.argv[1]

if __name__ == "__main__":

    print("\n\n»-(¯`·.·´¯)-> " +  filename + " <-(¯`·.·´¯)-«\n\n")

    fichero = open(filename, "r")

    linea = fichero.readlines()
    line = 0
    for i in linea:
        line += 1
        output = chr(27)+"[0;36m"+str(line)+ chr(27) + "[0m" + " " + str(i)
        print(output.strip("\n"))
