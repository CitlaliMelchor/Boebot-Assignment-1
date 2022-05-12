# Automation for Bio-production 
# Assignment 1.4b v1
# Authors:
    # Nick van de Wedteringh
    # Citlali Melchor Ramírez

# Load libraries
from controller import Robot, LED, Motor
import math

boebot = Robot()

# Time inputs
TIME_STEP = 32
PRINT_INTERVAL = 500 # ms

# Define Motors
left_wheel= boebot.getMotor("left wheel motor")
right_wheel = boebot.getMotor("right wheel motor")

# Define Sensors
lw_sensor= boebot.getPositionSensor("left wheel sensor")
rw_sensor = boebot.getPositionSensor("right wheel sensor")

# Enable the sensors
lw_sensor.enable(TIME_STEP)
rw_sensor.enable(TIME_STEP)

# Wheel radio
r = 0.034

# Functions
def drive():
    left_wheel.setVelocity(1/(5*0.034))
    right_wheel.setVelocity(1/(5*0.034))
    left_wheel.setPosition(float("Inf"))
    right_wheel.setPosition(float("Inf"))
        
def stop():
    left_wheel.setVelocity(float(0))
    right_wheel.setVelocity(float(0))
    
def Position(rws, lws):
    x1 = lws.getValue()
    x2 = rws.getValue()
    return x1,x2

def Velocity(rw, lw):
    v1 = lw.getVelocity()
    v2 = rw.getVelocity()
    return v1,v2  

def rTurn():
    right_wheel.setVelocity(float(0))    
      
steps_counted = 0 #[#]
time_running = 0.0 #[ms]


# main loop
while boebot.step(TIME_STEP) != -1:

    #drive()
    
    # Position, rad
    xR,xL = Position(rw_sensor, lw_sensor)
    
    # Traveled distance, m
    dR_1,dL_1 = 1.25/r, 1.25/r
    dR_2,dL_2 = 1.25/r, 1.25/r + 95*math.pi/68
    dR_3,dL_3 = 1.75/r, 1.75/r + 95*math.pi/68
    dR_3,dL_3 = 1.75/r, 1.75/r + 95*math.pi/34
    
    # Velocity, rad/s
    vR,vL = Velocity(right_wheel, left_wheel)
    
    # Counters and time inputs
    steps_counted += 1
    time_running = (steps_counted*TIME_STEP/1000)
    
    # Print every 0.5 seconds
    if steps_counted % (PRINT_INTERVAL/TIME_STEP) <1:
        print('Position', xR,xL, 'Velocity', vR,vL)
        
        
    if xR and xL <= dR_1:
        drive()
        
    elif xL <= dL_2:
        rTurn()
        
    elif xL> dL_2 and xL <= dL_3:
        drive()
        

            
    
    
    
    
    
    


            