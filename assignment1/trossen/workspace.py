from trossen.robots import PincherX100
from matplotlib import pyplot as plt
import numpy as np


def plot_workspaces(robot, samples=15):
    """Plot both reachable and dextrous workspaces side by side"""
    fig = plt.figure(figsize=(20, 8))

    # Reachable Workspace
    ax1 = fig.add_subplot(121, projection="3d")

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
                t4 = theta4[0]
                T = robot.fkine([t1, t2, t3, t4])
                reachable_points.append(T.t)

    reachable_points = np.array(reachable_points)

    # Plot reachable workspace
    scatter1 = ax1.scatter(
        reachable_points[:, 0],
        reachable_points[:, 1],
        reachable_points[:, 2],
        c=reachable_points[:, 2],
        cmap="viridis",
        alpha=0.3,
        s=2,
    )

    plt.colorbar(scatter1, ax=ax1, label="Z Height (m)")
    ax1.set_xlabel("X (m)")
    ax1.set_ylabel("Y (m)")
    ax1.set_zlabel("Z (m)")
    ax1.set_title("Reachable Workspace")
    ax1.set_box_aspect([1, 1, 1])

    # Dextrous Workspace
    ax2 = fig.add_subplot(122, projection="3d")

    # Calculate dextrous workspace points
    dextrous_points = []
    for t1 in theta1:
        for t2 in theta2:
            for t3 in theta3:
                point_orientations = []
                for t4 in theta4:
                    T = robot.fkine([t1, t2, t3, t4])
                    point_orientations.append(T.t)
                point_orientations = np.array(point_orientations)
                if np.all(np.isfinite(point_orientations)):
                    dextrous_points.append(np.mean(point_orientations, axis=0))

    dextrous_points = np.array(dextrous_points)

    # Plot dextrous workspace
    if len(dextrous_points) > 0:
        scatter2 = ax2.scatter(
            dextrous_points[:, 0],
            dextrous_points[:, 1],
            dextrous_points[:, 2],
            c=dextrous_points[:, 2],
            cmap="viridis",
            alpha=0.3,
            s=2,
        )

        plt.colorbar(scatter2, ax=ax2, label="Z Height (m)")

    ax2.set_xlabel("X (m)")
    ax2.set_ylabel("Y (m)")
    ax2.set_zlabel("Z (m)")
    ax2.set_title("Dextrous Workspace")
    ax2.set_box_aspect([1, 1, 1])

    # Set the same view angle for both plots
    ax1.view_init(elev=20, azim=45)
    ax2.view_init(elev=20, azim=45)

    plt.suptitle("PincherX-100 Robot Workspaces", fontsize=16)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    robot = PincherX100()
    plot_workspaces(robot, samples=15)
