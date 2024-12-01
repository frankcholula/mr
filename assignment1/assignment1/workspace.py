from assignment1.robots import PincherX100
from matplotlib import pyplot as plt
import numpy as np


def is_point_dextrous(
    robot, t1, t2, t3, theta4, position_threshold=0.05, angle_threshold=0.2
):
    # 1. Check for elbow singularities (both fully extended and folded back)
    arm_angle = abs(t2 + t3)
    if abs(arm_angle) < angle_threshold or abs(arm_angle - np.pi) < angle_threshold:
        return False, None

    # 2. Check for vertical alignment singularity
    if (abs(abs(t2) - np.pi / 2) < angle_threshold) and (abs(t3) < angle_threshold):
        return False, None

    # Collect positions for different wrist angles
    positions = []
    for t4 in theta4:
        T = robot.fkine([t1, t2, t3, t4])
        if T is not None:
            pos = [float(T.t[0]), float(T.t[1]), float(T.t[2])]
            positions.append(pos)

    # 3. Check wrist dexterity through position variation
    if len(positions) > 0:
        positions = np.array(positions)
        variation = np.max([np.std(positions[:, i]) for i in range(3)])
        if variation < position_threshold:
            return True, positions[0]

    return False, None


def calculate_workspace(robot, samples=15):
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
                is_dextrous, reference_position = is_point_dextrous(
                    robot, t1, t2, t3, theta4
                )
                if is_dextrous:
                    dextrous_points.append(reference_position)
    dextrous_points = np.array(dextrous_points)
    return reachable_points, dextrous_points


def plot_workspaces(robot, reachable_points, dextrous_points, samples=15):
    """Plot both reachable and dextrous workspaces side by side"""
    fig = plt.figure(figsize=(20, 8))
    ax1 = fig.add_subplot(121, projection="3d")
    ax2 = fig.add_subplot(122, projection="3d")

    # Plot reachable workspace
    ax1.scatter(
        reachable_points[:, 0],
        reachable_points[:, 1],
        reachable_points[:, 2],
        c="blue",
        alpha=0.3,
        s=2,
        label="Reachable Points",
    )
    ax1.set_title("Reachable Workspace")
    ax1.legend()

    # Plot dextrous workspace
    if len(dextrous_points) > 0:
        ax2.scatter(
            dextrous_points[:, 0],
            dextrous_points[:, 1],
            dextrous_points[:, 2],
            c="red",
            alpha=0.3,
            s=2,
            label="Dextrous Points",
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
    reachable_points, dextrous_points = calculate_workspace(robot)
    plot_workspaces(robot, reachable_points, dextrous_points)
