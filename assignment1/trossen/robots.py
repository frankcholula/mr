import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH
import matplotlib.pyplot as plt


class PincherX100(DHRobot):
    def __init__(self):
        links = [
            RevoluteDH(
                alpha=-np.pi / 2, a=0, d=0.08945, offset=0, qlim=[-np.pi, np.pi]
            ),
            RevoluteDH(
                alpha=0,
                a=0.10595,
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

