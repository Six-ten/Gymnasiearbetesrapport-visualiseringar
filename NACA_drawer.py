from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    script_dir = Path(__file__).resolve().parent

    
    naca_high_def_path = script_dir / "naca_high_def.csv"
    naca_low_def_path = script_dir / "naca_low_def.csv"
    
    naca_continous, naca_discretized = naca_reader(naca_high_def_path)



    plt.plot(naca_continous["x"], naca_continous["y"], "r", naca_discretized["x"], naca_discretized["y"], "g--", lw=1)

    plt.xticks(np.arange(-0.5, 1.5, 0.25))
    plt.yticks(np.arange(-1, 1, 0.25))
    plt.xlim(-0.1, 1.1)
    plt.ylim(-0.1, 0.2)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()

def naca_reader(file_name):


    naca_finished = {"x": [], "y": []}
    naca_discrete = {"x": [], "y": []}
    with open(file_name, "r") as file:
        
        for line in file:
            
            n = line.find(" ")

            try:
                x = float(line[0:n])
                y = float(line[n + 1:])
            except:
                continue

            naca_finished["x"].append(x)
            naca_finished["y"].append(y)
            if (len(naca_finished["x"]) % 10 == 0):
                naca_discrete["x"].append(x)
                naca_discrete["y"].append(y)
    print(len(naca_discrete["x"]))
    if(naca_finished["x"][-1] != naca_discrete["x"][-1]):
        naca_discrete["x"].append(naca_finished["x"][-1])
        naca_discrete["y"].append(naca_finished["y"][-1])
    print(len(naca_discrete["x"]))
    return naca_finished, naca_discrete
            
if (__name__ == "__main__"):
    main()