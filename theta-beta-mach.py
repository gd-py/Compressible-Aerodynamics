import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

## returns (theta, beta) value for which M_2 = 1
def M2_value(M_1, theta_range, beta_range, gamma):
    M_1n = M_1*np.sin(beta_range)
    M_2n = np.sqrt(np.abs((1+(gamma-1)/2*M_1n**2)/(gamma*M_1n**2-(gamma-1)/2)))
    M_2 = M_2n/(np.sin(beta_range-theta_range))
    ## find index in M_2 where M_2 = 1
    M2_min_index = (np.abs(M_2 - 1)).argmin()
    theta, beta = theta_range[M2_min_index], beta_range[M2_min_index]
    return 180/(np.pi)*np.array([theta, beta])

def main():
    gamma = 1.4
    max_values = np.empty((0, 2))
    M2_values = np.empty((0, 2))
    M_1_range = np.arange(1.1, 10, 0.2)
    for M_1 in M_1_range:
        beta_range = np.linspace(0.001, np.pi/2-0.001, 1000)
        ## this is the main formula. Ref: John D. Anderson, Page 570
        theta_range = np.arctan(2*1/np.tan(beta_range)*((M_1*np.sin(beta_range))**2-1)/(M_1**2*(gamma+np.cos(2*beta_range))+2))
        data = np.zeros((beta_range.shape[0], 2))
        data[:, 0] = theta_range
        data[:, 1] = beta_range
        ## delete negative theta values from the data
        data = 180/(np.pi)*data[np.all(data>=0, axis=1)]
        ## compute (theta, beta) value for shock attachment point.
        max_values = np.append(max_values, np.expand_dims(data[np.argmax(data, axis=0)[0]], axis=0), axis=0)
        ## compute (theta, beta) value for which M_2 = 1
        M2_values = np.append(M2_values, np.expand_dims(M2_value(M_1, np.pi/180*data[:, 0], np.pi/180*data[:, 1], gamma), axis=0), axis=0)
        plt.plot(data[:, 0], data[:, 1])

    ## Beautify plots from here!!
    ## Use scipy spline interpolation to smooth the curve   
    theta_max, beta_max = max_values[:, 0], max_values[:, 1]
    xy_spline = make_interp_spline(theta_max, beta_max)
    theta_max = np.linspace(0, max(theta_max), 1000)
    beta_max = xy_spline(theta_max)

    theta_M2, beta_M2 = M2_values[:, 0], M2_values[:, 1]
    xy_spline = make_interp_spline(theta_M2, beta_M2)
    theta_M2 = np.linspace(0, max(theta_M2), 1000)
    beta_M2 = xy_spline(theta_M2)
    
    plt.plot(theta_M2, beta_M2, '--', color='green', label='sonic behind shockwave')
    plt.plot(theta_max, beta_max, '-.', color='red', label='shock detached beyond this line')

    plt.xlim(0, 45)
    plt.ylim(0, 90)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()