import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH
import matplotlib.pyplot as plt

links = [
    # Link 1: Base to Waist
    RevoluteDH(
        alpha=0,
        a=0,
        d=0.08945,
        offset=0,
        qlim=[-np.pi, np.pi]
    ),
    
    # Link 2: Waist to Shoulder
    RevoluteDH(
        alpha=np.pi/2,
        a=0.035,
        d=0,
        offset=0,
        qlim=[-111*np.pi/180, 107*np.pi/180]
    ),
    
    # Link 3: Shoulder to Elbow
    RevoluteDH(
        alpha=0,
        a=0.100,
        d=0,
        offset=0,
        qlim=[-121*np.pi/180, 92*np.pi/180]
    ),
    
    # Link 4: Elbow to Wrist
    RevoluteDH(
        alpha=0,
        a=0.066,
        d=0,
        offset=0,
        qlim=[-100*np.pi/180, 123*np.pi/180]
    )
]

robot = DHRobot(links, name='PincherX 100')

# Set different joint angles
q = [0, 0, 0, 0]
# q = [np.pi/4, np.pi/4, np.pi/4, np.pi/4]
robot.plot(q, backend='pyplot', block=True)
