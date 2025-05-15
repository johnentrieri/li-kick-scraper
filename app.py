from bs4 import BeautifulSoup

import db
import likick
import notify

# Initialize Database & Notifier
db.init()
notify.init()

# Scrape Data from LI Kick
site_data = likick.scrape()

# Connect to MariaDB
conn = db.connect()

# Fetch Data fom Database
event_data = db.get_data(conn)

# Compare & Remove Old Events
for db_event in event_data:
    event_found = False
    for site_event in site_data:
        if db_event['eventURL'] == site_event['eventURL']:
            event_found = True
    if event_found == False:
        db.remove_event(conn,db_event)

# Compare & Add New Events
for site_event in site_data:
    event_found = False
    for db_event in event_data:
        if site_event['eventURL'] == db_event['eventURL']:
            event_found = True
    if event_found == False:
        db.add_event(conn,site_event)
        notify.send_sms(site_event['eventURL'])

# Close Database Connection
db.close(conn)