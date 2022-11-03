import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
from scipy.optimize import curve_fit


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





if __name__ == "__main__":
    path = "scope_captures\scope_6.csv"
    x_data_arr, y_data_arr, y_data_arr_2 = import_data(path, 2)
    index = np.where((-0.0225<x_data_arr)&(x_data_arr<-0.001))
    x_selected = x_data_arr[index]
    y_selected = y_data_arr[index]
    fig, ax = plt.subplots()
    ax.text(-0.023,-1, path)
    ax.plot(x_selected, y_selected, color="b", label="Rubidium, Absorbtion Spectra")
    ax.legend()
    ax.set_title("Rubidium Absorbtion Spectrum With Pump Beam")
    fig.set_figheight(4)
    fig.set_figwidth(8)
    plt.tight_layout()
    plt.show()