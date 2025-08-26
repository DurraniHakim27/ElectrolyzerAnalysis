import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial
import ipywidgets as widgets
from ipywidgets import interactive

# Load the Excel file
file_path = 'C:\\Users\\User\\Desktop\\Internship\\Real Results\\Book1.xlsx'  # Replace with your actual file path
df = pd.read_excel(file_path)

# Rename columns for easier access (adjust based on your file's structure)
df.columns = [
    'Power_Level', 'Voltage', 'Current', 'Surface_Area', 'Hydrogen_Volume_Flow',
    'Valve_Output', 'Temperature', 'Pressure', 'Voltage_Cell', 'Current_Density', 
    'Current_Cell', 'Real_Hydrogen_Volume_Flow_m3', 'Real_Hydrogen_Volume_Flow_kg', 
    'Mass_Flow_kg_s', 'Hydrogen_Mol_Flow', 'Voltage_Efficiency', 'Faraday_Efficiency', 
    'Cell_Efficiency', 'Power', 'Overall_Efficiency'
]

# Drop the first row if it contains units (adjust as needed)
df = df.drop(0)

# Convert relevant columns to numeric values (ignore errors for non-numeric cells)
df['Power_Level'] = pd.to_numeric(df['Power_Level'], errors='coerce')
df['Voltage_Efficiency'] = pd.to_numeric(df['Voltage_Efficiency'], errors='coerce')
df['Faraday_Efficiency'] = pd.to_numeric(df['Faraday_Efficiency'], errors='coerce')
df['Cell_Efficiency'] = pd.to_numeric(df['Cell_Efficiency'], errors='coerce')
df['Overall_Efficiency'] = pd.to_numeric(df['Overall_Efficiency'], errors='coerce')

# Drop any rows with missing values to ensure smooth processing
df = df.dropna(subset=['Power_Level', 'Voltage_Efficiency', 'Faraday_Efficiency', 'Cell_Efficiency', 'Overall_Efficiency'])

# Define the Power Level data and efficiency metrics
power_level = df['Power_Level']
voltage_efficiency = df['Voltage_Efficiency']
faraday_efficiency = df['Faraday_Efficiency']
cell_efficiency = df['Cell_Efficiency']
overall_efficiency = df['Overall_Efficiency']

# Polynomial Regression for Smoothing
degree = 10  # Polynomial degree for regression smoothing

# Fit polynomial regressions
poly_voltage_efficiency = Polynomial.fit(power_level, voltage_efficiency, degree)
poly_faraday_efficiency = Polynomial.fit(power_level, faraday_efficiency, degree)
poly_cell_efficiency = Polynomial.fit(power_level, cell_efficiency, degree)
poly_overall_efficiency = Polynomial.fit(power_level, overall_efficiency, degree)

# Generate smooth x-axis values
power_smooth = np.linspace(power_level.min(), power_level.max(), 200)

# Function to update the plot based on the selected power level
def update_plot(power_input):
    # Compute efficiency values at the given power level
    voltage_eff_at_power = poly_voltage_efficiency(power_input)
    faraday_eff_at_power = poly_faraday_efficiency(power_input)
    cell_eff_at_power = poly_cell_efficiency(power_input)
    overall_eff_at_power = poly_overall_efficiency(power_input)
    
    # Plotting
    plt.figure(figsize=(10, 6))

    # Plot the data points (scatter with 'x' markers)
    plt.plot(power_level, voltage_efficiency, 'o', markersize=4, alpha=0.7, color='blue')
    plt.plot(power_level, faraday_efficiency, 'o', markersize=4, alpha=0.7, color='green')
    plt.plot(power_level, cell_efficiency, 'o', markersize=4, alpha=0.7, color='red')
    plt.plot(power_level, overall_efficiency, 'o', markersize=4, alpha=0.7, color='purple')

    # Plot the smoothed polynomial regression lines
    plt.plot(power_smooth, poly_voltage_efficiency(power_smooth), '-', label='Voltage Efficiency', color='blue')
    plt.plot(power_smooth, poly_faraday_efficiency(power_smooth), '-', label='Faraday Efficiency ', color='green')
    plt.plot(power_smooth, poly_cell_efficiency(power_smooth), '-', label='Cell Efficiency', color='red')
    plt.plot(power_smooth, poly_overall_efficiency(power_smooth), '-', label='Overall Efficiency ', color='purple')

    # Plot the efficiency values at the selected power level
    plt.scatter(power_input, voltage_eff_at_power, color='blue', zorder=5)
    plt.scatter(power_input, faraday_eff_at_power, color='green', zorder=5)
    plt.scatter(power_input, cell_eff_at_power, color='red', zorder=5)
    plt.scatter(power_input, overall_eff_at_power, color='purple', zorder=5)

    # Show the efficiency values at the selected power level
    plt.text(power_input, voltage_eff_at_power, f'  Voltage: {voltage_eff_at_power:.2f}', color='blue', verticalalignment='bottom')
    plt.text(power_input, faraday_eff_at_power, f'  Faraday: {faraday_eff_at_power:.2f}', color='green', verticalalignment='bottom')
    plt.text(power_input, cell_eff_at_power, f'  Cell: {cell_eff_at_power:.2f}', color='red', verticalalignment='bottom')
    plt.text(power_input, overall_eff_at_power, f'  Overall: {overall_eff_at_power:.2f}', color='purple', verticalalignment='bottom')

    # Customize plot
    plt.title('Smoothed Efficiency Metrics vs Power Level (%)')
    plt.xlabel('Power Level (%)')
    plt.ylabel('Efficiency')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    
    # Display the plot
    plt.show()

# Create a slider for selecting power level
power_slider = widgets.FloatSlider(
    value=power_level.min(),  # Starting value
    min=power_level.min(),    # Minimum value
    max=power_level.max(),    # Maximum value
    step=0.1,                 # Step size
    description='Power Level:',
    continuous_update=False   # Only update when the slider is released
)

# Use the slider to call the update_plot function
interactive_plot = interactive(update_plot, power_input=power_slider)
output = interactive_plot.children[-1]
output.layout.height = '700px'
interactive_plot


