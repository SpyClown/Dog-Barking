import RPi.GPIO as GPIO
import time
import mysql.connector
import random
from datetime import datetime

#Database Setuping part

db = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="root",
	database="dog_barking"
	)

mycursor = db.cursor()

#GPIO Setuping part
#The channel which is connected for sound sensor
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

#Making a startdate for checking, because the first bark is always newer 
startdate = datetime(2000, 01, 01, 00, 00, 00)
barkingnumber = 1

while True:
	value = GPIO.input(channel)
        if (value == 0):
            print "Sound Detected!"
            now = datetime.now()
            print "Ennyi az ido:"
            print now
            idn = random.randint(0,2500000)
            print "Az ID azonosito:"
            print idn
            checkidsql = "SELECT ID FROM Ugatasok"
            mycursor.execute(checkidsql)
            if(idn = lekerdezettid)
                while n != lekerdezettid
                idn = random.randint(0,2500000)
                checkidsql = "SELECT ID FROM Barkings"
                mycursor.execute(checkidsql)
            bark = 1
            sql = "INSERT INTO Barkings (ID, Date, Bark) VALUES (%s, %s, %s)"
            val = (idn ,now, bark)
            mycursor.execute(sql, val)
            db.commit()
            diffbettwohours = now.hour - startdate.hour
            diffbettwominute = now.minute - startdate.minute
            #diffbettwosecond = now.second - startdate.second
            print "A kulonbseg a ketto ido kozott:"
            print diffbettwominute
            if(diffbettwohours == 0)
                if(diffbettwominute ==0)
                #time.sleep(2)
                #if(diffbettwosecond < 30 and diffbettwosecond > -29):
                #if(diffbettwominute == 0):
                print "Ugyan abban a percben tortent az ugatas"
                barkingnumber += 1
                startdate = now
                print "A startdate-nek az uj erteke:"
                print startdate
                print "Mennyiszer lepett ide be"
                print barkingnumber
                startdate = now
                    if(barkingnumber == 5):
                        print "5 siker!"
                        #sound play
                    if(barkingnumber == 10):
                        print "10 siker!"
                        #sound play
                else
                barkingnumber = 1
            else
            barkingnumber = 1
                



