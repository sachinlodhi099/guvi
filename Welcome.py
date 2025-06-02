import streamlit as st
import numpy as np
import pandas as pd
import mysql.connector
import time
import datetime

st.set_page_config(
    page_title="Welcome to My Mini Project",
    page_icon="🚀",
    layout="centered"
)
st.image("guvi_logo.jpg", width=150 )
st.write("This is my mini project.")

st.markdown(
    """
    <div style="text-align:center;">
        <h1 style='color:#2F4F4F;'>Food waste management system project </h1>
        
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    ### 📌 Project Overview
    This mini project is designed to demonstrate the use of Python , SQL Server, Steamlit for building fast and interactive data-driven web applications.
    """,
    unsafe_allow_html=True
)



if st.button("👉 Get Started"):
    st.success("Let’s Begin!")
    


st.markdown(
    """
    <hr style="border: 1px solid #ddd;">
    <div style="text-align:center; font-size: 14px;">
        Project submitted by Sachin Lodhi
    </div>
    """,
    unsafe_allow_html=True
)
providers = pd.read_csv("C:/Users/User/Desktop/python/PYTHON_PROJECT/providers_data.csv")
receivers = pd.read_csv("C:/Users/User/Desktop/python/PYTHON_PROJECT/receivers_data.csv")
food_listings = pd.read_csv("C:/Users/User/Desktop/python/PYTHON_PROJECT/food_listings_data.csv")
claims = pd.read_csv("C:/Users/User/Desktop/python/PYTHON_PROJECT/claims_data.csv")

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



time.sleep(1)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Food_Providers (
        Provider_ID INT PRIMARY KEY,
        Name VARCHAR(255),
        Type VARCHAR(100),
        Address TEXT,
        City VARCHAR(100),
        Contact VARCHAR(50)
    )
""")
conn.commit()
for index, row in providers.iterrows():
    cursor.execute("""
        INSERT INTO Food_Providers (Provider_ID, Name, Type, Address, City, Contact) 
        VALUES (%s, %s, %s, %s, %s, %s)
    """, tuple(row))

time.sleep(1)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Food_Receivers (
        Receiver_ID INT PRIMARY KEY,
        Name VARCHAR(255),
        Type VARCHAR(100),
        City VARCHAR(100),
        Contact VARCHAR(50)
    )
""")
conn.commit()


for index, row in receivers.iterrows():
    cursor.execute("""
        INSERT INTO Food_Receivers (Receiver_ID, Name, Type, City, Contact) 
        VALUES (%s, %s, %s, %s, %s)
    """, tuple(row))

time.sleep(1)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Food_listing (
        Food_ID INT PRIMARY KEY,
        Food_Name VARCHAR(255),
        Quantity INT,
        Expiry_Date TEXT,
        Provider_ID INT,
        Provider_Type VARCHAR(100),
        Location VARCHAR(100),
        Food_Type VARCHAR(100),
        Meal_Type VARCHAR(100)
    )
""")
conn.commit()

for index, row in food_listings.iterrows():
    cursor.execute("""
        INSERT INTO Food_listing (Food_ID, Food_Name, Quantity, Expiry_Date, Provider_ID, Provider_Type, Location, Food_Type, Meal_Type) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))
time.sleep(1)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Claim_data (
        Claim_ID INT PRIMARY KEY,
        Food_ID INT,
        Receiver_ID INT,
        Status TEXT,
        TimeStamp TEXT
    )
""")
conn.commit()

time.sleep(1)
for index, row in claims.iterrows():
    timestamp = datetime.now().strftime('%D-%m-%Y %H:%M')
    cursor.execute("""
        INSERT INTO Claim_data (Claim_ID, Food_ID, Receiver_ID, Status, Timestamp) 
        VALUES (%s, %s, %s, %s, %s)
    """, tuple(row))

conn.close()