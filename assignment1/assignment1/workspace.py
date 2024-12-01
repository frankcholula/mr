from roboticstoolbox.models.DH import KR5
from swift import Swift
import numpy as np

# Create the robot and Swift simulator instance
robot = KR5()
env = Swift()
env.launch()  # Launch the Swift window

# Add robot to the simulator
env.add(robot)

# Define configurations for CyberKnife-like movements
q_home = np.array([0, 0, 0, 0, 0, 0])  # Home position
q1 = np.array([np.pi/3, -np.pi/6, np.pi/4, 0, np.pi/3, 0])  # Upper hemisphere
q2 = np.array([-np.pi/3, np.pi/6, -np.pi/4, 0, -np.pi/3, 0])  # Lower hemisphere
q3 = np.array([np.pi/2, -np.pi/4, np.pi/3, np.pi/6, np.pi/4, -np.pi/6])  # Side approach

# Create trajectory
steps = 50
traj1 = np.zeros((steps, 6))
traj2 = np.zeros((steps, 6))
traj3 = np.zeros((steps, 6))

# Generate smooth trajectories
for i in range(steps):
    s = i / (steps - 1)
    traj1[i] = q_home + s * (q1 - q_home)
    traj2[i] = q1 + s * (q2 - q1)
    traj3[i] = q2 + s * (q3 - q2)

# Combine trajectories
trajectory = np.vstack((traj1, traj2, traj3))

# Animate the robot through the trajectory
for q in trajectory:
    robot.q = q  # Update joint configuration
    env.step()   # Update the display

print("\nRobot Model Details:")
print(robot)