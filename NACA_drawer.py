from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    script_dir = Path(__file__).resolve().parent

    
    csv_path = script_dir / "naca_high_def.csv"
    naca_continous = naca_reader(csv_path)

    plt.plot(naca_continous["x"], naca_continous["y"])
    plt.show()

def naca_reader(file_name):


    naca_finished = {"x": [], "y": []}
    with open(file_name, "r") as file:
        for line in file:
            n = line.find(" ")
            x = float(line[0:n])
            y = float(line[n + 1:])
            naca_finished["x"].append(x)
            naca_finished["y"].append(y)
    return naca_finished
            
main()