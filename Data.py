import streamlit as st
import numpy as np
import pandas as pd
import mysql.connector






st.title("Data")
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="1234",    
    database="project"
)
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS project")
if conn.is_connected():
    print("MySQL database 'Project' created successfully!")
cursor.execute("use project")



cursor.execute("CREATE DATABASE IF NOT EXISTS project")






SHOW_PROV_DATA = st.button("Providers Data")
REC_PROV_DATA = st.button("RECEIVERS Data")
FOOD_LIST_DATA = st.button("FOOD LISTNER data")
CLAIM_DATA = st.button("CLAIMS data")

if SHOW_PROV_DATA:
    st.write("Providers data")
    cursor.execute("select * from food_providers")
    data = cursor.fetchall()
    st.dataframe(data)
if REC_PROV_DATA:
    st.write("RECEIVERS DATA")
    cursor.execute("select * from food_receivers")
    data = cursor.fetchall()
    st.dataframe(data)
if FOOD_LIST_DATA:
    st.write("FOOD LIST data")
    cursor.execute("select * from food_listing")
    data = cursor.fetchall()
    st.dataframe(data)
if CLAIM_DATA:
    st.write("CLAIM data")
    cursor.execute("select * from claims_data")
    data = cursor.fetchall()
    st.dataframe(data)   
    

    
