import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def draw_line_plot(df, title, x_label, y_label):
    """Draws a line chart using Matplotlib.

    Args:
        df: A Pandas DataFrame containing the data to plot.
        title: The title of the chart.
        x_label: The label for the x axis.
        y_label: The label for the y axis.
    """

    fig, ax = plt.subplots()
    ax.plot(df.index, df['page_views'], label='Page Views')
    ax.set(title=title, xlabel=x_label, ylabel=y_label)
    ax.legend()
    plt.show()

def draw_bar_plot(df, title, x_label, y_label):
    """Draws a bar chart using Matplotlib.

    Args:
        df: A Pandas DataFrame containing the data to plot.
        title: The title of the chart.
        x_label: The label for the x axis.
        y_label: The label for the y axis.
    """

    fig, ax = plt.subplots()
    df.groupby('year')['page_views'].mean().plot(kind='bar', label='Page Views')
    ax.set(title=title, xlabel=x_label, ylabel=y_label)
    ax.legend()
    plt.show()

def draw_box_plot(df, title, x_label, y_label):
    """Draws a box plot using Seaborn.

    Args:
        df: A Pandas DataFrame containing the data to plot.
        title: The title of the chart.
        x_label: The label for the x axis.
        y_label: The label for the y axis.
    """

    fig, ax = plt.subplots()
    sns.boxplot(
        x = 'year',
        y = 'page_views',
        showmeans=True,
        data=df
    )
    ax.set(title=title, xlabel=x_label, ylabel=y_label)
    plt.show()

if __name__ == '__main__':
    # Read the data from the CSV file.
    df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')

    # Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
    df = df[df['page_views'].between(df['page_views'].quantile(0.025), df['page_views'].quantile(0.975))]

    # Create a copy of the data frame for each chart.
    df_line = df.copy()
    df_bar = df.copy()
    df_box = df.copy()

    # Draw the line chart.
    draw_line_plot(df_line, 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019', 'Date', 'Page Views')

    # Draw the bar chart.
    draw_bar_plot(df_bar, 'Average Daily Page Views by Month and Year', 'Years', 'Average Page Views')

    # Draw the box plots.
    draw_box_plot(df_box, 'Year-wise Box Plot (Trend)', 'Year', 'Page Views')
    draw_box_plot(df_box, 'Month-wise Box Plot (Seasonality)', 'Month', 'Page Views')
