import streamlit as st
import pandas as pd
import numpy as np
import tokenize
import base64
from pathlib import Path

st.set_page_config(
    page_title="Home",
    page_icon=":earth_africa:",
)

def load_bootstrap():
    return st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

st.sidebar.markdown(
    '''
        <div style="border: thin solid white    ; border-radius: 5px;">
            <div style="background-image: url(data:image/png;base64,{}); background-repeat: no-repeat; height: 125px;">
                <a href='https://github.com/aakashmohole' style="position: absolute; z-index: 2; top: 50px; left: 20px;">
                    <img src="https://skillicons.dev/icons?i=github" alt="GitHub"/>
                </a>
                <h1 style="color: rgb(224, 224, 224); position: absolute; z-index: 2; left: 85px; font-family: sans-serif;">QuoteFusion 🍂 Quote Genration using LSTM</h1>
            </div>
            <div style="margin-top: 40px">
                <a href="https://github.com/aakashmohole/QuoteFusion-Quote-Genration-using-LSTM" style="position: absolute; z-index: 2; top: 131px; left: 35px">
                    <img src="https://img.shields.io/badge/github-repo-white" alt="repo"/>
                </a>
                <a href="https://colab.research.google.com/drive/1F5phX4Ud2AL-gC9qoggvJELOfXMkPAMM#scrollTo=8w_2ZWu2-9E3&uniqifier=1" style="position: absolute; z-index: 2; top: 131px; right: 35px">
                    <img src="https://img.shields.io/badge/colab-notebook-orange" alt="repo"/>
                </a>
            </div>
        </div>
    '''.format(img_to_bytes('./icons/cover.jpg')),
    unsafe_allow_html=True)


# Create tabs in the sidebar
dev, link, doc = st.sidebar.tabs(["Devloper", "Links", "Doc"])
tab1, tab2, tab3 = st.tabs(["Home", "Quote Generation", "Translation"])

# Create tab for home
with tab1:       
    with st.container():
        st.title("QuoteFusion 🍂 Quote Genration using LSTM ")
        st.markdown('#')
        st.markdown("Introducing QuoteFusion 🍂 : Harnessing the power of AI to generate and translate inspiring quotes seamlessly.")
        st.caption('> Unlock the wisdom of words in any language with our cutting-edge Transformers pipeline.')
        st.caption("""> Tip: QuoteFusion seamlessly creates original quotes and translates them across multiple languages. 
                Experience the power of words, reimagined with cutting-edge AI. Perfect for global audiences and content creators.""")

        st.markdown('---')

        col1, col2, col3 = st.columns(3, gap='large')
        with col1:
            st.empty()
            st.markdown("<a href='https://docs.streamlit.io/library/get-started'><img src='data:image/png;base64,{}' class='img-fluid' width=100%/></a>".format(img_to_bytes('./icons/streamlit.png')), unsafe_allow_html=True)
        with col2:
            st.markdown("<a href='https://developers.themoviedb.org/3/getting-started/introduction'><img src='data:image/png;base64,{}' class='img-fluid' width=60%/></a>".format(img_to_bytes('./icons/beautifulsoup.png')), unsafe_allow_html=True)
        with col3:
            st.markdown("<a href='https://colab.research.google.com/drive/1J6hg-FvonxtgzQ71MNr11md5gFtiqmZV?usp=share_link'><img src='data:image/png;base64,{}' class='img-fluid' width=50%/></a>".format(img_to_bytes('./icons/colab.png')), unsafe_allow_html=True)
            
# Quote Generation tab content
with tab2:
    st.write("Generate inspirational quotes using LSTM models.")
    # Add more functionality for quote generation here

# Translation tab content
with tab3:
    st.write("Translate quotes into different languages using Transformers.")
    # Add more functionality for translation here 
