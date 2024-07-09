import csv
import os
import numpy as np
from scipy.spatial.transform import Rotation as R
import sys


zrot = R.from_rotvec([0, 0, -np.pi/2])
xrot = R.from_rotvec([-np.pi/2, 0, 0])

total_rot = zrot*xrot

print(total_rot.as_matrix())

trafo = np.eye(4, 4)
trafo[0:3, 0:3] = total_rot.as_matrix()
trafo[0:3, 3] = np.array([0.1177, -0.0422, -0.0826])

print(trafo)

sys.exit()

base_dir = "/home/victor/Downloads/traj_to_slam"

all = []

for edge in ["left", "upper", "right", "lower"]:
    with open(f'{base_dir}/{edge}/trajectory.dat') as f:
        lines = f.readlines()
        for line in lines:
            items = line.split(" ")
            items = [float(i) for i in items if i != ""]
            all.append(items)

all

all_processed = []
for i in range(len(all)):
    state = []
    state += all[i][1:4]
    quat = R.from_rotvec(all[i][4:7]).as_quat() 
    state += quat.tolist()
    all_processed.append(state)
    state += all[i][7:19]

all_processed

all_processed_np = np.array(all_processed)

all_processed_np

np.save("/home/victor/catkin_ws/data/trajectory", all_processed_np)