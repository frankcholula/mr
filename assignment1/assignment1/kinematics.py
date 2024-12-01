import numpy as np
from trossen.robots import PincherX100

if __name__ == "__main__":
    robot = PincherX100()
    print(robot)
    # Define a sequence of joint angles (in radians)
    q1 = [0, 0, 0, 0]
    q2 = [np.pi / 4, -np.pi / 4, 0, 0]
    q3 = [np.pi / 4, -np.pi / 4, -np.pi / 4, 0]
    q4 = [np.pi / 4, -np.pi / 4, -np.pi / 4, np.pi / 4]
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
        block=False,
        limits=[-0.3, 0.3, -0.2, 0.2, 0, 0.4],
        jointaxes=True,  # Optional
        eeframe=True,    # Optional
    )