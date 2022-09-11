import numpy as np
from matplotlib import pyplot as plt

def isentropic(M, gamma):
    return 1/np.sqrt(1/(M**2)*(2/(gamma+1)*(1+(gamma-1)/2*M**2))**((gamma+1)/(gamma-1)))

def kantrowitz(M, gamma):
    return M*((gamma+1)/(2+(gamma-1)*M**2))**((gamma+1)/
            (2*(gamma-1)))*((gamma+1)*M**2/((gamma-1)*M**2+2))**(-gamma/
            (gamma-1))*((gamma+1)/(2*gamma*M**2-(gamma-1)))**(-1/(gamma-1))

def main():
    M_isen = np.linspace(0, 10, 1000)
    M_kanto = M_isen[100:]
    gamma = 1.4
    isen_points = isentropic(M_isen, gamma)
    kanto_points = kantrowitz(M_kanto, gamma)

    plt.plot(M_isen, isen_points, label="isentropic")
    plt.plot(M_kanto, kanto_points, label="kantrowitz")
    # plt.plot([1 for i in range(1000)], np.linspace(0, 1, 1000), '-.', color='black', linewidth=0.7, label='throat')

    plt.xlabel("M")
    plt.ylabel("A*/A")
    plt.xlim(0, 10)
    plt.ylim(0, 1.1)
    # plt.fill_between(M_isen, 0, isen_points, color='blue', alpha=0.3, label="choked_isentropic")
    # plt.fill_between(M_kanto, isen_points[100:], kanto_points, color='red', alpha=0.3, label="choked_kantrowitz")
    plt.legend()
    # plt.savefig('area-mach.png', dpi=1000)
    plt.show()

if __name__=="__main__":
    main()