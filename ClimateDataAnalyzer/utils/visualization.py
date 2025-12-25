import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def plot_line_chart(dataframe, x_column, y_column):
    plt.figure(figsize=(10, 5))
    plt.plot(dataframe[x_column], dataframe[y_column])
    plt.title(f'Trend of {y_column} over {x_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close()
    return plot_url

def plot_bar_chart(dataframe, x_column, y_column):
    plt.figure(figsize=(10, 5))
    plt.bar(dataframe[x_column], dataframe[y_column])
    plt.title(f'Bar Chart of {y_column} by {x_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close()
    return plot_url

def plot_histogram(dataframe, column):
    plt.figure(figsize=(10, 5))
    plt.hist(dataframe[column], bins=20, edgecolor='black')
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close()
    return plot_url