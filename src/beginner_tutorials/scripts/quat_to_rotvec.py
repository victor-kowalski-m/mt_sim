from scipy.spatial.transform import Rotation as R

def to_rotvec(input, output):
    all = []
    with open(input, "r") as f:
        lines = f.readlines()
        for line in lines:
            items = line.split(" ")
            items = [float(i) for i in items if i != ""]
            quat = R.from_quat(items[4:])
            items = items[:4] + quat.as_rotvec().tolist()
            all.append(items)
    with open(output, "w") as f:    
        for state in all:
            f.write(" ".join([f"{i:.4f}" for i in state])+"\n")