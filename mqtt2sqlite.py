import paho.mqtt.subscribe as subscribe
import sqlite3
from datetime import datetime

#time setup
now = datetime.now()
dt_string = now.strftime("%m/%d/%Y %H:%M:%S")


topics = ['outTopic','smoker/temp','smoker/WiFi/#']

#database setup
conn = sqlite3.connect('smoker.db')
c = conn.cursor()
for topic in topics:
    c.execute('''CREATE TABLE '%s' 
              (date text, value text)''' % topic)

while True:
    msg = subscribe.simple(topics, hostname="tanukimario.mushroomkingdom", retained=False, msg_count=2) #in order not to miss any messages you will want msg_count to equal the max number of messages you expect to be sent at once.
    for message in msg:
        if message.topic == "smoker/temp":
            tempC = int(message.payload)
            tempF = 9.0/5.0 * int(message.payload)+32
            print(f'{message.topic}:{tempC}° C')
            print(f'{message.topic}:{tempF}° F')
            #c.execute("INSERT INTO '%s' VALUES ('fakedate, '%s')" % (message.topic,str(tempF)))
            c.execute(f"INSERT INTO '{message.topic}' VALUES ('{dt_string}','{tempF}')")
            conn.commit()
        else:
            print(f'{message.topic}:{message.payload}')
            
conn.close()
