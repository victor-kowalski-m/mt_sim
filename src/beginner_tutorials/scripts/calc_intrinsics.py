import numpy as np

h = 406
w = 528
f = 684

Int = np.array([[f, 0, w/2], [0, f, h/2], [0, 0 ,1]])


horfov = 2*np.arctan((w/2)/f)

print(f"{horfov:.4f}")
print(np.rad2deg(horfov))


print(Int)