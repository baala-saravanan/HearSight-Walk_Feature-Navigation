import time
import gpio as GPIO
import sys
import vlc
000000
from pydub import AudioSegment
sys.path.insert(0, '/home/rock/Desktop/Hearsight/')
from play_audio import GTTSA
machine_voice = GTTSA()

GPIO_TRIGECHO = 501  # Change this to the correct GPIO pin number
GPIO.setup(448, GPIO.IN)  # Exit Button (change to the correct pin)
GPIO.setup(GPIO_TRIGECHO, GPIO.OUT)  # Initial state as output
GPIO.output(GPIO_TRIGECHO, False)

def measure():# Your measurement logic here
    GPIO.output(GPIO_TRIGECHO, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGECHO, False)
    start = time.time()
    GPIO.setup(GPIO_TRIGECHO, GPIO.IN)
    while GPIO.input(GPIO_TRIGECHO)==0:
        start = time.time()
    while GPIO.input(GPIO_TRIGECHO)==1:
        stop = time.time() 
    if 'stop' not in locals():# Add a check to see if 'stop' variable is still undefined
#        machine_voice.play_machine_audio("sensor_is_not_working_so_switch_off_the_HearSight_device_for_some_time_and_then_start_it_again.mp3")
        machine_voice.play_machine_audio("now_press_confirm_button.mp3")
    GPIO.setup(GPIO_TRIGECHO, GPIO.OUT)
    GPIO.output(GPIO_TRIGECHO, False)
    TimeElapsed = stop-start
    distance = TimeElapsed / 0.000058
#    distance = (TimeElapsed * 34300)/1.5
    time.sleep(0.5)
    return distance

while True:
    distance = measure()     
    print("Distance: %.1f cm" % distance)

#    if distance<=457.2 and distance >=426.72:#15 to 14
    if distance<=243.84 and distance >=152.4:
        media = vlc.MediaPlayer("/home/rock/Desktop/Hearsight/audios/beeb/340Hz-5sec.wav")
        media.play()
        time.sleep(1.25)
        media.stop()
        print("h1")
        
#    elif distance<=304.8 and distance >=274.32:#10 to 09
#    if distance<=243.84 and distance >=182.88:#08 to 06
#    if distance<=304.79 and distance >=121.92:
#        media = vlc.MediaPlayer("/home/rock/Desktop/Hearsight/audios/beeb/440Hz-6sec.wav")
#        media.play()
#        time.sleep(1.25)
#        media.stop()
#        print("h2")
        
#    elif distance<=121.92 and distance >=60.96:#04 to 02
    if distance<=121.91:
        media = vlc.MediaPlayer("/home/rock/Desktop/Hearsight/audios/beeb/3_long_high.mp3")
        media.play()
        time.sleep(1.25)
        media.stop()
        print("h3")  

    input_state = GPIO.input(448)
    if input_state == True:
        machine_voice.play_machine_audio("feature_exited.mp3")
        break
