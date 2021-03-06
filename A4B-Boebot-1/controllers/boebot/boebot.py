# load libraries
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
    left_wheel.setVelocity(2)#(1/(1.5*0.034))
    right_wheel.setVelocity(2)#(1/(1.5*0.034))
    left_wheel.setPosition(float("Inf"))
    right_wheel.setPosition(float("Inf"))
        
def stop():
    left_wheel.setVelocity(float(0))
    right_wheel.setVelocity(float(0))
    
def Position(rws, lws):
    x1 = rws.getValue()
    x2 = lws.getValue()
    return x1,x2

def Velocity(rw, lw):
    v1 = lw.getVelocity()
    v2 = rw.getVelocity()
    return v1,v2  

def rTurn():
    right_wheel.setVelocity(float(0))    
      
steps_counted = 0 #[#]
time_running = 0.0 #[ms]

# Number of turns made
turns = 0
# Initial state
xR0, xL0 = 0,0

# Correction factor 

# main loop
while boebot.step(TIME_STEP) != -1:

    #drive()
    
    # Position, rad
    xR,xL = Position(rw_sensor, lw_sensor)
    
    # Traveled distance, m
    dR_1,dL_1 = xR0  + 1.25/r, xL0 + 1.25/r
    dR_2,dL_2 = xR0  + 1.25/r, xL0 + 1.25/r + 95*math.pi/68 
    dR_3,dL_3 = xR0  + 1.75/r, xL0 + 1.75/r + 95*math.pi/68 
    dR_4,dL_4 = xR0  + 1.75/r, xL0 + 1.75/r + 95*math.pi/34
    
    # Velocity, rad/s
    vR,vL = Velocity(right_wheel, left_wheel)
    
    # Counters and time inputs
    steps_counted += 1
    time_running = (steps_counted*TIME_STEP/1000)
    
# NOTE: THE SENSORS ARE SWITCHED    
    if steps_counted % (PRINT_INTERVAL/TIME_STEP) <1:
        print('Position', xR,xL, 'Velocity', vR,vL, "turns made:", turns)
        
    if xL <= dL_1 or xL>= dL_2 and xL <= dL_3:
        drive()
              
    elif xL > dL_1 and xL <= dL_2 or xL > dL_3 and xL <= dL_4:
        rTurn()
    
    if xL >= dL_4:
        drive()
        if turns == 0: #Verify if is the first turn 
            xR0,xL0 = xR + 0.125/r , xL + 0.125/r  
        else:
            xR0,xL0 = xR, xL  
        turns += 1

    
    
    
    
    


            