import numpy as np

planes = 200
lanes = 2

# =============================================================================
# Creates arrival times with the distribution from file 'ankomsttider.dat'.
# =============================================================================

arrivals = np.loadtxt('interarrival.dat', dtype = int, delimiter = ',')

arrival = np.array([])

for line in arrivals:

    x = line[0]
    y = line[1] + 1

    if line[2] == 0:
        prob = 0
    else:
        prob = int(planes // (arrivals.sum(axis=0)[2] / line[2]))
    if prob == 0:
        interval = [0]
    else:
        interval = np.random.randint(x, y, prob)

    arrival = np.concatenate((arrival, interval), axis = None)

np.random.shuffle(arrival)

# =============================================================================
# Creates landing times with the distribution from file 'landingstider.dat'.
# =============================================================================

landings = np.loadtxt('duration.dat', dtype = int, delimiter = ',')

landing = np.array([])

for line in landings:

    x = line[0]
    y = line[1] + 1

    if line[2] == 0:
        prob = 0
    else:
        prob = int(planes // (landings.sum(axis=0)[2] / line[2]))
    if prob == 0:
        interval = [0]
    else:
        interval = np.random.randint(x, y, prob)

    landing = np.concatenate((landing, interval), axis = None)

np.random.shuffle(landing)

# =============================================================================
# Computes total and average wait time and the wait time for each plane.
# =============================================================================

queWait = [0 for i in range(lanes)]
laneWait = []

for i in range(len(arrival)):
        queWait += -arrival[i]
        
        for j in range(len(queWait)):
            
            if queWait[j] < 0:    
                queWait[j] = 0
                
        laneWait.append(min(queWait)) 
        queWait[queWait.argmin()] += landing[i]

print(sum(laneWait))
        
        
wait = [0]

for i in range(1, len(arrival)):
    W = (landing[i-1] - arrival[i]) + wait[i-1]

    if W < 0:
        W = 0

    wait.append(W)

average_wait_time = sum(wait)/len(wait)
total_wait_time = sum(wait)
print(total_wait_time, '\n', average_wait_time)
