import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, leastsq
from plot_simple import import_data


def gaussian(x, a, b, c):
    '''
    a: height of peak
    b: center position of the peak
    c: the standard deviation
    '''
    f = a * np.exp(-(x-b)**2/(2*c**2))
    return f


def lorentzian( x, x0, a, gam ):
    L = a * gam**2 / ( gam**2 + ( x - x0 )**2)
    return L

fig, ax = plt.subplots(1)
ax.set_title("Rb Absorbtion Spectrum With Gaussian and Lorentzian Fits")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Amplitude (V)")

# # Trough 1
# path_hyperfine = "scope_captures\second_calibration\scope_64.csv"
# path_no_hyperfine = "scope_captures\second_calibration\scope_65.csv"
# hyperfine_x, hyperfine_y = import_data(path_hyperfine, 1)
# no_hyperfine_x, no_hyperfine_y = import_data(path_no_hyperfine, 1)

# bounds=[[0.0227434, 0.0231],
#     [0.0233989, 0.0236],
#     [0.0237, 0.0241281],
#     [0.0241281, 0.0247236],
#     [0.0252174, 0.0256375]]

# # Trough 1 Time Averaged
# path_hyperfine = "scope_captures\second_calibration\scope_73.csv"
# path_no_hyperfine = "scope_captures\second_calibration\scope_74.csv"
# hyperfine_x, hyperfine_y = import_data(path_hyperfine, 1)
# no_hyperfine_x, no_hyperfine_y = import_data(path_no_hyperfine, 1)

# bounds=[[0.02018, 0.0204],
#     [0.020768, 0.0210],
#     [0.021319, 0.02155],
#     [0.02174, 0.022],
#     [0.022207, 0.0226703],
#     [0.0232 , 0.023505]]

# Trough 2
# path_hyperfine = "scope_captures\second_calibration\scope_68.csv"
# path_no_hyperfine = "scope_captures\second_calibration\scope_69.csv"
# hyperfine_x, hyperfine_y = import_data(path_hyperfine, 1)
# no_hyperfine_x, no_hyperfine_y = import_data(path_no_hyperfine, 1)

# bounds=[[0.0254766, 0.025621],
# [0.0259199, 0.026082],
# [0.0260862, 0.0264464],
# [0.0265388, 0.026705]]

# Trough 2 Time Averaged
# path_hyperfine = "scope_captures\second_calibration\scope_75.csv"
# path_no_hyperfine = "scope_captures\second_calibration\scope_76.csv"
# hyperfine_x, hyperfine_y = import_data(path_hyperfine, 1)
# no_hyperfine_x, no_hyperfine_y = import_data(path_no_hyperfine, 1)

# bounds=[
#     [0.0205, 0.0207],
# [0.02082, 0.02095],
# [0.0210492, 0.02118],
# [0.02127, 0.0214],
# [0.021465, 0.02165], 
# [0.0219, 0.02205]
# ]

# Trough 3
# path_hyperfine = "scope_captures\second_calibration\scope_60.csv"
# path_no_hyperfine = "scope_captures\second_calibration\scope_61.csv"
# hyperfine_x, hyperfine_y = import_data(path_hyperfine, 1)
# no_hyperfine_x, no_hyperfine_y = import_data(path_no_hyperfine, 1)

# bounds = [[0.02569, 0.0258748],
# [0.0254965, 0.0256302]]

# Trough 3 Time Averaged
# path_hyperfine = "scope_captures\second_calibration\scope_80.csv"
# path_no_hyperfine = "scope_captures\second_calibration\scope_81.csv"
# hyperfine_x, hyperfine_y = import_data(path_hyperfine, 1)
# no_hyperfine_x, no_hyperfine_y = import_data(path_no_hyperfine, 1)

# bounds = [[0.02099, 0.021065],
# [0.02115, 0.02137],
# [0.0215, 0.02162]]

# # # # Trough 4
# path_hyperfine = "scope_captures\second_calibration\scope_71.csv"
# path_no_hyperfine = "scope_captures\second_calibration\scope_72.csv"
# hyperfine_x, hyperfine_y = import_data(path_hyperfine, 1)
# no_hyperfine_x, no_hyperfine_y = import_data(path_no_hyperfine, 1)


