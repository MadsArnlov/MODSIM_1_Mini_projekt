import numpy as np

planes = 200
lanes = 1
t = 0
wait = [0]

landing = np.random.randint(0, 200, planes)
arrival = np.random.randint(0, 200, planes)

for i in range(1, planes):
    V = (landing[i-1] - arrival[i]) + wait[i-1]
    
    if V < 0:
        V = 0
    
    wait.append(V)

average_wait_time = sum(wait)/len(wait)
total_wait_time = sum(wait)
print(total_wait_time, '\n', average_wait_time)
    
