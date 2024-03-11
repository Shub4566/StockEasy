import streamlit as st
from streamlit_option_menu import option_menu
import home, about,stock, Chatforums, account
from firebase_admin import credentials
from firebase_admin import auth
cred = credentials.Certificate('stockeasy-f3ac0-140c00ab9b02.json')
firebase_admin.initialize_app(cred)
    

st.set_page_config(
    page_title="StockEasy",
    layout="wide"  # Set layout to wide to occupy full width
)

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        selected = option_menu("StockEasy", ['About', 'Account', 'Your Posts', 'Stocks Trend Analytics', 'Social Lounge'],
                           icons=['person-rolodex', 'tencent-qq', 'chat', 'kanban', 'chat-fill'],
                           menu_icon='cast', default_index=1, orientation='horizontal', styles={
            "container": {"padding": "0px", "background-color": '#333333', "width": "80%", "display": "flex", "justify-content": "center"},
            "icon": {"color": "#ffffff", "font-size": "25px", "margin-right": "5px"},
            "nav-link": {"color": "#ffffff", "font-size": "18px", "text-align": "center", 
                         "width": "auto", "white-space": "nowrap", "margin": "5px 10px", "flex-grow": "1",
                         "border-bottom": "2px solid transparent", "transition": "border-color 0.3s ease", "font-weight": "normal"},
            "nav-link-selected": {"background-color": "#87CEEB", "border-bottom": "2px solid #87CEEB"},
            "nav-link:hover": {"color": "#cfe2f3", "text-decoration": "none"}
        })




        if selected == "Social Lounge":
            home.app()
        elif selected == "Account":
            account.app()
        elif selected == "Your Posts":
            Chatforums.app()
        elif selected == 'Stocks Trend Analytics':
            stock.app()
        elif selected == 'About':
            about.app()
    run()
