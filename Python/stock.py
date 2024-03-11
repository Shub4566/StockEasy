# import numpy as np
# import pandas as pd
# import yfinance as yf
# from keras.models import load_model

# import streamlit as st
# import matplotlib.pyplot as plt

# model = load_model('D:\Python\Stock Predictions.keras')

# st.header('Stock Market Predictor')

# stock =st.text_input('Enter Stock Symnbol', 'GOOG')
# start = '2012-01-01'
# end = '2022-12-31'

# data = yf.download(stock, start ,end)

# st.subheader('Stock Data')
# st.write(data)

# data_train = pd.DataFrame(data.Close[0: int(len(data)*0.80)])
# data_test = pd.DataFrame(data.Close[int(len(data)*0.80): len(data)])

# from sklearn.preprocessing import MinMaxScaler
# scaler = MinMaxScaler(feature_range=(0,1))

# pas_100_days = data_train.tail(100)
# data_test = pd.concat([pas_100_days, data_test], ignore_index=True)
# data_test_scale = scaler.fit_transform(data_test)

# st.subheader('Price vs MA50')
# ma_50_days = data.Close.rolling(50).mean()
# fig1 = plt.figure(figsize=(8,6))
# plt.plot(ma_50_days, 'r')
# plt.plot(data.Close, 'g')
# plt.show()
# st.pyplot(fig1)

# st.subheader('Price vs MA50 vs MA100')
# ma_100_days = data.Close.rolling(100).mean()
# fig2 = plt.figure(figsize=(8,6))
# plt.plot(ma_50_days, 'r')
# plt.plot(ma_100_days, 'b')
# plt.plot(data.Close, 'g')
# plt.show()
# st.pyplot(fig2)

# st.subheader('Price vs MA100 vs MA200')
# ma_200_days = data.Close.rolling(200).mean()
# fig3 = plt.figure(figsize=(8,6))
# plt.plot(ma_100_days, 'r')
# plt.plot(ma_200_days, 'b')
# plt.plot(data.Close, 'g')
# plt.show()
# st.pyplot(fig3)

# x = []
# y = []

# for i in range(100, data_test_scale.shape[0]):
#     x.append(data_test_scale[i-100:i])
#     y.append(data_test_scale[i,0])

# x,y = np.array(x), np.array(y)

# predict = model.predict(x)

# scale = 1/scaler.scale_

# predict = predict * scale
# y = y * scale

# st.subheader('Original Price vs Predicted Price')
# fig4 = plt.figure(figsize=(8,6))
# plt.plot(predict, 'r', label='Original Price')
# plt.plot(y, 'g', label = 'Predicted Price')
# plt.xlabel('Time')
# plt.ylabel('Price')
# plt.show()
# st.pyplot(fig4)


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


    
   