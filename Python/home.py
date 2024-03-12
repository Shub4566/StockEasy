import streamlit as st
from firebase_admin import firestore

def app():
    st.sidebar.header('')
    st.markdown(
    """
    <style>
    .heading {
        font-size: 24px;
        font-weight: bold;
        color: #FFD700; /* Golden color */
        margin-bottom: 20px;
    }
    .paragraph {
        font-size: 18px;
        color: #00FF00; /* Neon green color */
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Section content
    st.markdown("<p class='heading'>Welcome to the Social Lounge!</p>", unsafe_allow_html=True)
    st.markdown("<p class='paragraph'>We at StockEasy welcome you to the platform and look forward to your active participation in the community discussion. Please be respectful and share your valuable information and experiences with newcomers on the platform.</p>", unsafe_allow_html=True)
    st.header("")
    st.header("")
    
    if 'db' not in st.session_state:
        st.session_state.db = ''

    db = firestore.client()
    st.session_state.db = db

    ph = ''
    if st.session_state.username == '':
        ph = 'Login to be able to post!!'
    else:
        ph = 'Post your thought'

    post = st.text_area(label=':orange[+ New Post]', placeholder=ph, height=None, max_chars=10000)
    if st.button('Post', use_container_width=20):
        if post != '':
            info = db.collection('Posts').document(st.session_state.username).get()
            if info.exists:
                info = info.to_dict()
                if 'Content' in info.keys():
                    pos = db.collection('Posts').document(st.session_state.username)
                    pos.update({u'Content': firestore.ArrayUnion([u'{}'.format(post)])})
                else:
                    data = {"Content": [post], 'Username': st.session_state.username}
                    db.collection('Posts').document(st.session_state.username).set(data)
            else:
                data = {"Content": [post], 'Username': st.session_state.username}
                db.collection('Posts').document(st.session_state.username).set(data)

            st.success('Post uploaded!!')

    st.header(':violet[All Posts] ')

    docs = db.collection('Posts').get()

    # Reverse the order of documents
    docs = reversed(docs)

    for doc in docs:
        d = doc.to_dict()
        try:
            for post_content in reversed(d['Content']):
                st.text_area(label=':green[Posted by:] ' + ':orange[{}]'.format(d['Username']),
                            value=post_content, height=200, key=f"{doc.id}_{post_content}")
        except:
            pass
