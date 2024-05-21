import time
import gpio as GPIO
import vlc
from pydub import AudioSegment  # Import for audio processing
import sys
sys.path.insert(0, '/home/rock/Desktop/Hearsight/')
from play_audio import GTTSA
machine_voice = GTTSA()

GPIO_TRIGECHO = 501  # Change this to the correct GPIO pin number
GPIO.setup(448, GPIO.IN)  # Exit Button (change to the correct pin)
GPIO.setup(GPIO_TRIGECHO, GPIO.OUT)  # Initial state as output
GPIO.output(GPIO_TRIGECHO, False)

def measure():# Your measurement logic here
    GPIO.output(GPIO_TRIGECHO, True)
    GPIO.output(GPIO_TRIGECHO, False)
    start = time.time()
    GPIO.setup(GPIO_TRIGECHO, GPIO.IN)
    while GPIO.input(GPIO_TRIGECHO)==0:
        start = time.time()
    while GPIO.input(GPIO_TRIGECHO)==1:
        stop = time.time() 
    if 'stop' not in locals():# Add a check to see if 'stop' variable is still undefined
        machine_voice.play_machine_audio("sensor_is_not_working_so_switch_off_the_HearSight_device_for_some_time_and_then_start_it_again.mp3")
    GPIO.setup(GPIO_TRIGECHO, GPIO.OUT)
    GPIO.output(GPIO_TRIGECHO, False)
    TimeElapsed = stop-start
    distance = TimeElapsed / 0.000058
    return distance

while True:
    distance = measure()     
    print("Distance: %.1f cm" % distance)

    if 426.72 <= distance <= 457.2:
        machine_voice.play_machine_audio("340Hz-5sec.wav")
    
    if 274.32 <= distance <= 304.8:
        machine_voice.play_machine_audio("440Hz-6sec.wav")
        
    if 152.4 <= distance <= 182.88:
        machine_voice.play_machine_audio("640-3.5min.wav")
    
    input_state = GPIO.input(448)
    if input_state == True:
        machine_voice.play_machine_audio("exit_button_pressed.mp3")
        break
