from roboticstoolbox.models.DH import KR5
import numpy as np

# Create the robot
robot = KR5()

# Get preset configurations directly from robot
configs = [robot.qz, robot.qr, robot.qk1, robot.qk2, robot.qk3]
config_names = ['qz', 'qr', 'qk1', 'qk2', 'qk3']

# Create trajectories between consecutive configurations
steps = 50
all_trajectories = []

# Generate trajectories between each configuration
for i in range(len(configs)-1):
    start = configs[i]
    end = configs[i+1]
    
    trajectory = np.zeros((steps, 6))
    for j in range(steps):
        s = j / (steps - 1)
        trajectory[j] = start + s * (end - start)
    
    all_trajectories.append(trajectory)

# Combine all trajectories
full_trajectory = np.vstack(all_trajectories)

# Display the full motion
print("Moving through all configurations: qz → qr → qk1 → qk2 → qk3")
robot.plot(full_trajectory, block=False)
