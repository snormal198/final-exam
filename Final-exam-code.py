import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data_url = "https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/bike_sharing.csv"
df = pd.read_csv(data_url)

# Convert date column to datetime if it exists
df['day'] = pd.to_datetime(df['day'])

# Streamlit app
st.title("Bike Sharing Data Visualization")

# Line Plot: Total Ridership Over Time
st.subheader("Total Ridership Over Time")
fig, ax = plt.subplots()
ax.plot(df['day'], df['cnt'], label='Total Ridership', color='blue')
ax.set_xlabel("Date")
ax.set_ylabel("Total Ridership")
ax.set_title("Total Ridership Over Time")
ax.legend()
st.pyplot(fig)

# Bar Chart: Total Ridership by Season
st.subheader("Total Ridership by Season")
season_map = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}
df['season_name'] = df['season'].map(season_map)
season_data = df.groupby('season_name')['cnt'].sum().reset_index()
fig, ax = plt.subplots()
ax.bar(season_data['season_name'], season_data['cnt'], color=['blue', 'green', 'orange', 'red'])
ax.set_xlabel("Season")
ax.set_ylabel("Total Ridership")
ax.set_title("Total Ridership by Season")
st.pyplot(fig)

# Interactive Line Plot: Rolling Average
st.subheader("Rolling Average for Total Ridership")
average_option = st.radio("Select Rolling Average:", options=["7-day", "14-day"])
window = 7 if average_option == "7-day" else 14
df[f'{window}-day_avg'] = df['cnt'].rolling(window=window).mean()

fig, ax = plt.subplots()
ax.plot(df['day'], df['cnt'], label='Original Data', color='lightgray')
ax.plot(df['day'], df[f'{window}-day_avg'], label=f'{window}-Day Average', color='blue')
ax.set_xlabel("Date")
ax.set_ylabel("Total Ridership")
ax.set_title(f"Total Ridership with {window}-Day Rolling Average")
ax.legend()
st.pyplot(fig)

# Notes for Submission
st.info("Submit this Python script and screenshots of the app running with different visualizations.")
