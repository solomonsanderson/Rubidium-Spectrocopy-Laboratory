import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, leastsq
from sympy import C
# from fitting import gaussian
from plot_simple import import_data


def lorentzian_1(x, a, x0, gam ):
    L = a * gam**2 / ( gam**2 + ( x - x0 )**2)
    return L


def lorentzian_6(x , a_1, x0_1, gam_1, a_2, x0_2, gam_2, a_3, x0_3, gam_3, a_4, x0_4, gam_4 , a_5, x0_5, gam_5, a_6, x0_6, gam_6):
    L_1 = a_1 * gam_1**2 / ( gam_1**2 + ( x - x0_1 )**2)
    L_2 = a_2 * gam_2**2 / ( gam_2**2 + ( x - x0_2 )**2)
    L_3 = a_3 * gam_3**2 / ( gam_3**2 + ( x - x0_3 )**2)
    L_4 = a_4 * gam_4**2 / ( gam_4**2 + ( x - x0_4 )**2)
    L_5 = a_5 * gam_5**2 / ( gam_5**2 + ( x - x0_5 )**2)
    L_6 = a_6 * gam_6**2 / ( gam_6**2 + ( x - x0_6 )**2)
    return L_1 + L_2 + L_3 + L_4 + L_5 + L_6

def lorentzian_6_c(x , a_1, x0_1, gam_1, c_1, a_2, x0_2, gam_2, c_2, a_3, x0_3, gam_3, c_3, a_4, x0_4, gam_4,c_4 , a_5, x0_5, gam_5, c_5, a_6, x0_6, gam_6, c_6):
    L_1 = a_1 * gam_1**2 / ( gam_1**2 + ( x - x0_1 )**2) + c_1
    L_2 = a_2 * gam_2**2 / ( gam_2**2 + ( x - x0_2 )**2) + c_2
    L_3 = a_3 * gam_3**2 / ( gam_3**2 + ( x - x0_3 )**2) + c_3
    L_4 = a_4 * gam_4**2 / ( gam_4**2 + ( x - x0_4 )**2) + c_4
    L_5 = a_5 * gam_5**2 / ( gam_5**2 + ( x - x0_5 )**2) + c_5
    L_6 = a_6 * gam_6**2 / ( gam_6**2 + ( x - x0_6 )**2) + c_6
    return L_1 + L_2 + L_3 + L_4 + L_5 + L_6
  
def lorentzian_7(x , a_1, x0_1, gam_1, a_2, x0_2, gam_2, a_3, x0_3, gam_3, a_4, x0_4, gam_4 , a_5, x0_5, gam_5, a_6, x0_6, gam_6,  a_7, x0_7, gam_7):
    L_1 = a_1 * gam_1**2 / ( gam_1**2 + ( x - x0_1 )**2)
    L_2 = a_2 * gam_2**2 / ( gam_2**2 + ( x - x0_2 )**2)
    L_3 = a_3 * gam_3**2 / ( gam_3**2 + ( x - x0_3 )**2)
    L_4 = a_4 * gam_4**2 / ( gam_4**2 + ( x - x0_4 )**2)
    L_5 = a_5 * gam_5**2 / ( gam_5**2 + ( x - x0_5 )**2)
    L_6 = a_6 * gam_6**2 / ( gam_6**2 + ( x - x0_6 )**2)
    L_7 = a_7 * gam_7**2 / ( gam_7**2 + ( x - x0_7 )**2)
    return L_1 + L_2 + L_3 + L_4 + L_5 + L_6 + L_7

# path_hyperfine = "scope_captures\scope_95.csv"
# path_no_hyperfine = "scope_captures\scope_96.csv"

path_hyperfine = "scope_captures\scope_97.csv"
path_no_hyperfine = "scope_captures\scope_98.csv"


# path_hyperfine = "scope_captures\scope_99.csv"
# path_no_hyperfine = "scope_captures\scope_100.csv"

hyperfine_x, hyperfine_y = import_data(path_hyperfine, 1)
no_hyperfine_x, no_hyperfine_y = import_data(path_no_hyperfine, 1)

corrected = hyperfine_y - no_hyperfine_y

# Removing infinite or nan values
print(np.isnan(hyperfine_x).any(),
np.isnan(corrected).any(),

np.isinf(hyperfine_x).any(),
np.isinf(corrected).any())

corrected = np.nan_to_num(corrected)

fig, ax1 = plt.subplots(1)
ax1.scatter(hyperfine_x, corrected, alpha=0.2)


# Fitting the lorentzian to the data
p0_2 = [0.380090366,0.09027, -1.1e-02,
 8.83644818e-02,0.093257,2.24490169e-04,
 0.112803950,0.0962,5.68822448e-04,
 0.399189408,0.09895, -3.78976656e-03, 
 0.91873538,0.101854,1.44264060e-03,
 0.69296368,0.107521,5.21090752e-04]

p0_2_c = [0.1,0.09027, 1.1e-02, 0.1,
 0.3,0.093257,2.24490169e-03, 0.1,
 0.5,0.0962,5.68822448e-03, 0.1,
 1.5,0.09895, 3.78976656e-02, 0.1,
 1,0.101854,1.44264060e-02, 0.01,
 0.3,0.107521,5.21090752e-02, 0.01]

p0_3 = [0.04110014,  0.09263,  0.00057025,
  0.138376074,  0.093597,  0.01,
  0.20285041,  0.09530,  0.00085261,
  8.49493844e-01,  9.89256724e-02, -7.32728819e-04,
  0.15302152,  0.0969919,  0.00106025,
  0.42950428,  0.09801, -0.00099101,
  0.22778305,  0.10107,  0.00099448]

p0_3_c = [0.04110014,  0.09263,  0.00057025, 0.1,
  0.04110014,  0.09263,  0.00057025, 0.1,
  0.138376074,  0.093597,  0.01, 0.1,
  0.20285041,  0.09530,  0.00085261, 0.1,
  0.15302152,  0.0969919,  0.00106025, 0.1,
  0.42950428,  0.09801, -0.00099101, 0.1,
  0.22778305,  0.10107,  0.00099448, 0.1]

p0_4 = [0.04110014,  0.08251538,  0.057025,
  0.0138376074,  0.086195,  0.01,
  0.020285041,  0.08955493,  0.085261,
  0.015302152,  0.09361354,  0.0106025,
  0.042950428,  0.09702558, -0.099101,
  0.22778305,  0.10441   ,  0.00099448]


popt, pcov = curve_fit(lorentzian_7, hyperfine_x, corrected, p0=p0_3, maxfev=500000)
print(popt)
ax1.plot(hyperfine_x, lorentzian_7(hyperfine_x, *popt), color="red")
# ax1.plot(hyperfine_x, lorentzian_6(hyperfine_x, *p0_2), color="orange")

for i in np.arange(0,len(p0_3) - 1, 3):
    params = popt[i: i+3]
    # print(params)
    ax1.plot(hyperfine_x, lorentzian_1(hyperfine_x, *params), color="green", alpha=0.3, label = f"x0: {params[1]}")

ax1.legend()
plt.show()