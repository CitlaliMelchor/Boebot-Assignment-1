# Initial Webot controller for Boebot training in Automation for Bioproduction
# Sam Blaauw - v0.1 - 30-4-2020

# Load libraries
from controller import Robot

# Define the time step
TIME_STEP = 500 # Miliseconds
# Initialize the simulation time variable
t = 0

# Create the Robot instance.
boebot = Robot()

# Main loop
while boebot.step(TIME_STEP) != -1:
    print("Hello World", "time is:",(t/1000),"seconds")
    t += TIME_STEP # Increase the simulation time in TIME_STEP