import numpy as np

h = 515*2
w = 625*2
f = 607

Int = np.array([[f, 0, w/2], [0, f, h/2], [0, 0 ,1]])


horfov = 2*np.arctan((w/2)/f)

print(f"horfov: {horfov:.4f}\n w: {w} \n h: {h}")
print(np.rad2deg(horfov))


print(Int)