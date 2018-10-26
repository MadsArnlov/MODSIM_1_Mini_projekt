import numpy as np

planes = 200
lanes = 1
t = 0

landing = np.random.uniform(0,200,planes)
arrival = np.random.uniform(0,200,planes)

for i in len(arrival):
    if t >= arrival[i]:
        t += arrival[i]

print(t)