# bounds = [[0.0274781, 0.027672],
#     [0.027695, 0.0279397],
#     [0.02803, 0.0282074],
#     [0.0282166, 0.0284705],
#     [0.0287566, 0.02901]]

# # # # Trough 4 Time averaged
# path_hyperfine = "scope_captures\second_calibration\scope_80.csv"
# path_no_hyperfine = "scope_captures\second_calibration\scope_81.csv"
# hyperfine_x, hyperfine_y = import_data(path_hyperfine, 1)
# no_hyperfine_x, no_hyperfine_y = import_data(path_no_hyperfine, 1)


# bounds = [[0.02696, 0.02705],
# [0.0272, 0.0273],
# [0.0275, 0.02763],
# [0.027745,0.0279],
# [0.02829,0.0285]]

# path_hyperfine = "scope_captures\scope_95.csv"
# path_no_hyperfine = "scope_captures\scope_96.csv"

path_hyperfine = "scope_captures\scope_103.csv"
path_no_hyperfine = "scope_captures\scope_104.csv"

bounds = [[0.0922, 0.0929],
[0.0934, 0.09429],
[0.0949, 0.0958],
[0.0966,0.0974],
[0.0974,0.0983],
[0.1002, 0.1016]]

# path_hyperfine = "scope_captures\scope_99.csv"
# path_no_hyperfine = "scope_captures\scope_100.csv"

hyperfine_x, hyperfine_y = import_data(path_hyperfine, 1)
no_hyperfine_x, no_hyperfine_y = import_data(path_no_hyperfine, 1)


ax.text(-0.023, 0.5,f"{path_hyperfine} \n{path_no_hyperfine}")

corrected = hyperfine_y - no_hyperfine_y
print(np.isnan(hyperfine_x).any(),
np.isnan(corrected).any(),

np.isinf(hyperfine_x).any(),
np.isinf(corrected).any())

corrected = np.nan_to_num(corrected)

# popt_ls = leastsq(gaussian, x0=[1,1,1,1],  args=(hyperfine_x, corrected))
ul = -0.0135
ll = -0.017


# ax.vlines([ll,ul], ymin=-0.2, ymax=0.5)

def fit_gaussian(x_data, y_data, lower_lim, upper_lim):
    index = np.where((lower_lim<x_data) & (x_data<upper_lim))

    fit_y = corrected[index]
    fit_x = hyperfine_x[index]
# print(len(fit_x))
    popt_cf, pcov = curve_fit(gaussian, fit_x ,fit_y, maxfev=50000)
# popt_cf_lrtz, pcov = curve_fit(lorentzian, fit_x ,fit_y, maxfev=10000)


# ax.plot(hyperfine_x, hyperfine_y)
# ax.plot(hyperfine_x, no_hyperfine_y)
    # ax.plot(hyperfine_x[index], gaussian(hyperfine_x,*popt_cf)[index], label=f"Gaussian: a={popt_cf[0]:.5f}, b={popt_cf[1]:.5f}, c={popt_cf[2]:.5}", color="blue")
   
def fit_lorentzian(x_data, y_data, lower_lim, upper_lim):
    index = np.where((lower_lim<x_data) & (x_data<upper_lim))

    fit_y = corrected[index]
    fit_x = hyperfine_x[index]
# print(len(fit_x))
    popt_cf, pcov = curve_fit(lorentzian, fit_x ,fit_y, maxfev=50000)
    print(np.diag(pcov)[0])
    ax.plot(hyperfine_x[index], lorentzian(hyperfine_x,*popt_cf)[index], label=f"Lorentzian: $X_0$={popt_cf[0]:.5f}, a={popt_cf[1]:.5f}, $\\gamma$={popt_cf[2]:.5}", color="red")

ind = 0

for bound in bounds:
    # print(bound)
    ax.vlines((bound[0], bound[1]), ymin=-0.01, ymax=0.020, alpha=0.5, linestyle = "--")
    fit_gaussian(hyperfine_x, corrected, bound[0], bound[1])
    fit_lorentzian(hyperfine_x, corrected, bound[0], bound[1])
    ax.text(bound[0] + (bound[1] - bound[0])/2,-0.01 , str(ind))
    ind+=1

ax.plot(hyperfine_x, corrected, alpha=0.5)
ax.legend()
plt.show()