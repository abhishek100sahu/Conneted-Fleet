# Execute this file to create “edgeData” mysql database with Tables to store data.

import mysql.connector
import time

mydb = mysql.connector.connect(
    host = "192.168.195.163",
    port = "3306",
    user = 'root',
    password = 'nimesh'
    # database='edgeData'
)  

mycursor = mydb.cursor()

try:

    #mycursor.execute("CREATE DATABASE edgeData")
    mycursor.execute("USE edgeData")

    # Temperature table (temp and humidity ) 
    tempData = """ CREATE TABLE IF NOT EXISTS Temperature(
                    Time_Stamp VARCHAR(255),
                    Sensor_Name VARCHAR(255),
                    Vehicle_Name VARCHAR(255),
                    Temperature FLOAT(4,2) NOT NULL,
                    Humidity FLOAT(4,2) NOT NULL

    )"""
    mycursor.execute(tempData)
    print("Temperature Table Created ")

    # vibratsion table 
    vibData = """ CREATE TABLE IF NOT EXISTS Vibration(
                    Time_Stamp VARCHAR(255),
                    Sensor_Name VARCHAR(255),
                    Vehicle_Name VARCHAR(255),
                    Vibrations_value VARCHAR(255) NOT NULL

    )"""
    mycursor.execute(vibData)    
    print("Vibration Table Created ")
    
    
except mysql.connector.DatabaseError as e:
    print(e)

mydb.close()






