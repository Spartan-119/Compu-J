# import the needed libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('E:\Experimental Projects\Compu-J\data\song18.csv')

# Display the first few rows of the dataset
print(df.head())

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%y')

# If needed, convert the 'Offset' column from scientific notation to float
df['Offset'] = df['Offset'].astype(float)

# Display the data types to ensure they are correct
print(df.dtypes)