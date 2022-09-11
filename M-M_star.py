import numpy as np
from matplotlib import pyplot as plt

def M_star(M, gamma):
    return np.sqrt((gamma+1)*M**2/(2+(gamma-1)*M**2))

def main():
    M = np.linspace(0, 100, 10000)
    gamma = 1.4
    isen_points = M_star(M, gamma)

    plt.plot(M, isen_points, label="M_star")
    plt.plot(M, M, label="M")

    plt.xlim(0, 10)
    plt.ylim(0, 10)

    plt.xlabel("M")
    plt.ylabel("M*, M")
    plt.legend()
    plt.show()

if __name__=="__main__":
    main()