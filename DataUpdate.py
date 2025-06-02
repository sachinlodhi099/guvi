import streamlit as st
import numpy as np
import pandas as pd
import mysql.connector


st.title("Data Update / Monitoring")

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="1234",    
    database="project"
)
cursor = conn.cursor()


option = st.selectbox(
    "Select database to be update",
    ("Food Providers", "Food Recivers", "Food Listing", "Claims data"),
)
st.write("You selected:", option)
if option == 'Food Providers':
    Action = st.selectbox(
    "Select option",
    ("Create", "Update", "Read", "Delete")
    )

    if Action == 'Create':
     ID = st.number_input("Provider ID:",step=1)
     NAME = st.text_input("Name:")
     TYPE = st.text_input("Type:")
     ADD = st.text_input("Address:")
     CITY = st.text_input("City:")
     Contact = st.text_input("Contact:")
     PB_CREATE = st.button("Create")
     if PB_CREATE:

        cursor.execute(
          "INSERT INTO food_providers (Provider_ID, Name, Type, Address, City, Contact) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (ID, NAME, TYPE, ADD, CITY, Contact)
            )
        conn.commit();

    if Action == 'Update':
     ID = st.number_input("Provider ID:",step=1)
     NAME = st.text_input("Name:")
     TYPE = st.text_input("Type:")
     ADD = st.text_input("Address:")
     CITY = st.text_input("City:")
     Contact = st.text_input("Contact:")
     PB_UPDATE = st.button("UPDATE")
     if PB_UPDATE:

        query = "UPDATE food_providers SET Name = %s, Type = %s, Address = %s, City = %s, Contact = %s where provider_id = %s" 
        VAL = (NAME, TYPE, ADD, CITY, Contact, ID)
        cursor.execute(query, VAL)    
        conn.commit();


    if Action == 'Read':
     
     PB_READ = st.button("READ")
     if PB_READ:

        query = "SELECT * FROM FOOD_PROVIDERS" 
        
        cursor.execute(query) 
        DATA = cursor.fetchall()
        st.dataframe(DATA)   
        conn.commit();
    if Action == 'Delete':
     ID = st.number_input("Provider ID:",step=1)
     
     
     PB_DELETE = st.button("DELETE")
     if PB_DELETE:
        

        query = "DELETE FROM FOOD_PROVIDERS where provider_id = %s" 
        VAL = ( ID,  )
        cursor.execute(query, VAL) 
        DATA = cursor.fetchall()
        st.dataframe(DATA)   
        conn.commit();

# food receivers 
if option == 'Food Recivers':
    Action = st.selectbox(
    "Select option",
    ("Create", "Update", "Read", "Delete")
    )

    if Action == 'Create':
     ID = st.number_input("REC ID:",step=1)
     NAME = st.text_input("Name:")
     TYPE = st.text_input("Type:")
     CITY = st.text_input("City:")
     Contact = st.text_input("Contact:")
     PB_CREATE1 = st.button("Create")
     if PB_CREATE1:

        cursor.execute(
          "INSERT INTO food_receivers (receiver_ID, Name, Type, City, Contact) VALUES ('%s', '%s', '%s', '%s', '%s')" % (ID, NAME, TYPE, CITY, Contact)
            )
        conn.commit();

    if Action == 'Update':
     ID = st.number_input("REC ID:",step=1)
     NAME = st.text_input("Name:")
     TYPE = st.text_input("Type:")
     CITY = st.text_input("City:")
     Contact = st.text_input("Contact:")
     PB_UPDATE1 = st.button("UPDATE")
     if PB_UPDATE1:

        query = "UPDATE food_receivers SET Name = %s, Type = %s, City = %s, Contact = %s where receiver_id = %s" 
        VAL = (NAME, TYPE, CITY, Contact, ID)
        cursor.execute(query, VAL)    
        conn.commit();


    if Action == 'Read':
     
     PB_READ1 = st.button("READ")
     if PB_READ1:

        query = "SELECT * FROM FOOD_receivers" 
        
        cursor.execute(query) 
        DATA = cursor.fetchall()
        st.dataframe(DATA)   
        conn.commit();
    if Action == 'Delete':
     ID = st.number_input("Provider ID:",step=1)
     
     
     PB_DELETE1 = st.button("DELETE")
     if PB_DELETE1:
        

        query = "DELETE FROM FOOD_receivers where receiver_id = %s" 
        VAL = ( ID,  )
        cursor.execute(query, VAL) 
        DATA = cursor.fetchall()
        st.dataframe(DATA)   
        conn.commit();



# food listing


