import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the medical examination data into a Pandas DataFrame.
df = pd.read_csv('medical_examination.csv')

# Add an overweight column to the data.
df['overweight'] = df['weight'] / (df['height'] / 100) ** 2 > 25

# Normalize the data by making 0 always good and 1 always bad.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# Convert the data into long format.
long_df = df.set_index(['cardio']).stack().reset_index(name='value').rename(columns={'level_1': 'variable'})

# Create a chart that shows the value counts of the categorical features using seaborn's catplot().
sns.catplot(
    x = 'variable',
    y = 'value',
    hue = 'cardio',
    kind = 'count',
    data = long_df
)

# Rotate x labels to prevent overlapping.
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.25)
plt.show()
