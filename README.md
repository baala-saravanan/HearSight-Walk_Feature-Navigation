# HearSight-Walk_Feature-Navigation
This code is designed for a device that uses a GPIO-triggered ultrasonic sensor to measure distances and plays different audio files based on the measured distance.
Here is a short summary of the code:

Setup: The code imports necessary libraries and modules, sets up GPIO pins for an ultrasonic sensor and an exit button, and initializes the GPIO states.

Distance Measurement Function (measure): This function triggers the ultrasonic sensor to send a pulse, waits for the echo to return, and calculates the distance based on the time taken for the echo to return.

Device Restart Function (restart_device): This function plays some audio messages and then reboots the device.

Main Loop (main): This continuously measures the distance using the measure function and:

Plays different audio files based on the distance ranges.
Tracks a counter that increases when the distance is in a specific small range.
Resets the counter if the distance is outside that range.
Restarts the device if the counter exceeds a threshold.
Exits if the exit button is pressed.
Execution: The main function is executed when the script is run.

**Summary of Functional Blocks**
GPIO Setup: Configures GPIO pins for sensor and exit button.
Distance Measurement: Measures the distance using the ultrasonic sensor.
Audio Playback: Plays specific audio files based on distance ranges using the VLC media player.
Device Control: Monitors for specific conditions to restart the device or exit the program.
Distance Ranges and Actions
137.16 cm to 213.36 cm: Plays a specific audio file.
20 cm to 121.91 cm: Plays another specific audio file.
14 cm to 15 cm: Increments a counter.
Counter reaches 40: Restarts the device.
Exit button pressed: Exits the program.
