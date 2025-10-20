from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Get the motor
x_motor = robot.getDevice('x motor')

delay = 1.5  # seconds
steps_to_wait = int(delay * 1000 / timestep)

for _ in range(steps_to_wait):
    robot.step(timestep)

# Infinite position = velocity control
x_motor.setPosition(float('inf'))
x_motor.setVelocity(1)

while robot.step(timestep) != -1:
    # Just move a little in +X as a test
    x_motor.setVelocity(1)
