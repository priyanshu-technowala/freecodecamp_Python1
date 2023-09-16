import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Import the data from the CSV file.
df = pd.read_csv('epa-sea-level.csv')

# Create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

# Use the linregress function to get the slope and y-intercept of the line of best fit.
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

# Plot the line of best fit over the top of the scatter plot.
plt.plot(df['Year'], slope * df['Year'] + intercept, color='red')

# Make the line go through the year 2050 to predict the sea level rise in 2050.
plt.plot([2050], [slope * 2050 + intercept], marker='o', color='red')

# Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset.
recent_df = df[df['Year'] >= 2000]
slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
plt.plot(recent_df['Year'], slope_recent * recent_df['Year'] + intercept_recent, color='blue')

# Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
plt.plot([2050], [slope_recent * 2050 + intercept_recent], marker='o', color='blue')

# Set the x and y labels and the title of the plot.
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

# Show the plot.
plt.show()

# Predict the sea level rise in 2050 using the line of best fit for the entire dataset.
predicted_sea_level_rise_2050 = slope * 2050 + intercept
print('Predicted sea level rise in 2050 using the line of best fit for the entire dataset:', predicted_sea_level_rise_2050)

# Predict the sea level rise in 2050 using the line of best fit for the data from year 2000 through the most recent year in the dataset.
predicted_sea_level_rise_2050_recent = slope_recent * 2050 + intercept_recent
print('Predicted sea level rise in 2050 using the line of best fit for the data from year 2000 through the most recent year in the dataset:', predicted_sea_level_rise_2050_recent)
