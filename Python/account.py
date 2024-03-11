import streamlit as st
import firebase_admin

from firebase_admin import credentials
from firebase_admin import auth


cred = credentials.Certificate('stockeasy-f3ac0-140c00ab9b02.json')
firebase_admin.initialize_app(cred)
    



#if not firebase_admin._apps:
    # cred = credentials.Certificate('path/to/serviceAccountKey.json') 
    # default_app = firebase_admin.initialize_app(cred)

def app() :
    

    st.title('Welcome to :violet[StockEasy]')
    st.sidebar.header('')

    

    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''



    def f():
        try:
            user = auth.get_user_by_email(email)
            # password = auth.get_user_by_email(password)
            # password = auth.get_user_by_passsword(password)
            st.write('Login Successful')

            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            st.session_state.signedout = True
            st.session_state.signout = True

        except:
            st.warning('Login Failed')

    def t():
        st.session_state.signout = False
        st.session_state.signedout = False
        st.session_state.username = ''
            
    if 'signedout' not in st.session_state:
        st.session_state.signedout = False
    if 'signout' not in st.session_state:
        st.session_state.signout = False

    
    if not st.session_state['signedout']:
        choice = st.selectbox('Login/Signup', ['Login', 'Sign Up'])
    

        if choice=='Login':

            email=st.text_input('Email Address')
            password=st.text_input('Password', type='password')
            phone_number = st.text_input('Phone Number')
            
            st.button('Login', on_click=f)


        else:

            email=st.text_input('Email Address')
            password=st.text_input('Password', type='password')
            phone_number = st.text_input('Phone Number')

            username = st.text_input('Enter Your Unique Username')

            if st.button('Create my account'):
                user = auth.create_user(email = email, password = password, uid = username)

                st.success('Account Created Successfully!')
                st.markdown('Please Login Using Your Email and Password')
                st.balloons()

    if st.session_state.signout:
        st.text('Name: ' + st.session_state.username)
        st.text('Email id: ' + st.session_state.useremail)
        st.button('Sign out',on_click=t)
    