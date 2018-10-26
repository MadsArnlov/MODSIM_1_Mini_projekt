import numpy as np

planes = 200
lanes = 1
t = 0
wait = [0]


# Creates arrivals in the given distribution


infile = open('ankomsttider.dat', 'r')
b = []

for line in infile:
        
    words = line.split(' ')
    
    b.append(words)
        
infile.close()

arrival = np.array([])

for i in range(len(b)):

    x = float(b[i][0])
    y = float(b[i][1]) + 1

    if float(b[i][2]) == 0:
        prob = 0
    else:
        prob = int(planes//(200/float(b[i][2])))
    if prob == 0:
        interval = [0]
    else:
        interval = np.random.randint(x, y, prob)
        
    print((interval))
    arrival = np.concatenate((arrival,interval), axis=None)
    
np.random.shuffle(arrival)
print(arrival)

# =============================================================================
# 
# =============================================================================

infile = open('landingstider.dat', 'r')
c = []
    
for line in infile:
    words = line.split(' ')
    c.append(words)
        
infile.close()

landing = np.array([])

for i in range(len(b)):

    x = float(b[i][0])
    y = float(b[i][1]) + 1

    if float(b[i][2]) == 0:
        prob = 0
    else:
        prob = int(planes//(200/float(b[i][2])))
    if prob == 0:
        interval = [0]
    else:
        interval = np.random.randint(x, y, prob)
        
    print((interval))
    landing = np.concatenate((landing,interval), axis=None)
    
np.random.shuffle(landing)
print(landing)
    


# =============================================================================
# for i in range(1, planes):
#     V = (landing[i-1] - arrival[i]) + wait[i-1]
#     
#     if V < 0:
#         V = 0
#     
#     wait.append(V)
# 
# average_wait_time = sum(wait)/len(wait)
# total_wait_time = sum(wait)
# print(total_wait_time, '\n', average_wait_time)
# =============================================================================
