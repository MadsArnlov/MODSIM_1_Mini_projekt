import numpy as np

def arrivalTimes(planes, year):
    
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
    
    probList = []
    nrPlanes = arrivals.sum(axis=0)[2]
    maxTime = 0 
    
    
    for line in arrivals:
        interval = int((line[1]-line[0]+1)*(1/1.05**year))
        prob = [(line[2]/nrPlanes)/interval for i in range(interval)]
        probList += prob
        maxTime += interval
    return np.random.choice(maxTime, planes, p=probList)
    

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
    probList = []
    nrPlanes = landings.sum(axis=0)[2]
    maxTime = landings[-1][1]+1
    
    
    for line in landings:
        interval = line[1]-line[0]+1
        prob = [(line[2]/nrPlanes)/interval for i in range(interval)]
        probList += prob
        
    return np.random.choice(maxTime, planes, p=probList)


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
        
    Returns
    ----------
    out : string
        Prints the Total, Average and Maximum wait time
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
    
    return(laneWait)

def simulations(N, lanes=1, year=1):

    totalWait = 0
    averageWait = 0
    maxWait = 0
    planes = int(200*1.05**year)
    
    for n in range(N):
        waitLane = waitTime(lanes, arrivalTimes(planes, year), landingTimes(planes))
        waitTotal = sum(waitLane)
        waitAvg = sum(waitLane)/len(waitLane)
        waitMax = max(waitLane)
        totalWait += waitTotal
        averageWait += waitAvg
        maxWait += waitMax
        
    if totalWait/N <= 86400:
        print("Total Ventetid:", totalWait/N, "sekunder")
        print("Gennemsnitlig Ventetid:", averageWait/N, "sekunder")
        print("Maksimal Ventetid:", maxWait/N, "sekunder")
    else:
        print("Kan ikke nå alle fly på en dag")
        print("Timer for meget", ((totalWait/N)-86400)/60/60)


simulations(1000, lanes=1, year=8)