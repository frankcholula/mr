import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH
import matplotlib.pyplot as plt

class PincherX100(DHRobot):
    def __init__(self):
        links = [
            RevoluteDH(alpha=np.pi / 2, a=0, d=0.08945, offset=0, qlim=[-np.pi, np.pi]),
            RevoluteDH(
                alpha=0,
                a=0.035,
                d=0,
                offset=0,
                qlim=[np.deg2rad(-111), np.deg2rad(107)],
            ),
            RevoluteDH(
                alpha=0,
                a=0.100,
                d=0,
                offset=0,
                qlim=[np.deg2rad(-121), np.deg2rad(92)],
            ),
            RevoluteDH(
                alpha=0,
                a=0.066,
                d=0,
                offset=0,
                qlim=[np.deg2rad(-100), np.deg2rad(123)],
            ),
        ]
        super().__init__(links, name="PincherX100")

robot = PincherX100()

# Define a sequence of joint angles (in radians)
q1 = [0, 0, 0, 0]
q2 = [np.pi / 4, np.pi / 4, 0, 0]
q3 = [np.pi / 4, np.pi / 4, np.pi / 4, 0]
q4 = [np.pi / 4, np.pi / 4, np.pi / 4, -np.pi / 4]  # Corrected to 4 elements
q5 = [0, 0, 0, 0]

q_list = [q1, q2, q3, q4, q5]

# Create trajectory
steps = 10
trajectory = []

for i in range(len(q_list) - 1):
    start = q_list[i]
    end = q_list[i + 1]
    for step in range(steps + 1):  # Include the endpoint
        t = step / steps  # Interpolation parameter from 0 to 1
        q = [start[j] + t * (end[j] - start[j]) for j in range(4)]
        trajectory.append(q)

q_traj = np.array(trajectory)

# Plot the trajectory
robot.plot(
    q_traj,
    block=True,
    limits=[-0.2, 0.2, -0.2, 0.2, 0, 0.4],
    jointaxes=True,  # Optional
    eeframe=True,    # Optional
)