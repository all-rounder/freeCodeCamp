import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

pd.set_option('display.width', 160)
pd.set_option('display.max_columns', 160)
pd.set_option('display.max_colwidth', 160)


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    # fig, ax = plt.subplots(figsize=(11, 9))
    plt.scatter('Year', 'CSIRO Adjusted Sea Level', data=df)

    # Create first line of best fit
    slope, intercept, r, p, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    sr1 = pd.Series([i for i in range(1880, 2050)])
    plt.plot(sr1, intercept + slope * sr1, 'r')

    # def myfunc(x):
    #     return slope * x + intercept
    # for x in range(2014, 2051):
    #     # df = df.append([{'Year': x}], ignore_index=True)
    #     df = df.append([{'Year': x, 'CSIRO Adjusted Sea Level': myfunc(x)}], ignore_index=True)
    # print(df)
    # plt.plot(df['Year'], intercept + slope * df['Year'], 'r')

    # Create second line of best fit
    df2 = df[df['Year'] >= 2000]
    slope, intercept, r, p, std_err = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    sr2 = pd.Series([i for i in range(2000, 2050)])
    plt.plot(sr2, intercept + slope * sr2, 'r')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
