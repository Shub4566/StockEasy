
# import libraries
import streamlit as st
import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import datetime
from datetime import date, timedelta
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
#TITLE
def app():
#     with st.sidebar:
#         selected = option_menu("Stock Trend Predictor and Analysis Centre",["Analyse yourself", "Effective Chatbot Support"])
#         icons = ['house', 'cloud-upload']
#         menu_icon = "cast"
#     if selected == "Analyse yourself":
#             predictor.app()
#     elif selected == "Effective Chatbot Support":
#             chatbot.app()





# app()


    st.header("")
    st.header("")
    st.header("")
    st.write("""
<div style='text-align: center;'>
    <h2>Welcome to the Magic Section!</h2>
    <p>This is where the magic happens. Explore and discover the wonders of our platform.</p>
</div>
""", unsafe_allow_html=True)
    st.header("")
    st.header("")
  
    st.markdown(
    """
    <style>
   
    }
    .title {
        font-size: 24px;
        font-weight: bold;
        color: #FFFFFF; /* Adjusted text color to white */
        margin-bottom: 20px;
    }
    .text {
        font-size: 18px;
        color: #FFFFFF; /* Adjusted text color to white */
        margin-bottom: 10px;
    }
    .code {
        font-family: monospace;
        background-color: #e0e0e0;
        padding: 5px 10px;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Section content

    st.markdown("<p class='text'>Enter the ticker code of the company to get detailed stock information. For Example we have already used the Ticker code of GOOGLE as GOOG. Use your own ticker code of the company and get the analytics below.....</p>", unsafe_allow_html=True)

    st.sidebar.header('User Input Parameters')

    start_date = st.sidebar.date_input('Start Date', date(2020, 1, 1))
    end_date = st.sidebar.date_input('End Date', date(2021, 12, 31))

    #add ticker symbol list
    ticker = st.sidebar.text_input("Enter the Correct Stock Code of the Company","GOOG")
    
    
    
    st.header("")
    st.header("")
    #fetch data from yfinance library

    data = yf.download(ticker, start = start_date, end = end_date)
    data.insert(0, "Date", data.index, True)
    data.reset_index(drop = True, inplace = True) 
    st.write('Data from', start_date, 'to', end_date)
    st.write(data)
    

#PLOT THE DATA 
    st.header("DATA VISUALISATION")
    st.subheader('Plot of DATA')
    st.write("**NOTE:** Select Your Specific Data Range on the Sidebar, or Zoom in on the plot and select the specific column")
    fig = px.line(data, x = "Date", y = data.columns, title = "CLOSING PRICE OF STOCK", width=1450, height=600)
    st.plotly_chart(fig)


#ADD A SELECT BOX TO SELECT COLUMN FROM THE DATA 
    
    column = st.selectbox('Select the Column to be used for forecasting', data.columns[1:])

#SUBSETTING THE DATA
    
    data = data[['Date', column]]
    st.write("Selected Data")
    st.write(data)


    #ADF Test Check Stationarily

    st.subheader('Is the Data Stationary?')
    st.write("if value of p is less than 0.05, then data is stationary")
    st.write(adfuller(data[column])[1] < 0.05)

    # LETS DECOMPOSE THE DATA 

    st.header('Decomposition of the Data')
    decomposition = seasonal_decompose(data[column], model = 'additive', period = 12)
    # st.write(decomposition.plot())

# MAKING THE SAME PLOT IN PLOTLY
    st.write('Plotting the Decompostion in Plotly')
    st.plotly_chart(px.line(x = data["Date"], y = decomposition.trend, title = "Trend", width = 1450, height = 400, labels = {'x': 'Date', 'y': 'Price'}))
    st.plotly_chart(px.line(x = data["Date"], y = decomposition.seasonal, title = 'Seasonality', width = 1450, height=400, labels={'x': 'Date', 'y': 'Price'}))
    st.plotly_chart(px.line(x = data["Date"], y = decomposition.resid, title = 'Residuals', width = 1450, height=400, labels={'x': 'Date', 'y': 'Price'}))

    #LETS RUN THE MODEL
    #USER INPUT FOR THREE PARAMETERS OF THE MODEL AND SEASONAL ORDER

    p = st.slider('Select the Value of P', 0, 5, 2)
    d = st.slider('Select the value of d', 0, 5, 1)
    q = st.slider('Select the number of q', 0, 5, 2)
    seasonal_order = st.number_input('Select the value of seasonal p', 0, 24, 12)

    model = sm.tsa.statespace.SARIMAX(data[column], order = (p,d,q), seasonal_order=(p,d,q,seasonal_order))
    model = model.fit()

#PRINT MODEL SUMMARY
    st.header('Model Summary')
    st.write(model.summary())
    st.write("---")

#PREDICT THE VALUES AKA FORECASTING
    st.write("<p style = 'color:green; font-size: 50px; font-weight: bold;'> Forecasting the Data</p>", unsafe_allow_html=True)
    forecast_period = st.number_input('Select the number of days to forecast', 1, 365, 10)

    predictions = model.get_prediction(start = len(data), end = len(data) + forecast_period)
    predictions = predictions.predicted_mean
    # st.write(predictions)

    #add the index to the predictions
    predictions.index = pd.date_range(start = end_date, periods = len(predictions), freq = 'D')
    predictions = pd.DataFrame(predictions)
    predictions.insert(0, "Date", predictions.index, True)
    predictions.reset_index(drop = True, inplace = True)
    st.write("Predictions", predictions)
    st.write("Actual Data", data)
    st.write("---")

    #LETS PLOT THE DATA

    fig = go.Figure()
    fig.add_trace(go.Scatter(x = data["Date"], y = data[column], mode = 'lines', name = 'Actual', line = dict(color = 'blue')))
    fig.add_trace(go.Scatter(x = predictions["Date"], y = predictions["predicted_mean"], mode = 'lines', name = 'Predicted', line = dict(color = 'red')))
    fig.update_layout(title = 'Actual vs Predicted', xaxis_title = 'Date', yaxis_title = 'Price', width = 1450, height = 400)
    st.plotly_chart(fig)


    
   