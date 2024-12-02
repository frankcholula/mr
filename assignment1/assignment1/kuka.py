from roboticstoolbox.models.DH import KR5
import numpy as np

# Create the robot
robot = KR5()

# Show each configuration individually
configs = [robot.qz, robot.qr, robot.qk1, robot.qk2, robot.qk3]
config_names = ['qz', 'qr', 'qk1', 'qk2', 'qk3']

# Display each configuration
for config, name in zip(configs, config_names):
    print(f"\nDisplaying {name} configuration...")
    print(f"Joint angles: {np.rad2deg(config)} degrees")
    robot.plot(config, block=True)

# Now show the full trajectory
print("\nNow showing full trajectory through all configurations...")

# Create trajectories between consecutive configurations
steps = 50
all_trajectories = []

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
robot.plot(full_trajectory, block=True)