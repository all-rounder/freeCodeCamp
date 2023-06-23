import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def is_overweight(bmi):
    if bmi > 25:
        return 1
    else:
        return 0


def normalize(x):
    if x == 1:
        return 0
    else:
        return 1


# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['bmi'] = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = df['bmi'].apply(is_overweight)
df['cholesterol'] = df['cholesterol'].apply(normalize)
df['gluc'] = df['gluc'].apply(normalize)
df = df.drop('bmi', axis=1)


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1,
# make the value 0. If the value is more than 1, make the value 1.


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke',
    # 'alco', 'active', and 'overweight'.
    df_cat = df[['cardio', 'active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']]

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename
    # one of the collumns for the catplot to work correctly. df_cat = None

    df_melt = pd.melt(df_cat, id_vars=['cardio'])

    # Draw the catplot with 'sns.catplot()'
    sns_plot = sns.catplot(x='variable', hue='value', col="cardio", data=df_melt, kind="count")
    sns_plot.set_ylabels('total')
    fig = sns_plot.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (
                df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (
                                 df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()
    print(corr)

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, fmt='.1f', mask=mask, xticklabels=corr.columns, yticklabels=corr.columns)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
