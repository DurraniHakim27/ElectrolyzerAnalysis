# Project Overview

This repository contains Python code for analyzing electrolyzer performance data extracted from an Excel file (Book1.xlsx). The project calculates key efficiency metrics and fits electrochemical models, including:

Faradaic efficiency (η<sub>F</sub>) – efficiency of charge usage for desired product (H₂) generation.

Voltage efficiency (η<sub>V</sub>) – ratio of theoretical reversible voltage to actual cell voltage.

Cell (energy) efficiency (η<sub>cell</sub>) – fraction of electrical energy stored as chemical energy in H₂ (product of η<sub>F</sub> and η<sub>V</sub>
en.wikipedia.org
).

Overall energy efficiency (η<sub>energy</sub>) – ratio of hydrogen energy output to electrical energy input.

Tafel analysis – fits the Tafel equation to polarization data to extract kinetic parameters.

Each metric is computed and plotted by the provided scripts. The code reads the raw data, performs calculations, and generates plots in the results/ folder.

Setup and Dependencies

Python Version: Use Python 3.7+.

Install dependencies: Run pip install -r requirements.txt in your virtual environment. Typical packages include:

pandas (data handling)

numpy (numerical operations)

matplotlib or seaborn (plotting)

scipy (for curve fitting, e.g. Tafel)

openpyxl or xlrd (Excel I/O)

Environment: It’s recommended to use a virtual environment (venv/conda) to manage packages. The requirements.txt file pins all necessary libraries.

Excel Data: Place the original data file (Book1.xlsx) in data/raw/. Do not modify this file; any cleaning should be done by scripts copying from it.

Running the code: Each script can be executed from the command line or an IDE:

Efficiencies calculation:
