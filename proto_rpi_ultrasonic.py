import time
import RPi.GPIO as GPIO
import os
import sys
import vlc
000000
GPIO.setmode(GPIO.BCM)
GPIO_TRIGECHO = 18

print ("Ultrasonic Measurement")
       
GPIO.setup(11, GPIO.IN)#Confirm Button
GPIO.setup(GPIO_TRIGECHO,GPIO.OUT)  # Initial state as output

GPIO.output(GPIO_TRIGECHO, False)

class Navigation:
    def measure():
        GPIO.output(GPIO_TRIGECHO, True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGECHO, False)
        start = time.time()

        GPIO.setup(GPIO_TRIGECHO, GPIO.IN)
        while GPIO.input(GPIO_TRIGECHO)==0:
            start = time.time()

        while GPIO.input(GPIO_TRIGECHO)==1:
            stop = time.time()
      
        GPIO.setup(GPIO_TRIGECHO, GPIO.OUT)
        GPIO.output(GPIO_TRIGECHO, False)

        TimeElapsed = stop-start
        #distance = (elapsed * 34300)/2.0
        distance = TimeElapsed / 0.000058
        time.sleep(0.1)
        return distance

    try:

        while True:

            distance = measure()
            print ("  Distance : %.1f cm" % distance)
            if distance<=396.24 and distance >=304.80:
                  media = vlc.MediaPlayer("/home/pi/Hearsight/English/English/340Hz-5sec.wav")
                  media.play()
                  time.sleep(1.25)
                  media.stop()
                  print("h1")
            if distance<=304.79 and distance >=121.92:
                  media = vlc.MediaPlayer("/home/pi/Hearsight/English/English/440Hz-6sec.wav")
                  media.play()
                  time.sleep(1.25)
                  media.stop()
                  print("h2")
            if distance<=121.91:
                  media = vlc.MediaPlayer("/home/pi/Hearsight/English/English/640-3.5min.wav")
                  media.play()
                  time.sleep(1.25)
                  media.stop()
                  print("h3")  
            input_state = GPIO.input(11)
            if input_state == True:
                time.sleep(1)
                media = vlc.MediaPlayer("/home/pi/Hearsight/English/English/exit_button_pressed.mp3")
                media.play()
                sys.exit()
                break

    except KeyboardInterrupt:
        GPIO.cleanup()
a = Navigation()
c = a.measure()
