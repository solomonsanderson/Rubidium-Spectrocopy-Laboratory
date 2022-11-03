import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, leastsq
from sympy import C
# from fitting import gaussian
from plot_simple import import_data


def find_trough(x_data, y_data, ll, ul):
    index = np.where((ll<x_data)&(x_data<ul))
    selected = y_data[index]
    min  = selected.min()
    min_index = np.where((y_data == min) & (ll<x_data) & (x_data<ul))
    return min_index


def plot_hyperfine(hyperfine_path, no_hyperfine_path, ax, ax_original=None):
    '''A function for plotting the doppler free hyperfine data. If a value of ax_original is given then the original data will be plotted on this axis'''

    hyperfine_x, hyperfine_y = import_data(hyperfine_path, 1)
    no_hyperfine_x, no_hyperfine_y = import_data(no_hyperfine_path, 1)
    corrected_y = hyperfine_y - no_hyperfine_y
    ax.plot(no_hyperfine_x, corrected_y, color="purple", label="Doppler Free Rubidium Spectra")
    ax.set_xlabel("Time (s))")
    ax.set_ylabel("Amplitude (V)")
    
    if ax_original is not None:
        ax_original.plot(hyperfine_x, hyperfine_y, color="orange", label="Rb Spectrum w/ hyperfine")
        ax_original.plot(no_hyperfine_x, no_hyperfine_y, color="blue", label="Rb Spectrum w/o hyperfine")
        ax_original.set_xlabel("Time (s))")
        ax_original.set_ylabel("Amplitude (V)")
    ax.legend()


def calibration_plot(x_data, y_data, bounds, ax):

    # Finding the minima of the spectrum to identify troughs
    min_indexs = []
    mins = []
    for bound in bounds:
        lower, upper = bound
        min_index = find_trough(x_data, y_data, lower, upper)
        mins.append(x_data[min_index][0])
        min_indexs.append(min_index[0][0])
    
    x_pos = x_data[min_indexs]
    print(np.diff(x_pos))

    ax.vlines(x_pos, ymin=-2, ymax=2, alpha=0.5, color="orange", label=f"Minima of Rb Spectrum troughs:\n{x_pos[0]:.3} s, {x_pos[1]:.3} s, {x_pos[2]:.3} s, {x_pos[3]:.3} s ")    


def sinfunc(t, A, w, p, c):
    return A * np.sin(w*t + p) + c


def fit_sin(tt, yy):
    '''Fit sin to the input time sequence, and return fitting parameters "amp", "omega", "phase", "offset", "freq", "period" and "fitfunc"'''
    tt = np.array(tt)
    yy = np.array(yy)
    ff = np.fft.fftfreq(len(tt), (tt[1]-tt[0]))   # assume uniform spacing
    Fyy = abs(np.fft.fft(yy))
    guess_freq = abs(ff[np.argmax(Fyy[1:])+1])   # excluding the zero frequency "peak", which is related to offset
    guess_amp = np.std(yy) * 2.**0.5
    guess_offset = np.mean(yy)
    guess = np.array([guess_amp, 2.*np.pi*guess_freq, 0., guess_offset])

    popt, pcov = curve_fit(sinfunc, tt, yy, p0=guess)
    A, w, p, c = popt
    f = w/(2.*np.pi)
    print(1/f)
    fitfunc = lambda t: A * np.sin(w*t + p) + c
    return popt, pcov, f

if  __name__ == "__main__":
    x_data_arr, y_data_arr, y_data_arr_2 = import_data("scope_captures\scope_3.csv", 2)
    
    fig, ax = plt.subplots()


    index = np.where((-0.0136<x_data_arr)&(x_data_arr<-0.0005))
    y_selected = y_data_arr_2[index]
    x_selected = x_data_arr[index]
    ax.plot(x_data_arr,y_data_arr, color="r", label="Rb Spectrum")
    ax.plot(x_data_arr, y_data_arr_2, color="green", alpha = 0.5, label="Cavity Intensity")

    popt, pcov, f = fit_sin(x_selected, y_selected)
    error = np.diag(pcov)
    rel_error = error[2]/popt[2]
    period = 1/f
    period_err = period * rel_error
    ax.plot(x_selected, sinfunc(x_selected, *popt), color = "blue", label = f"Sin fit to calibration curve, \n T = {period:.3} $\pm$ {period_err:.3} s")

    bounds = [[-0.0144, -0.0131],
        [-0.0123, -0.0111],
        [-0.00699, -0.00584],
        [-0.00271, -0.00148]]

    calibration_plot(x_data_arr, y_data_arr, bounds, ax)
    ax.text(0.02,-2, "scope_3.csv")
    ax.legend(loc="upper right")
    ax.set_title("Calibration of Oscilloscope Time axis")
    fig.set_figheight(4)
    fig.set_figwidth(8)
    plt.tight_layout()
    plt.show()