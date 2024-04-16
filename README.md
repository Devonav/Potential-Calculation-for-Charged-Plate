Title: Finite Difference Methods for Computing Electric Potential

Overview:
This Python script computes and compares the electric potential near a charged plate using exact calculations and two finite difference methods. It visualizes the results and the absolute error between exact and approximate solutions.

Content:

Introduction:
Briefly explain the problem: computing the electric potential near a charged plate.
Mention the methods used: exact computation and finite difference methods.
File Structure:
main.py: Contains the main script.
functions.py: Defines functions for exact computation and finite difference methods.
plots.py: Contains functions for plotting results.
Libraries Used:
NumPy: For numerical operations.
Matplotlib: For plotting graphs.
Functions:
V_exact(sigma, dr, rrange): Computes exact potential values at given intervals from a charged plate.
E_plate(sigma, dr, rrange): Computes exact electric field values at given intervals from a charged plate.
V_first_order(sigma, dr, rrange): Approximates potential using the first-order finite difference method.
V_second_order(sigma, dr, rrange): Approximates potential using the second-order finite difference method.
plot_V(V_exact, V_finite_diff, V_finite_diff2, dr, rrange): Plots exact and approximate potential values.
plot_abs_error(E_exact, E_finite_diff, E_finite_diff2, dr, rrange): Plots absolute error between exact and approximate solutions.
Main Script (main.py):
Sets parameters for charge density and computation intervals.
Calls functions to compute exact and approximate potential values.
Calls plotting functions to visualize the results.
Usage:
Modify parameters (charge density, interval size) in main.py as needed.
Run main.py to compute and visualize results.
Result Interpretation:
The plotted graphs show the comparison between exact and approximate potential values.
Absolute error plots indicate the accuracy of the finite difference methods.
Evaluate the accuracy and efficiency of each method based on the plotted results.
