import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH
import matplotlib.pyplot as plt

# Create robot with DH parameters
links = [
    # Link 1: Base to Waist
    RevoluteDH(alpha=0, a=0, d=0.08945, offset=0),
    
    # Link 2: Waist to Shoulder
    RevoluteDH(alpha=np.pi/2, a=0.035, d=0, offset=0),
    
    # Link 3: Shoulder to Elbow
    RevoluteDH(alpha=0, a=0.100, d=0, offset=0),
    
    # Link 4: Elbow to Wrist
    RevoluteDH(alpha=0, a=0.066, d=0, offset=0)
]

# Create the robot
robot = DHRobot(links, name='PincherX 100')

# Plot the robot in home position
robot.plot([0, 0, 0, 0], block=True)