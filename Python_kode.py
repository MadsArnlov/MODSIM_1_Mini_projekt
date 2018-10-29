import numpy as np


def arrivalTimes(planes):
    
    """
    arrivalTimes(planes)
    
    Returns arrival times for planes with the distribution from file 'interarrival.dat'
    
    Parameters
    ----------
    planes : int
        Number of planes trying to land
        
    Returns
    -------
    out : ndarray
        One dimentional array filled with arrival times of planes
    """
    
    arrivals = np.loadtxt('interarrival.dat', dtype = int, delimiter = ',')
    
    arrival = np.array([])
    
    for line in arrivals:
    
        x = line[0]
        y = line[1] + 1
    
        # Makes sure no division by 0
        if line[2] == 0:
            prob = 0
        
        # Calculates the probability of a plane arriving in a given timespace
        else:
            prob = int(planes // (arrivals.sum(axis=0)[2] / line[2]))
        
        # Makes sure no division by 0
        if prob == 0:
            interval = [0]
        else:
            interval = np.random.randint(x, y, prob)
    
        arrival = np.concatenate((arrival, interval), axis = None)
    
    np.random.shuffle(arrival)
    return(arrival)


def landingTimes(planes):
    
    """
    landingTimes(planes)
    
    Returns landing times for planes with the distribution from file 'duration.dat' as an array
    
    Parameters
    ----------
    planes : int
        Number of planes trying to land
        
    Returns
    -------
    out : ndarray
        One dimentional array filled with landing times of planes
    """
    
    landings = np.loadtxt('duration.dat', dtype = int, delimiter = ',')
    
    landing = np.array([])
    
    for line in landings:
    
        x = line[0]
        y = line[1] + 1
        
        # Makes sure no division by 0
        if line[2] == 0: 
            prob = 0
        
        # Calculates the probability of a plane landing in a given timespace
        else:
            prob = int(planes // (landings.sum(axis=0)[2] / line[2]))
        
        # Makes sure no division by 0
        if prob == 0:
            interval = [0]
        else:
            interval = np.random.randint(x, y, prob)
    
        landing = np.concatenate((landing, interval), axis = None)
    
    np.random.shuffle(landing)
    return(landing)


def waitTime(lanes, arrivalTimes, landingTimes):
    
    """
    waitTime(lanes, arrivalTimes, landingTimes)
    
    Prints the average and total wait time and returns waittimes as ndarray
    
    Parameters
    ----------
    lanes : int
        Number of lanes at the airfield
    arrivalTimes : ndarray
        Array containing the arrival times of the planes
    landingTimes : ndarray
        Array containing the landing times of the planes
    """
    
    queWait = [0 for i in range(lanes)] # Keeps track of avalible lanes
    laneWait = []
    
    # Loops through all planes
    for i in range(len(arrivalTimes)): 
            queWait += -arrivalTimes[i]
            
            # Makes sure no negative wait time
            for j in range(len(queWait)): 
                
                if queWait[j] < 0:    
                    queWait[j] = 0
                    
            # Keeps track of the time waited
            laneWait.append(min(queWait)) 
            
            # Updates the lane that is currently in use with the new waittime
            queWait[queWait.argmin()] += landingTimes[i] 
    
    print("Total wait time:", sum(laneWait), "seconds")
    print("Average wait time:", sum(laneWait)/len(laneWait), "seconds")
    
    return(laneWait)
        
arrival = arrivalTimes(200)
landing = landingTimes(200)

print("Length of array 'arrival':", len(arrival))
print("Length of array 'landing':", len(landing))    
    
