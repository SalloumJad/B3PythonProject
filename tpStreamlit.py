from encodings import utf_8
import streamlit as st
import requests
import pandas as pd
import numpy as np

# Le get n'arrive pas a détecter les données, donc je part directement du csv ici.
#response = requests.get("http://127.0.0.1:5000/1")
data_table1 = pd.read_csv('result.csv')

#def load_data() :
#    data = pd.read_json('http://127.0.0.1:5000')
#    return data

#df = load_data()
#st.dataframe(df)
#print(response.json())
#data_table1 = pd.DataFrame(response.json())

st.title('Genius discographie rap Francais 2021')

option = st.text_input("Entrez un mot a rechercher")

#options = st.multiselect('Entrez un mot a rechercher', ['title'])

st.dataframe(data_table1)