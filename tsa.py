# import the needed libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.seasonal import seasonal_decompose



# Load the dataset
df = pd.read_csv('E:\Experimental Projects\Compu-J\data\song18.csv')

# Display the first few rows of the dataset
print(df.head())

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# If needed, convert the 'Offset' column from scientific notation to float
df['Offset'] = df['Offset'].astype(float)

# Display the data types to ensure they are correct
print(df.dtypes)

# some basic EDA
print(df.describe())

# some visualisation
plt.figure(figsize = (10, 6))
sns.histplot(df['Offset'], bins = 50, kde = True)
plt.title('Distribution of Offsets')
plt.xlabel('Offset (seconds)')
plt.ylabel('Frequency')
plt.show()

# Plot the number of Shazam queries over time
plt.figure(figsize=(10, 6))
df['Date'].value_counts().sort_index().plot()
plt.title('Number of Shazam Queries Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Queries')
plt.show()

# Time Series Analysis
# Aggregate the number of queries by date
time_series = df['Date'].value_counts().sort_index()

# Plot the time series
plt.figure(figsize=(10, 6))
time_series.plot()
plt.title('Number of Shazam Queries Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Queries')
plt.show()

# advanced analysis

# Decompose the time series
decomposition = seasonal_decompose(time_series, model='additive', period=30)
decomposition.plot()
plt.show()


########################
# using SARIMAX
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Assuming time_series is your prepared time series data
# Convert to DataFrame if it's a Series
if isinstance(time_series, pd.Series):
    time_series = time_series.to_frame(name='y')

# Fit the SARIMA model
model = SARIMAX(time_series, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
results = model.fit()

# Make predictions
forecast = results.get_forecast(steps=30)
forecast_ci = forecast.conf_int()

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(time_series.index, time_series, label='Observed')
plt.plot(forecast.predicted_mean.index, forecast.predicted_mean, color='r', label='Forecast')
plt.fill_between(forecast_ci.index, forecast_ci.iloc[:, 0], forecast_ci.iloc[:, 1], color='r', alpha=0.1)
plt.title('SARIMA Forecast of Shazam Queries')
plt.xlabel('Date')
plt.ylabel('Number of Queries')
plt.legend()
plt.show()

# Print the forecast
print(forecast.predicted_mean)
