import numpy as np 
import scipy.integrate
import matplotlib.pyplot as plt

q = 1000
analyt = (0.5 * (np.exp(-np.pi) + 1))

fig , ax = plt.subplots()

def func_exp_sin(x):
    return np.sin(x) * np.exp(-x)
    
x_range = np.linspace(0, np.pi, q)
plt.plot(x_range, func_exp_sin(x_range))
plt.title("sin(x)*e^-x on the interval 0 to pi")
ax.set_xlabel("x")
ax.set_ylabel("y")

plt.show()


def trap_area(func, a, b, N):
    h = (b-a)/N
    x_in = np.linspace(a, b, int(N+1))
    y_out = func(x_in)
    area = (h/2) * (y_out[0] + y_out[-1] + 2*np.sum(y_out[1:-1]))
    error = np.abs(analyt - area)
    # print(error)
    return [area, h, error]

i = scipy.integrate.trapz(func_exp_sin(x_range), x_range)
# print(i)

err_vals = []
i_list = []
for i in range(4, int(2E+8), int(5E+6)):
    print(i)
    i_list.append(i)
    area, width, error = trap_area(func_exp_sin, 0, np.pi, i)
    # print(area)
    err_vals.append(error)

print(err_vals)

'''c
h_values = np.linspace(0.001, np.pi, 1000)
N_test = np.array(np.pi/h_values)


area_arr = trap_area(func_exp_sin, 0, np.pi, N_test)
new_error = analyt - area_arr[0]
'''
print(np.log10(i_list), np.log10(err_vals))
plt.plot(np.log10(i_list), np.log10(err_vals), marker="o")
plt.title("How the error of numericl result in comparison to analytical result varies with width of trapeziums")
plt.xlabel("Width of histograms")
plt.ylabel("Error")
plt.show()
