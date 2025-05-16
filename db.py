
from dotenv import load_dotenv
import mysql.connector
import os
import sys

load_dotenv()

def init():
    # Check Environment Variables
    if os.environ.get('DB_USER') is None:
        print("[FAIL]: Environment Variable DB_USER is not set")
        sys.exit()
    if os.environ.get('DB_PASSWORD') is None:
        print("[FAIL]: Environment Variable DB_PASSWORD is not set")
        sys.exit()
    if os.environ.get('DB_HOST') is None:
        print("[FAIL]: Environment Variable DB_HOST is not set")
        sys.exit()
    if os.environ.get('DB_PORT') is None:
        print("[FAIL]: Environment Variable DB_PORT is not set")
        sys.exit()
    if os.environ.get('DB_DATABASE') is None:
        print("[FAIL]: Environment Variable DB_DATABASE is not set")
        sys.exit()

def connect():
    try:
        # Connect to MariaDB
        db_connection = mysql.connector.connect(
            user = os.environ.get('DB_USER'),
            password = os.environ.get('DB_PASSWORD'),
            host = os.environ.get('DB_HOST'),
            port = int(os.environ.get('DB_PORT')),
            database = os.environ.get('DB_DATABASE'),
            collation = 'utf8mb4_unicode_520_ci'
        )
        print ("Successfully Connected to MariaDB")
        return db_connection

    except Exception as e:
        print("[FAIL]: " + str(e))
        sys.exit()

def get_data(db_connection):
    cur = db_connection.cursor()
    try:
        # Create Mix & Match Event Table in Database
        cur.execute("CREATE TABLE IF NOT EXISTS mix_match_events ( \
            EventID int NOT NULL AUTO_INCREMENT, \
            Subtitle varchar(255), \
            Title varchar(255), \
            Date varchar(255), \
            Time varchar(255), \
            Location varchar(255), \
            EventURL varchar(255), \
            PRIMARY KEY (EventID))"
        )

        # Pull Events from Database
        event_data = []
        cur.execute("SELECT * FROM mix_match_events")
        db_events = cur.fetchall()
        for event in db_events:
            temp_event = {}
            temp_event['ID'] = event[0]
            temp_event['subtitle'] = event[1]
            temp_event['title'] = event[2]
            temp_event['date'] = event[3]
            temp_event['time'] = event[4]
            temp_event['location'] = event[5]
            temp_event['eventURL'] = event[6]
            event_data.append(temp_event)

        print ("Succesfully Fetched " + str(len(event_data)) + " Events from Database")
        return event_data
    
    except Exception as e:
        print("[FAIL]: " + str(e))
        sys.exit()

def remove_event(db_connection, event):
    cur = db_connection.cursor()
    try:            
        cur.execute("DELETE FROM mix_match_events WHERE EventID='" + str(event['ID']) + "'")
        db_connection.commit()
        print("Removed Obsolete Event: " + event['eventURL'])

    except Exception as e:
        print("[FAIL]: " + str(e))
        sys.exit()

def add_event(db_connection, event):
    cur = db_connection.cursor()
    try:            
        cur.execute("INSERT INTO mix_match_events (Subtitle, Title, Date, Time, Location, EventURL) VALUES ('" \
            + event['subtitle'] + "','" \
            + event['title'] + "','" \
            + event['date'] + "','" \
            + event['time'] + "','" \
            + event['location'] + "','" \
            + event['eventURL'] + "')" \
        )
        db_connection.commit()
        print("Added Event: " + event['eventURL'])

    except Exception as e:
        print("[FAIL]: " + str(e))
        sys.exit()
def close(db_connection):
    # Close MariaDB Connection
    db_connection.close()
    print ("Closed Connection to MariaDB")