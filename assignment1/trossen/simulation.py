import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH
import matplotlib.pyplot as plt

links = [
    RevoluteDH(
        alpha=np.pi/2,
        a=0,            
        d=0.08945,      
        offset=0,       
        qlim=[-np.pi, np.pi]
    ),
    
    RevoluteDH(
        alpha=0,
        a=0.035,
        d=0,
        offset=0,
        qlim=[-111*np.pi/180, 107*np.pi/180]
    ),
    
    RevoluteDH(
        alpha=0,
        a=0.100,
        d=0,
        offset=0,
        qlim=[-121*np.pi/180, 92*np.pi/180]
    ),
    
    RevoluteDH(
        alpha=0,
        a=0.066,
        d=0,
        offset=0,
        qlim=[-100*np.pi/180, 123*np.pi/180]
    )
]

robot = DHRobot(links, name='PincherX 100')

# Define a sequence of joint angles to move through (in radians)
q1 = [0, 0, 0, 0]
q2 = [np.pi/4, np.pi/4, 0, 0]
q3 = [np.pi/4, np.pi/4, np.pi/4, 0]
q4 = [np.pi/4, np.pi/4, np.pi/4, -np.pi/4, 0]
q5 = [0, 0, 0, 0]

# Create trajectory through these points
steps = 10
trajectory = []

for i in range(len([q1,q2,q3,q4,q5])-1):
    start = [q1,q2,q3,q4,q5][i]
    end = [q1,q2,q3,q4,q5][i+1]
    for step in range(steps):
        t = step/steps  # Interpolation parameter
        q = []
        for j in range(4):  # For each joint
            angle = start[j] + t*(end[j] - start[j])
            q.append(angle)
        trajectory.append(q)

for q in trajectory:
    robot.plot(q, block=False, limits=[-0.2, 0.2, -0.2, 0.2, 0, 0.4])
