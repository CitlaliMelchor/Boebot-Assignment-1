# Initial Webot controller for Boebot training in Automation for Bioproduction
# Sam Blaauw - v0.1 - 30-4-2020

# Load libraries
# from controller import Robot, LED

#import pyb

# Define the time step
# TIME_STEP = 32 # Miliseconds
# Initialize the simulation time variable
# t = 0
# time = 0.0

# Create the Robot instance.
# boebot = Robot()
# left = boebot.getLED("left_led")


# Main loop
# while boebot.step(TIME_STEP) != -1:
    # time = (t*TIME_STEP)/1000 # seconds
    # #left.set(0)
    # if (t/TIME_STEP) % 0.5 < :
       # left.set(1)
        # print(time)
    # t += 1
    
    
    
# Initial Webot controller for Boebot training in Automation for Bioproduction
# Sam Blaauw - v0.1 - 30-4-2020

# load libraries
from controller import Robot, LED

boebot = Robot()

# Time inputs
TIME_STEP = 32
PRINT_INTERVAL = 500 #[ms]
LED_INTERVAL = 333 #[ms]

# Define LEDS
left_led = boebot.getLED("left_led")
right_led = boebot.getLED("right_led")

# Functions
def toggle_led(led, state):
    if state == "ON":
        left_led.set(1)
    if state == "OFF":
        left_led.set(0)
    
steps_counted = 0 #[#]
time_running = 0.0 #[ms]

# main loop
while boebot.step(TIME_STEP) != -1:
    
    # counters and time inputs
    steps_counted += 1
    time_running = (steps_counted*TIME_STEP/1000)
    
    # Print the steps and running time every 500 ms
    if steps_counted % (PRINT_INTERVAL/TIME_STEP) <1:
        print("Step:", steps_counted, "time:", time_running)
    
    # Let the LED blink for only the first 5000 ms
    if time_running <= 5:
        # Toggle left LED every 333 ms
        toggle_led(left_led, "OFF")
        if steps_counted % (LED_INTERVAL/TIME_STEP) <1:
            toggle_led(left_led, "ON")