import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def plot_temperature_trend(dataframe):
    plt.figure(figsize=(10, 5))
    plt.plot(dataframe['Date'], dataframe['Temperature'], label='Temperature Trend', color='blue')
    plt.title('Temperature Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.grid(True)
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return plot_url

def plot_precipitation_trend(dataframe):
    plt.figure(figsize=(10, 5))
    plt.bar(dataframe['Date'], dataframe['Precipitation'], label='Precipitation Trend', color='green')
    plt.title('Precipitation Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Precipitation (mm)')
    plt.legend()
    plt.grid(True)
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return plot_url

def plot_co2_levels(dataframe):
    plt.figure(figsize=(10, 5))
    plt.plot(dataframe['Year'], dataframe['CO2'], label='CO2 Levels', color='red')
    plt.title('CO2 Levels Over Years')
    plt.xlabel('Year')
    plt.ylabel('CO2 Concentration (ppm)')
    plt.legend()
    plt.grid(True)
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return plot_url

def create_interactive_chart(dataframe, x_column, y_column, chart_type='line'):
    plt.figure(figsize=(10, 5))
    if chart_type == 'line':
        plt.plot(dataframe[x_column], dataframe[y_column], label=f'{y_column} over {x_column}', color='purple')
    elif chart_type == 'bar':
        plt.bar(dataframe[x_column], dataframe[y_column], label=f'{y_column} over {x_column}', color='orange')
    plt.title(f'{y_column} Trend Over {x_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.legend()
    plt.grid(True)
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return plot_url