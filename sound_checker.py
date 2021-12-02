import RPi.GPIO as GPIO
import time
import mysql.connector
import random
from datetime import datetime

db = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="root",
	database="dog_barking"
	)

mycursor = db.cursor()

#GPIO Setuping part

ID = 1
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):

	if GPIO.input(channel):
		print "Sound Detected!"
		now = datetime.now()
		print now
		dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
		print dt_string
		n = random.randint(0,2500000)
		print n
		ugat = 1
		mennyi = 0
		egy = 1
		sql = "INSERT INTO Ugatasok (ID, Date, Ugat) VALUES (%s, %s, %s)"
		val = (n ,dt_string, ugat)
		mycursor.execute(sql, val)
		db.commit()
		lekerdezes = "SELECT * FROM Ugatasok ORDER BY Date DESC LIMIT 5"
		mycursor.execute(lekerdezes)
		records = mycursor.fetchall()
		for record in records:
			if egy in record:
				mennyi += 1
				print "Ez a mennyi erteke"
				print mennyi
		if(mennyi == 5):
			print "Siker!" 
	else:
		n = random.randint(0,2500000)
		now = datetime.now()
		dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
		ugat = 0
		print "Sound not Detected!"
		sql = "INSERT INTO Ugatasok (ID, Date, Ugat) VALUES (%s, %s, %s)"
		val = (n, dt_string, ugat)
		mycursor.execute(sql,val)
		db.commit()
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)

while True:
	time.sleep(1)

