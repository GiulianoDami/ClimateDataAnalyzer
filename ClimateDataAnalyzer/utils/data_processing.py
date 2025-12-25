import pandas as pd
from io import StringIO

def read_data(file_content, file_type):
    if file_type == 'csv':
        return pd.read_csv(StringIO(file_content))
    elif file_type == 'json':
        return pd.read_json(StringIO(file_content))
    else:
        raise ValueError("Unsupported file type")

def calculate_average(dataframe, column_name):
    if column_name not in dataframe.columns:
        raise ValueError(f"Column {column_name} not found in dataframe")
    return dataframe[column_name].mean()

def identify_trend(dataframe, column_name):
    if column_name not in dataframe.columns:
        raise ValueError(f"Column {column_name} not found in dataframe")
    trend = dataframe[column_name].diff().mean()
    return "increasing" if trend > 0 else "decreasing" if trend < 0 else "stable"

def generate_report(dataframe, column_name):
    average = calculate_average(dataframe, column_name)
    trend = identify_trend(dataframe, column_name)
    report = f"Report for Column: {column_name}\n"
    report += f"Average Value: {average}\n"
    report += f"Trend: {trend}\n"
    return report