import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
url = "https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/bike_sharing.csv"
df = pd.read_csv(url)

# Debugging step: check column names
st.write("Columns in the dataset:", df.columns)

# Ensure the date column is properly formatted
if 'dteday' in df.columns:  # Check if the column exists
    df['dteday'] = pd.to_datetime(df['dteday'])  # Convert to datetime
    df['day'] = df['dteday'].dt.day  # Extract day
else:
    st.error("The dataset does not have a column named 'dteday'. Please check the dataset structure.")

# Streamlit App Title
st.title("Bike Sharing Analysis")

# Create a line plot of total ridership over the entire period
st.subheader("Line Plot: Total Ridership Over Time")
if 'cnt' in df.columns:  # Ensure the column exists
    fig, ax = plt.subplots()
    ax.plot(df['dteday'], df['cnt'], label="Total Ridership")
    ax.set_title("Total Ridership Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Ridership Count")
    ax.legend()
    st.pyplot(fig)
else:
    st.error("The dataset does not have a column named 'cnt'. Please check the dataset structure.")

# Create a bar chart for total ridership by season
st.subheader("Bar Chart: Total Ridership by Season")
if 'season' in df.columns and 'cnt' in df.columns:  # Ensure columns exist
    season_ridership = df.groupby('season')['cnt'].sum()
    fig, ax = plt.subplots()
    season_ridership.plot(kind='bar', ax=ax)
    ax.set_title("Total Ridership by Season")
    ax.set_xlabel("Season (1 = Winter, 2 = Spring, 3 = Summer, 4 = Fall)")
    ax.set_ylabel("Total Ridership")
    st.pyplot(fig)
else:
    st.error("The dataset does not have the required columns ('season' or 'cnt').")

# Create a line plot for total ridership with a rolling average
st.subheader("Line Plot: Total Ridership with Rolling Average")
if 'cnt' in df.columns:
    rolling_option = st.radio(
        "Select Rolling Average:",
        options=["7-day average", "14-day average"]
    )
    window = 7 if rolling_option == "7-day average" else 14
    df['rolling_avg'] = df['cnt'].rolling(window=window).mean()
    fig, ax = plt.subplots()
    ax.plot(df['dteday'], df['cnt'], label="Daily Ridership")
    ax.plot(df['dteday'], df['rolling_avg'], label=f"{window}-Day Rolling Average", linestyle='--')
    ax.set_title("Total Ridership with Rolling Average")
    ax.set_xlabel("Date")
    ax.set_ylabel("Ridership Count")
    ax.legend()
    st.pyplot(fig)
else:
    st.error("The dataset does not have a column named 'cnt'. Please check the dataset structure.")
