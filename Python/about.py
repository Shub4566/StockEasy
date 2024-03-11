import streamlit as st
from annotated_text import annotated_text

def app() :
    st.sidebar.header('')
    st.markdown(
        """
        <style>
        .title {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 20px;
            color: #FFD700; 
        }
        .subtitle {
            font-size: 20px;
            font-weight: bold;
            margin-top: 20px;
            margin-bottom: 10px;
            color: #00FF00;
        }
        .point {
            margin-left: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # About section
    st.markdown("<p class='title'>About StockEasy</p>", unsafe_allow_html=True)
    st.write("""
    StockEasy is a cutting-edge web application conceived and developed by Mohit Kumar Singh, Shubham Singh, Parth Goswami, and Kaushik Sharma,all fourth-year students pursuing B.Tech in the Faculty of Engineering and Technology at the University of Lucknow. This innovative platform specializes in real-time stock analysis and forecasting, leveraging the powerful SARIMA model to predict future stock prices with precision.

    The project boasts a robust user authentication system, allowing seamless access to its community page. Here, traders and experts converge to share insights, strategies, and valuable information, fostering an environment conducive to learning and collaboration. StockEasy isn't just about predictions; it's about building a community of traders who can leverage collective wisdom to make informed decisions.
    """)

    # What This Project Aims to Deliver
    st.markdown("<p class='subtitle'>What This Project Aims to Deliver</p>", unsafe_allow_html=True)
    st.write("""
    - <span class='point'>SARIMA Model for Forecasting and Analysis:</span> Leveraging advanced statistical techniques for accurate stock price predictions and insightful analysis.
    - <span class='point'>User Authentication:</span> A secure login, logout, and signup feature ensuring only authorized users access the platform's features.
    - <span class='point'>Community Engagement:</span> A vibrant community platform where traders can interact, share insights, and learn from each other's experiences.
    - <span class='point'>New User Onboarding:</span> Providing resources and tools to help new traders navigate the complexities of stock trading and analysis.
    - <span class='point'>User-Friendly UI:</span> An intuitive interface designed to facilitate a smooth learning curve for novice traders, ensuring an enjoyable learning experience.
    """, unsafe_allow_html=True)

    # Technology Used
    st.markdown("<p class='subtitle'>Technology Used</p>", unsafe_allow_html=True)
    st.write("""
    - <span class='point'>Streamlit:</span> Employed for the creation of the web application, ensuring an interactive and dynamic user experience.
    - <span class='point'>SARIMA Model:</span> Powering the predictive analytics capabilities of the platform, enabling accurate forecasting and analysis.
    - <span class='point'>Firebase Database:</span> Serving as the backend database, ensuring efficient data management and retrieval.
    - <span class='point'>User Authentication:</span> Leveraging Firebase authentication services to secure user accounts and data.
    - <span class='point'>Python (with yfinance library):</span> Utilized for backend processing and data analysis, harnessing the capabilities of the yfinance library for stock data retrieval and manipulation.
    """, unsafe_allow_html=True)


    st.header("")
    st.header("")
    st.header("")

    annotated_text(
    "Community platform where traders can interact, share insights, and learn from each other's experiences",
    ("Community platform", "noun"),
    " where ",
    ("traders", "noun"),
    " can ",
    ("interact", "verb"),
    ", ",
    ("share insights", "verb"),
    ", and ",
    ("learn from each other's experiences", "verb")
)
