# load libraries
from controller import Robot, LED, Motor

boebot = Robot()

# Time inputs
TIME_STEP = 32

# Define Motors
left_wheel= boebot.getMotor("left wheel motor")
right_wheel = boebot.getMotor("right wheel motor")

# Define Sensors
lw_sensor= boebot.getPositionSensor("left wheel sensor")
rw_sensor = boebot.getPositionSensor("right wheel sensor")

# Enable the sensors
lw_sensor.enable(TIME_STEP)
rw_sensor.enable(TIME_STEP)

# Functions
def drive():
    left_wheel.setPosition(0)
    right_wheel.setPosition(0)
        
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
      
steps_counted = 0 #[#]
time_running = 0.0 #[ms]

# main loop
while boebot.step(TIME_STEP) != -1:

    drive()
    
    # Position, rad
    x1,x2 = Position(rw_sensor, lw_sensor)
    
    # Traveled distance, m
    d1,d2 = 0.034*x1, 0.034*x2
    
    # Velocity, rad/s
    v1,v2 = Velocity(right_wheel, left_wheel)
    
    # Counters and time inputs
    steps_counted += 1
    time_running = (steps_counted*TIME_STEP/1000)
    
    # Set velocity
    right_wheel.setVelocity(1/(5*0.034))
    left_wheel.setVelocity(1/(5*0.034))
          
    print("time:", time_running, 'Position', d1,d2, "Velocity",v1, v2 )
    
    # Stop after 5 seconds
    if d1 and d2 >= 1:
        stop()


            