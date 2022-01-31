##############################
#           Imports          #
##############################
from guizero import App, Window, Text, PushButton, TextBox, info, Box, ButtonGroup, Picture, CheckBox, ListBox
import matplotlib.pyplot as plt
import pandas as pd
import openpyxl
import sqlite3
from datetime import datetime, timedelta
import base64
import os
import os.path
###############################################
#                Database Setup               #
#                                             #
#           Delete Existing Database          #
###############################################
# This function deletes a database.
# checks if file exist if it does then it removes it
def delete_database(database_file):
    if os.path.exists(database_file):
        os.remove(database_file)
#######################################################
#              Executing SQL in a File                #
#######################################################
def init_db(database_file, database_sql):   
    # open the sqlite database file
    conn = sqlite3.connect(database_file)
    # connect to it and get a cursor
    # this is like a placeholder in the database
    cursor = conn.cursor()                  
    # open the script file containing SQL
    script = open(database_sql, 'r')
    # read the contents of the script 
    # into a string called sql
    sql = script.read()                     
    # execute the SQL 
    cursor.executescript(sql)               
    # commit the changes to make them permanent
    conn.commit()                           
    # close the connection to the database
    conn.close() 
#############################################
#              Executing SQL                #
#############################################
def Insert_Data(database_file, sql):   
    # open the sqlite database file
    conn = sqlite3.connect(database_file)
    # connect to it and get a cursor
    # this is like a placeholder in the database
    cursor = conn.cursor()                  
    cursor.executescript(sql)               
    # commit the changes to make them permanent
    conn.commit()                           
    # close the connection to the database
    conn.close()

########################################
#          Query the Database          #
########################################
# this peice of code connected to the database file i have in my files
# it then creates a variable to hold all the data and uses cursor function
# it then excecutes the sql code its give and returns all the rows that it found
def query_database(database, query):
    # this is used to pass a query and then it will fetchall rows found and then return this value
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    return rows

########################################
#         Calling the Database         #
########################################
# this bit of code called the functions that delete the existing database named FitnessApp, and then create a brand new one using DDL and DML sql in files and by calling these functions
# delete_database(database_file)
# init_db(database_file, SQLFile)
# query_database(database_file, query)
