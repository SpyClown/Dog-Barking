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

channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
startdate = datetime(2000, 01, 01, 00, 00, 00)
mennyi = 1

while True:
	value = GPIO.input(channel)
        if (value == 0):
            print "Sound Detected!"
	    time.sleep(2)
	    now = datetime.now()
	    print "Ennyi az ido:"
            print now
            n = random.randint(0,2500000)
	    print "Az ID azonosito:"
            print n
            ugat = 1
            sql = "INSERT INTO Ugatasok (ID, Date, Ugat) VALUES (%s, %s, %s)"
            val = (n ,now, ugat)
            mycursor.execute(sql, val)
            db.commit()
	    diffbettwominute = now.minute - startdate.minute
            diffbettwosecond = now.second - startdate.second
	    print "A kulonbseg a ketto ido kozott:"
	    print diffbettwosecond
	    time.sleep(5)
	    if(diffbettwosecond < 30 and diffbettwosecond > -29):
		if(diffbettwominute == 0):
			print "kevesebb mint 30 a kulonbseg"
			mennyi += 1
			startdate = now
			print "Az uj ido"
			print startdate
			print "Mennyiszer lepett ide be"
			print mennyi
	    else:
		mennyi = 1
		print "Uj ido"
		startdate = now
            if(mennyi == 5):
                print "Siker!"



