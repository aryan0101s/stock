import App2realtime as Ap
import tatasteel as Ta
import Tesla_Final  as Te


import streamlit as st
import pandas as pd
import plotly.graph_objects as go


def date(a):
    d=a.forecasted_dates
    return  d.tolist()

def forecast(b):
    p=b.forecasted_prices
    return p.tolist()

def actual(c):
    ac=c.quote2['Actual Price']
    return ac.tolist()

# Sample stock data
def load_stock_data():
    return {
        "Tesla": pd.DataFrame({
            "Date": date(Te),
            "Actual Price": actual(Te),
            "Forecasted Price": forecast(Te)
        }),
        "Tata": pd.DataFrame({
            "Date": date(Ta),
            "Actual Price": actual(Ta),
            "Forecasted Price": forecast(Ta)
        }),
        "Apple": pd.DataFrame({
            "Date":date(Ap),
            "Actual Price": actual(Ap),
            "Forecasted Price": forecast(Ap)
        }),
    }

# Load stock data
stock_data = load_stock_data()

# Streamlit App Layout
st.title("Stock Price Comparison")

# Sidebar for stock selection
stock_selection = st.sidebar.selectbox("Select Stock", options=list(stock_data.keys()))

# Get the selected stock data
selected_stock_data = stock_data[stock_selection]

# Display the stock name
st.header(f"{stock_selection} Stock Prices")

# Show data in table format
st.subheader("Data Table")
st.dataframe(selected_stock_data)
