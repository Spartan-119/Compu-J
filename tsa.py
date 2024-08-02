import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.signal import find_peaks
from statsmodels.tsa.seasonal import seasonal_decompose

# Creating the Analysis folder where I will add the output of each song's analysis
if not os.path.exists("Analysis"):
    os.makedirs("Analysis")

# Function to perform the analyses
def analyze_song(file_path, song_name):
    # Read the data
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Create a directory for the song
    song_dir = os.path.join("Analysis", song_name)
    if not os.path.exists(song_dir):
        os.makedirs(song_dir)
    
    # 1. Popularity Trend Analysis
    df_trend = df.groupby(df['Date'].dt.date).size().reset_index()
    df_trend.columns = ['Date', 'Count']
    df_trend['Date'] = pd.to_datetime(df_trend['Date'])
    df_trend.set_index('Date', inplace=True)
    
    plt.figure(figsize=(10, 6))
    df_trend['Count'].plot(title=f'Popularity Trend for {song_name}', xlabel='Date', ylabel='Number of Queries')
    plt.savefig(os.path.join(song_dir, 'popularity_trend.png'))
    plt.close()
    
    # 2. Peak Detection
    peaks, _ = find_peaks(df_trend['Count'], distance=1)
    plt.figure(figsize=(10, 6))
    plt.plot(df_trend.index, df_trend['Count'], label='Query Count')
    plt.plot(df_trend.index[peaks], df_trend['Count'].iloc[peaks], "x", label='Peaks')
    plt.title(f'Peak Detection for {song_name}')
    plt.xlabel('Date')
    plt.ylabel('Number of Queries')
    plt.legend()
    plt.savefig(os.path.join(song_dir, 'peak_detection.png'))
    plt.close()
    
    # 3. Seasonal Patterns
    df_seasonal = df_trend['Count'].resample('D').sum()
    df_seasonal = df_seasonal.asfreq('D').fillna(0)
    
    # adding this checker to make sure we have sufficient data to perform seasonal decompose
    if len(df_seasonal) > 2:  
        decomposition = seasonal_decompose(df_seasonal, model='additive', period=7)  
        plt.figure(figsize=(10, 6))
        decomposition.seasonal.plot(title=f'Seasonal Patterns for {song_name}', xlabel='Date', ylabel='Seasonal Component')
        plt.savefig(os.path.join(song_dir, 'seasonal_patterns.png'))
        plt.close()
    else:
        print(f"Not enough data for seasonal decomposition for {song_name}")

# main starting point
data_folder = 'data'
song_numbers = list(range(1, 15)) + list(range(16, 22))  # Skipping 15 as i don't have it

for i in song_numbers:
    file_name = f'song{i:02d}.csv'
    file_path = os.path.join(data_folder, file_name)
    analyze_song(file_path, f'song{i:02d}')

print("Analysis completed and plots saved.")
