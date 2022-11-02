import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd


def import_data(path_string, column_number):
    data = pd.read_csv(path_string)

    x_data = data["x-axis"][1:]
    x_data_arr = np.array(x_data).astype(float)

    y_data = data["1"][1:]
    y_data_arr_1 = np.array(y_data).astype(float)

    if column_number == 2:
        y_data = data["2"][1:]
        y_data_arr_2 = np.array(y_data).astype(float)
        return x_data_arr, y_data_arr_1, y_data_arr_2
    
    else:
        return x_data_arr, y_data_arr_1
    

def find_peak(x_data,y_data, ll, ul):
    index = np.where((ll<x_data)&(x_data<ul))
    selected = y_data[index]
    max = selected.max()
    max_index = np.where((y_data == max) & (ll<x_data) & (x_data<ul))
    return max_index


def find_trough(x_data, y_data, ll, ul):
    index = np.where((ll<x_data)&(x_data<ul))
    selected = y_data[index]
    min  = selected.min()
    min_index = np.where((y_data == min) & (ll<x_data) & (x_data<ul))
    return min_index


def subtract_y_data(y1, y2):
    result = y2 - y1
    return result

if __name__ == "__main__":
    x_data_arr, y_data_arr, y_data_arr_2 = import_data("scope_captures\second_calibration\scope_66.csv", 2)
    
    
    # peak_1 = find_peak(x_data_arr,y_data_arr_2, 0.0229254,0.0237008)
    # peak_2 = find_peak(x_data_arr, y_data_arr_2, 0.0300704, 0.030809)
    # print(peak_1)
    # print(peak_2[0][0])
    # peak_2_x = x_data_arr[peak_2[0][0]]
    # peak_1_x = x_data_arr[peak_1[0][0]]
    # peak_diff = peak_2_x - peak_1_x
    # print(f"peak diff {peak_diff}")
    # print(f"Peak 1:{peak_1_x}, Peak 2:{peak_2_x}")
  

    hyperfine_x, hyperfine_y = import_data("scope_captures\scope_105.csv", 1)
    no_hyperfine_x, no_hyperfine_y = import_data("scope_captures\scope_106.csv", 1)
    
    corrected_y = hyperfine_y - no_hyperfine_y
    
    # fig, ax_lst = plt.subplots(2)
    fig, ax = plt.subplots()
    # ax, ax1 = ax_lst
    # ax.vlines([ 0.0228257, 0.0238005 ,0.03 , 0.0308902], ymin=0, ymax=8)
    # ax.vlines([peak_1_x, peak_2_x], ymin=0.5, ymax=8, color="red", label=f"Peaks at {peak_1_x} and {peak_2_x}")
    # min_indexs = []
    # mins = []
    
    # for bound in bounds:
    #     lower, upper = bound
    #     min_index = find_trough(x_data_arr, y_data_arr, lower, upper)
    #     mins.append(x_data_arr[min_index][0])
    #     min_indexs.append(min_index[0][0])
    
    # ax.vlines(min_indexs, ymin=-2, ymax=2, alpha=0.5, color="orange")    
    
    # fig.set_figheight(5)
    # fig.set_figwidth(10)
    
    # ax.set_xticks(np.linspace(0,2000, 10))
    # labels = ax.get_xticklabels()
    # txt = "dt = " + f"{peak_diff/5 :.6f} s" 
    
    # ax.text(0.05, 3,txt)
    paths = ["scope_captures\scope_46.csv", "scope_captures\scope_47.csv"]
    string = ""
    for path in paths:
        string += path
        string += "\n"
    
    ax.text(-0.020, 4.0, str(string))
    
    
    # ax.vlines(peak_1, ymin=5, ymax=10, alpha=0.5, color="orange")
    # ax.vlines(peak_2[0], ymin=5, ymax=10, alpha=0.5, color="orange")
    
    # ax.set_title("Adjusted Rubidium Absorbtion Spectrum")
    ax.set_title("Doppler Free Rubidium absorbtion spectrum")
    ax.set_xlabel("time (s)")
    ax.set_ylabel("Amplitude (V)")
    # ax1.set_title("Adjusted Rubidium Absorbtion Spectrum")
    # ax1.set_xlabel("time (s)")
    # ax1.set_ylabel("Amplitude (V)")
    # ax.plot(x_data_arr, y_data_arr, color="firebrick", label="Trace 1 - Subtracted Rubidium Spectra, Hyperfine")
    # ax.plot(x_data_arr, y_data_arr_2, color="blue", label="Trace 1 - Subtracted Rubidium Spectra, Hyperfine")
    

    ax.plot(no_hyperfine_x, corrected_y, color="purple", label="Doppler Free Rubidium Spectra")
    # ax.plot(hyperfine_x, hyperfine_y, color="orange", label="Rb Spectrum w/ hyperfine")
    # ax.plot(no_hyperfine_x, no_hyperfine_y, color="blue", label="Rb Spectrum w/o hyperfine")
    # ax.grid(True)
    ax.legend()
    # ax1.legend()
    plt.tight_layout()
    plt.show()