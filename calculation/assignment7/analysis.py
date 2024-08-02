import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from data_cleaning  import clean_data, load_data
from filehandling import load_cleaned_data, save_cleaned_data
from exceptions import DataCleaningError

file_name = "country_wise_latest.csv"
cleaned_file_name = "clean_covid_data.csv"

try:
    df = load_data(file_name)
    st.write("Original Data Overview")
    st.write(df.head())
    
    df = clean_data(df)
    save_cleaned_data(cleaned_file_name,df)
    
    st.write('Cleaned Data Overview')
    df = load_cleaned_data(cleaned_file_name)
    st.write(df.head())
except DataCleaningError as e:
    st.error(f"Data Cleaning Error: {e.message}")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")
        
total_cases = df['Confirmed'].sum()
total_deaths = df['Deaths'].sum()
total_recovered = df['Recovered'].sum()

st.subheader("_Globally_")
st.write("Total Cases:", total_cases)
st.write("Total Deaths:", total_deaths)
st.write("Total Recovered:", total_recovered)

show_top_bottom = st.button("Show top/bottom 5 countries/states by cases")

if show_top_bottom:
    country_cases = df.groupby("Country/Region")["Confirmed"].sum().reset_index()
    country_cases = country_cases.sort_values("Confirmed", ascending=False)

    st.write("Top 5 countries/states by cases:")
    top_5 = country_cases.head(5)
    st.write(top_5)

    st.write("Bottom 5 countries/states by cases:")
    bottom_5 = country_cases.tail(5)
    st.write(bottom_5)

    fig_top, ax_top = plt.subplots(figsize=(10, 6))
    ax_top.bar(top_5["Country/Region"], top_5["Confirmed"], color='skyblue')
    ax_top.set_xlabel("Country/Region")
    ax_top.set_ylabel("Confirmed Cases")
    ax_top.set_title("Top 5 Countries/Regions by Confirmed Cases")
    st.pyplot(fig_top)

    fig_bottom, ax_bottom = plt.subplots(figsize=(10, 6))
    ax_bottom.bar(bottom_5["Country/Region"], bottom_5["Confirmed"], color='skyblue')
    ax_bottom.set_xlabel("Country/Region")
    ax_bottom.set_ylabel("Confirmed Cases")
    ax_bottom.set_title("Bottom 5 Countries/Regions by Confirmed Cases")
    st.pyplot(fig_bottom)