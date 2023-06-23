import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    df.plot.scatter(x='Year', y="CSIRO Adjusted Sea Level")
    sr1 = pd.Series([int(i) for i in range(1880, 2050)])
    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df["CSIRO Adjusted Sea Level"])
    plt.plot(sr1, intercept + slope * sr1, 'r', label='fitted line')

    # Create second line of best fit
    recent = df[df['Year'] >= 2000]
    slope, intercept, r_value, p_value, std_err = linregress(recent['Year'], recent["CSIRO Adjusted Sea Level"])

    sr2 = pd.Series([int(i) for i in range(2000, 2050)])
    recent.append(sr2, ignore_index=True)
    plt.plot(sr2, intercept + slope * sr2, 'r', label='fitted line', color="orange")

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()