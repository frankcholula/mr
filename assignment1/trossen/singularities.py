from trossen.robots import PincherX100
import numpy as np

if __name__ == "__main__":
    robot = PincherX100()
    # 1. Reach Singularities: Fully extended configuration
    q_reach_singularity = [0, 0, 0, 0]

    # 2. Wrist Singularities: Joint 3 and Joint 4 align
    q_wrist_singularity = [0, np.pi / 2, -np.pi / 2, 0]

    # 3. Joint Alignment Singularities: Joints 2 and 3 align with the base
    q_joint_alignment_singularity = [0, 0, 0, np.pi / 2]

    J_reach = robot.jacob0(q_reach_singularity)
    print("Jacobian at Reach Singularity:")
    print(J_reach)
    print("Visualizing Reach Singularity...")
    robot.plot(
        q_reach_singularity,
        block=True,
        limits=[-0.3, 0.3, -0.2, 0.2, 0, 0.4],
        jointaxes=True,
        eeframe=True,
    )

    J_wrist = robot.jacob0(q_wrist_singularity)
    J_joint_align = robot.jacob0(q_joint_alignment_singularity)

    # print("Visualizing Wrist Singularity...")
    # robot.plot(q_wrist_singularity, block=True)

    # print("Visualizing Joint Alignment Singularity...")
    # robot.plot(q_joint_alignment_singularity, block=True)

    # print("\nJacobian at Wrist Singularity:")
    # print(J_wrist)
    # print("\nJacobian at Joint Alignment Singularity:")
    # print(J_joint_align)
