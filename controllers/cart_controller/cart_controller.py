from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Get the motor
x_motor = robot.getDevice('x motor')

# Infinite position = velocity control
x_motor.setPosition(float('inf'))
x_motor.setVelocity(0.0)

while robot.step(timestep) != -1:
    # Just move a little in +X as a test
    x_motor.setVelocity(0.005)
