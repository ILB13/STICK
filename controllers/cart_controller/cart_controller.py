
from controller import Robot

def sign(x):
    return 0 if x == 0 else x / abs(x)
def maxvelocity(x,y):
    if abs(x)>y:
        return y * sign(x)
    else:
        return x
# Initialize robot
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Devices
motor = robot.getDevice("x motor")
motor.setPosition(float('inf'))
motor.setVelocity(0.5)   # start moving

# Stick angle sensor
stick_sensor = robot.getDevice("stick_angle_sensor")
stick_sensor.enable(timestep)

# Print at 10 Hz
print_interval = 0.01  # seconds
steps_per_print = int((print_interval * 1000) / timestep)
step_counter = 0

prev_angle = stick_sensor.getValue()  # initial value
angular_velocity = 0.0

print("Cart controller started.", flush=True)

# sensitivity = 1
speed = 10000000000
speedpower = 0.1
# deadzone = 0.5
# damper = .967
extra = 5

while robot.step(timestep) != -1:
    step_counter += 1

    # Compute angular velocity from change in angle
    current_angle = stick_sensor.getValue()
    angular_velocity = (current_angle - prev_angle) / (timestep / 1000.0)
    prev_angle = current_angle

    if step_counter >= steps_per_print:
        step_counter = 0

        # Direction of rotation
        if angular_velocity > 0.001:
            direction = "clockwise"
        elif angular_velocity < -0.001:
            direction = "counterclockwise"
        else:
            direction = "steady"

        print(f"Angle: {current_angle:+.3f} rad | "
              f"Angular Velocity: {angular_velocity:+.3f} rad/s | "
              f"Direction: {direction}",
              flush=True)
    
    # if angular_velocity < -sensitivity:
        # motor.setVelocity(-speed)
    # elif angular_velocity > sensitivity:
        # motor.setVelocity(speed)
    # elif angular_velocity > -deadzone and angular_velocity < deadzone:
        # motor.setVelocity(motor.getVelocity()*damper)
    motor.setVelocity(maxvelocity(((speed * sign(angular_velocity)*abs(angular_velocity) ** speedpower)+extra * sign(angular_velocity)),10))