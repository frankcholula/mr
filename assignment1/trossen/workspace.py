from trossen.robots import PincherX100
from matplotlib import pyplot as plt
import numpy as np


def plot_workspaces(robot, samples=15):
    """Plot both reachable and dextrous workspaces side by side"""
    fig = plt.figure(figsize=(20, 8))
    ax1 = fig.add_subplot(121, projection="3d")
    ax2 = fig.add_subplot(122, projection="3d")

    # Sample joint angles
    theta1 = np.linspace(robot.links[0].qlim[0], robot.links[0].qlim[1], samples)
    theta2 = np.linspace(robot.links[1].qlim[0], robot.links[1].qlim[1], samples)
    theta3 = np.linspace(robot.links[2].qlim[0], robot.links[2].qlim[1], samples)
    theta4 = np.linspace(robot.links[3].qlim[0], robot.links[3].qlim[1], samples)

    # Calculate reachable workspace points
    reachable_points = []
    for t1 in theta1:
        for t2 in theta2:
            for t3 in theta3:
                T = robot.fkine([t1, t2, t3, 0])
                if T is not None:
                    pos = [float(T.t[0]), float(T.t[1]), float(T.t[2])]
                    reachable_points.append(pos)
    
    reachable_points = np.array(reachable_points)

    # Calculate dextrous workspace points
    dextrous_points = []
    for t1 in theta1:
        for t2 in theta2:
            for t3 in theta3:
                # Only check for the most critical singularity - straight arm
                arm_angle = abs(t2 + t3)
                if abs(arm_angle) < 0.2 or abs(arm_angle - np.pi) < 0.2:  # Relaxed threshold
                    continue
                
                # Check wrist movement capability
                positions = []
                for t4 in theta4:
                    T = robot.fkine([t1, t2, t3, t4])
                    if T is not None:
                        pos = [float(T.t[0]), float(T.t[1]), float(T.t[2])]
                        positions.append(pos)
                
                if len(positions) > 0:
                    positions = np.array(positions)
                    # More lenient position variation check
                    variation = np.max([np.std(positions[:, i]) for i in range(3)])
                    if variation < 0.05:  # Increased threshold to 5cm
                        dextrous_points.append(positions[0])
    
    dextrous_points = np.array(dextrous_points)

    # Plot reachable workspace
    ax1.scatter(
        reachable_points[:, 0],
        reachable_points[:, 1],
        reachable_points[:, 2],
        c='blue',
        alpha=0.3,
        s=2,
        label='Reachable Points'
    )
    ax1.set_title("Reachable Workspace")
    ax1.legend()

    # Plot dextrous workspace
    if len(dextrous_points) > 0:
        ax2.scatter(
            dextrous_points[:, 0],
            dextrous_points[:, 1],
            dextrous_points[:, 2],
            c='red',
            alpha=0.3,
            s=2,
            label='Dextrous Points'
        )
    ax2.set_title("Dextrous Workspace")
    ax2.legend()

    # Make both plots consistent
    for ax in [ax1, ax2]:
        ax.set_xlabel("X (m)")
        ax.set_ylabel("Y (m)")
        ax.set_zlabel("Z (m)")
        ax.set_box_aspect([1, 1, 1])
        ax.view_init(elev=20, azim=45)
        # Set same axis limits for both plots
        ax.set_xlim([np.min(reachable_points[:, 0]), np.max(reachable_points[:, 0])])
        ax.set_ylim([np.min(reachable_points[:, 1]), np.max(reachable_points[:, 1])])
        ax.set_zlim([np.min(reachable_points[:, 2]), np.max(reachable_points[:, 2])])

    plt.suptitle("PincherX-100 Robot Workspaces", fontsize=16)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    robot = PincherX100()
    plot_workspaces(robot, samples=15)
