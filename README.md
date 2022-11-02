# Investigating Doppler-Free Spectroscopy Techniques With a Rubidium Vapour
## Solomon Sanderson & Dominic Mould
This repository contains the code written by [Solomon Sanderson](https://github.com/solomonsanderson) for investigating Doppler-free spectroscopy with a rubidium vapour as part of Year 3 Photonics Labs at the University of Birmingham.

### Repository Structure
The structure of this repository is detailed below:
* `scope_captures`: Contains all of the data that we capured using the oscilloscope throughout out lab sessions.
    * `second_calibration`: Contains data used for the second calibration of our setup
* `fitting.py`: A script for fitting Lorentzian and Gaussian curves to each of the peaks of our data *individually*. Used for identifying the positions of the hyperfine peaks.
* `new_fitting.py`: A script for fitting multiple Lorentzians to the *entire* Rubidium spectrum and visualising how the constituent peaks make up the overall spectrum
* `plot_simple.py`: A script for plotting `.csv` files from the oscilloscope, contains some code for finding the maxima of the calibration wave. Used for general plotting.

### Data Structure
The data is formatted such that the first row contains "axis", "1" and "2" where 1 and 2 refer to channels 1 and 2. The second row contains the units of the above quantities.

Beyond this the first column contains the time in seconds, the second and third columns record the amplitude in Volts.

If one of the channels is disabled then its respective column is not present.