if option == 'Food Listing':
    Action = st.selectbox(
    "Select option",
    ("Create", "Update", "Read", "Delete")
    )

    if Action == 'Create':
     ID = st.number_input("Food ID:",step=1)
     NAME = st.text_input("Food_Name:")
     QTY = st.number_input("QANTITY:",step=1)
     EXP_DATE = st.text_input("Exparity Date")
     P_ID = st.number_input("Provider_ID")
     p_TYPE = st.text_input("Provider Type:")
     LOC = st.text_input("Location:")
     Food_Type = st.text_input("Food Type:")
     Meal_type = st.text_input("Meal Type")
     PB_CREATE2 = st.button("Create")
     if PB_CREATE2:

        cursor.execute(
          "INSERT INTO food_listing (Food_ID, Food_Name, Quantity, Expiry_Date, Provider_ID, Provider_Type, Location, Food_Type, Meal_Type ) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (ID, NAME, QTY, EXP_DATE, P_ID, p_TYPE, LOC, Food_Type, Meal_type)
            )
        conn.commit();

    if Action == 'Update':
     ID = st.number_input("Food ID:",step=1)
     NAME = st.text_input("Food_Name:")
     QTY = st.number_input("QANTITY:",step=1)
     EXP_DATE = st.text_input("Exparity Date")
     P_ID = st.number_input("Provider_ID")
     p_TYPE = st.text_input("Provider Type:")
     LOC = st.text_input("Location:")
     Food_Type = st.text_input("Food Type:")
     Meal_type = st.text_input("Meal Type")
     PB_UPDATE2 = st.button("UPDATE")
     
     if PB_UPDATE2:

        query = "UPDATE food_listing SET Food_Name = %s, Quantity = %s, Expiry_Date = %s, Provider_ID = %s, Provider_Type = %s, Location = %s, Food_Type = %s, Meal_Type = %s  where food_id = %s" 
        VAL = (NAME, QTY, EXP_DATE, P_ID, p_TYPE, LOC, Food_Type, Meal_type, ID)
        cursor.execute(query, VAL)    
        conn.commit();


    if Action == 'Read':
     
     PB_READ2 = st.button("READ")
     if PB_READ2:

        query = "SELECT * FROM FOOD_LISTING" 
        
        cursor.execute(query) 
        DATA = cursor.fetchall()
        st.dataframe(DATA)   
        conn.commit();
    if Action == 'Delete':
     ID = st.number_input("FOOD ID:",step=1)
     
     
     PB_DELETE2 = st.button("DELETE")
     if PB_DELETE2:
        

        query = "DELETE FROM FOOD_LISTING where FOOD_id = %s" 
        VAL = ( ID,  )
        cursor.execute(query, VAL) 
        DATA = cursor.fetchall()
        st.dataframe(DATA)   
        conn.commit();


#CLAIM DATA

if option == 'Claims data':
    Action = st.selectbox(
    "Select option",
    ("Create", "Update", "Read", "Delete")
    )

    if Action == 'Create':
     ID = st.number_input("Food ID:",step=1)
     FOOD_ID = st.number_input("Food_ID:")
     R_ID = st.number_input("Provider_ID")
     STATUS = st.text_input("STATUS:")
     TIME_STAMP = st.text_input("TIME_STAMP:")
     PB_CREATE3 = st.button("Create")
     if PB_CREATE3:

        cursor.execute(
          "INSERT INTO CLAIMS_DATA (CLAIM_ID, Food_ID, RECEIVER_ID, STATUS, TIMESTAMP  ) VALUES ('%s', '%s', '%s', '%s', '%s')" % (ID, FOOD_ID, R_ID, STATUS, TIME_STAMP)
            )
        conn.commit();

    if Action == 'Update':
     ID = st.number_input("Food ID:",step=1)
     FOOD_ID = st.number_input("Food_ID:")
     R_ID = st.number_input("Provider_ID")
     STATUS = st.text_input("STATUS:")
     TIME_STAMP = st.text_input("TIME_STAMP:")
     


     PB_UPDATE3 = st.button("UPDATE")
     if PB_UPDATE3:

        query = "UPDATE CLAIMS_DATA SET Food_ID = %s, Receiver_ID = %s, Status = %s, timestamp = %s,  where claim_id = %s" 
        VAL = (FOOD_ID, R_ID, STATUS, TIME_STAMP, ID)
        cursor.execute(query, VAL)    
        conn.commit();


    if Action == 'Read':
     
     PB_READ3 = st.button("READ")
     if PB_READ3:

        query = "SELECT * FROM CLAIMS_DATA" 
        
        cursor.execute(query) 
        DATA = cursor.fetchall()
        st.dataframe(DATA)   
        conn.commit();
    if Action == 'Delete':
     ID = st.number_input("FOOD ID:",step=1)
     
     
     PB_DELETE3 = st.button("DELETE")
     if PB_DELETE3:
        

        query = "DELETE FROM CLAIMS_DATA where CLAIM_id = %s" 
        VAL = ( ID,  )
        cursor.execute(query, VAL) 
        DATA = cursor.fetchall()
        st.dataframe(DATA)   
        conn.commit();

#conn.close()