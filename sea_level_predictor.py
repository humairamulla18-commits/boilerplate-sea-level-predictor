import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Import data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data')

    # First line of best fit (all data through 2050)
    slope1, intercept1, r1, p1, se1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years1 = range(df['Year'].min(), 2051)
    ax.plot(years1, [slope1 * y + intercept1 for y in years1], 
            color='red', label='Best Fit Line (1880-2050)')

    # Second line of best fit (from 2000 through 2050)
    df_2000 = df[df['Year'] >= 2000]
    slope2, intercept2, r2, p2, se2 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years2 = range(2000, 2051)
    ax.plot(years2, [slope2 * y + intercept2 for y in years2], 
            color='green', label='Best Fit Line (2000-2050)')

    # Labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    fig.savefig('sea_level_plot.png')
    return ax
