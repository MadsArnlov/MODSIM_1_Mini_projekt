import numpy as np

planes = 200
lanes = 1
t = 0
wait = [0]

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

time_lanes = [0 for lane in range(lanes)]
wait_test = [0 for i in range(len(arrival))]

for i in range(0, len(arrival)):
    ### Note ### Hvad skal den gøre? Returnerer den ikke det index som har værdien 0?
    if 0 in time_lanes:    # Hvis en lane er fri, vil tiden til den lane være 0 (start tilstand)
        wait_time = 0
        time = landing[i]
        time_lanes[time_lanes.index(0)] = time
    elif arrival[i] >= max(time_lanes):
        wait_time = 0
        time = landing[i]
        time_lanes[time_lanes.index(max(time_lanes))] = time
    else:
        wait_time = landing[i - 1] - arrival[i] + wait_test[i - 1]
        if wait_time < 0:
            wait_time = 0
    wait_test[i] = wait_time
    ### Note ### Der forsøges at sætte et index til float. Tror ikke den går

print(sum(wait_test), '\n', sum(wait_test)/len(wait_test))


for i in range(1, len(arrival)):
    W = (landing[i-1] - arrival[i]) + wait[i-1]

    if W < 0:
        W = 0

    wait.append(W)

average_wait_time = sum(wait)/len(wait)
total_wait_time = sum(wait)
print(total_wait_time, '\n', average_wait_time)
