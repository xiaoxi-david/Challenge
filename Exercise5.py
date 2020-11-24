import streamlit as st
import pandas as pd

# Ordered list of pairs airports/passengers
path_grouped_bookings = "../Data/grouped_bookings.csv"

# Webpage
st.title("Airports with more passengers in 2013")
st.markdown("Please insert the number of TOP airports you want to get.")

n = st.text_input("Insert a number:")

if n:
    n = int(n, base=10)
    airports_per_passengers = pd.read_csv(path_grouped_bookings, sep="^")
    rqst = airports_per_passengers.head(n).to_json()
    st.write(rqst)
