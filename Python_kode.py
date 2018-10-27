import numpy as np

planes = 200
lanes = 1
t = 0
wait = [0]

# =============================================================================
# Creates arrival times with the distribution from file 'ankomsttider.dat'.
# =============================================================================

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

    arrival = np.concatenate((arrival, interval), axis=None)

np.random.shuffle(arrival)

# =============================================================================
# Creates landing times with the distribution from file 'landingstider.dat'.
# =============================================================================

infile = open('landingstider.dat', 'r')
b = []

for line in infile:
    words = line.split(' ')
    b.append(words)

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

    landing = np.concatenate((landing, interval), axis=None)

np.random.shuffle(landing)

# =============================================================================
# Computes total and average wait time and the wait time for each plane.
# =============================================================================

filled_lanes = [0 for lane in range(lanes)]
time_lanes = [0 for lane in range(lanes)]
wait_test = [0 for i in range(len(arrival))]

for i in range(0, len(arrival)):
    ### Note ### Hvad skal den gøre? Returnerer den ikke det index som har værdien 0?
    if time_lanes.index(0) >= 0:    # Hvis en lane er fri, vil tiden til den lane være 0 (start tilstand)
        wait_time = 0
        time = landing[i]
    else:
        if arrival <= max(time_lanes):
            wait_time = 0
            time = landing[i]
            time_lanes[time_lanes.indx(max(time_lanes))] = time
    wait_test[i] = wait_time
    time_lanes[time_lanes.index(0)] = time
    ### Note ### Der forsøges at sætte et index til float. Tror ikke den går

filled_lanes[filled_lanes.index(0)] = 1

#for i in range(1, len(arrival)):
#    W = (landing[i-1] - arrival[i]) + wait[i-1]
#
#    if W < 0:
#        W = 0
#
#    wait.append(W)
#
average_wait_time = sum(wait)/len(wait)
total_wait_time = sum(wait)
print(total_wait_time, '\n', average_wait_time)

# =============================================================================
# Keeping track of filled lanes.
# =============================================================================

