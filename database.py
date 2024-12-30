import sqlite3
import json
import stock_json
import pprint
    
def connection():
    return sqlite3.connect("stocks.db")

def demo_load_from_json():
    json_sql=stock_json.open_json('ddl.json')
    return json_sql

def create_tables(connection):

    # Create table if table does not exist.
    # Open JSON File.
    CREATE_TABLES="CREATE TABLE IF NOT EXISTS hello(one TEXT, two TEXT)"
    print("Creating table if it does not exist.")
    with connection:
        connection.execute(CREATE_TABLES)

    DELETE_ALL_DATA="DELETE FROM hello"
    print("Deleting All rows from table . . . ")
    with connection:
        connection.execute(DELETE_ALL_DATA)

def create_table_json(connection):

    # Create table if table does not exist.
    # Get SQL Syntax from JSON File.

    CREATE_TABLES="CREATE TABLE IF NOT EXISTS hello(one TEXT, two TEXT)"
    print("Creating table if it does not exist.")
    with connection:
        connection.execute(CREATE_TABLES)

    DELETE_ALL_DATA="DELETE FROM hello"
    print("Deleting All rows from table . . . ")
    with connection:
        connection.execute(DELETE_ALL_DATA)

def add_row(connection, one, two):
    INSERT_ROW = "INSERT INTO hello (one, two) VALUES(?,?);"
    print("Adding rows back into table.")
    with connection:
        connection.execute(INSERT_ROW, (one, two))
        connection.execute(INSERT_ROW, ('three', 'four'))
        connection.execute(INSERT_ROW, ('five', 'six'))

def get_all_data(connection):

    GET_ALL_DATA = "SELECT * FROM hello;"
    print("Displaying all data.")
    with connection:
        return connection.execute(GET_ALL_DATA).fetchall()