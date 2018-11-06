import numpy as np
import sys
import os
from matplotlib import pyplot as plt


def arrivalTimes(planes, year):
    """
    arrivalTimes(planes, years)

    Returns arrival times for planes with the distribution from
    the file "interarrival.dat"

    Parameters
    ----------
    planes : int
        Number of planes trying to land
    year : int
        What year the calculation is set

    Returns
    -------
    out : ndarray
        One dimentional array filled with arrival times of planes
    """

    arrivals = np.loadtxt("interarrival.dat", dtype=int, delimiter=",")
    probList = []
    nrPlanes = arrivals.sum(axis=0)[2]
    maxTime = 0

    for line in arrivals:
        interval = int((line[1] - line[0] + 1)*(1/1.05**year))
        prob = [(line[2]/nrPlanes)/interval for i in range(interval)]
        probList += prob
        maxTime += interval
        
    return np.random.choice(maxTime, planes, p=probList)


def landingTimes(planes):
    """
    landingTimes(planes)

    Returns landing times for planes with the distribution from
    the file "duration.dat" as an array

    Parameters
    ----------
    planes : int
        Number of planes trying to land

    Returns
    -------
    out : ndarray
        One dimentional array filled with landing times of planes
    """

    landings = np.loadtxt("duration.dat", dtype=int, delimiter=",")
    probList = []
    nrPlanes = landings.sum(axis=0)[2]
    maxTime = landings[-1][1] + 1

    for line in landings:
        interval = line[1] - line[0] + 1
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
        Returns the Total wait time
    """

    # Keeps track of avalible lanes
    queueWait = [0 for i in range(lanes)]
    laneWait = []

    # Loops through all planes
    for i in range(len(arrivalTimes)):
            queueWait -= arrivalTimes[i]

            # Makes sure no negative wait time
            for j in range(len(queueWait)):

                if queueWait[j] < 0:
                    queueWait[j] = 0

            # Keeps track of the time waited
            laneWait.append(min(queueWait))

            # Updates the lane that is currently in use with the new waittime
            queueWait[queueWait.argmin()] += landingTimes[i]

    return laneWait


def simulations(year, sims, lanes, willPrint=False):
    """
    simulations(year, N, lanes, willPrint=False)

    Returns the average, max and total wait time based on multiple simulations
    in a given year. Will also print the data if specified.

    Parameters
    ----------
    years : int
        Last year shown on the plot
    sims: int
        Number of simulations to run each year
    lanes : int
        Number of lanes at the airfield
    willPrint : bool
        Whether to print the data or not

    Returns
    ----------
    out : list
        Returns (total wait time, the average wait time, the max wait time)
        in a list
    (optional) : str
        Prints the calculated data with two decimal points
    """

    waitTotal = 0
    waitAvg = 0
    waitMax = 0
    arrivalSum = 0
    landings = np.loadtxt("duration.dat", dtype=int, delimiter=",")
    planes = int(landings.sum(axis=0)[2]*1.05**year)
    lastWait = waitTime(lanes, arrivalTimes(planes, year), landingTimes(planes))[-1]
    lastLanding = landingTimes(planes)[-1]

    try:
        for i in range(sims):
            waitLane = waitTime(lanes, arrivalTimes(planes, year), landingTimes(planes))
            waitTotal += sum(waitLane)/sims
            waitAvg += (sum(waitLane)/len(waitLane))/sims
            waitMax += max(waitLane)/sims
            arrivalSum += sum(arrivalTimes(planes, year))/sims

        if willPrint:

            if arrivalSum + lastWait + lastLanding <= 86400:
                print("Total wait time: {:.2f} seconds".format(waitTotal))
                print("Average wait time: {:.2f} seconds".format(waitAvg))
                print("Maximum wait time: {:.2f} seconds".format(waitMax))
            else:
                print("Can't fit all planes into one day!")
                print("Hours exceeding the daily maximum", ((waitTotal + arrivalSum) - 86400)/60/60)

        return waitTotal, waitAvg, waitMax

    except:
        print("""Can't calculate that many years in the future.
              Please try again with a smaller number""")


def plotGrowth(years, sims, lanes, timeStyle):
    """
    plotGrowth(years, sims, lanes, timeStyle)

    Plots the graphs using the given parameters. With Years on the x-axis,
    and timeStyle on the y-axis

    Parameters
    ----------
    years : int
        Last year shown on the plot
    sims: int
        Number of simulations to run each year
    lanes : int
        Number of lanes at the airfield
    timeStyle : str
        What type of data to be plotted along the y axis.
    Total => Total wait time
    Average => Average wait time
    Maximum => Maximum wait time

    Returns
    ----------
    out : figure
        Saves the figure as png in the same folder as the program.
    """

    data = []
    timeStyle = timeStyle.lower()

    # Handles plot of average wait as function of time
    if timeStyle == "average" or timeStyle == "avg":

        for year in range(years):
            data.append(simulations(year, sims, lanes)[1])

        plt.figure(figsize=(12, 9))
        plt.plot(data, "o-", label="Average wait time per year")
        plt.axhline(y=300, color="red", label="Tolerance in seconds")
        plt.title("Years simulated: {:d}\n Simulations per year: {:d}\n Lanes: {:d}".format(years, sims, lanes))
        plt.xlabel("Years")
        plt.ylabel("Average wait in seconds")
        plt.legend(fontsize="large")
        plt.savefig("SimAvg_year{:d}_sims{:d}_lane{:d}.png".format(years, sims, lanes))

    # Handles plot of maximum wait as function of time
    elif timeStyle == "maximum" or timeStyle == "max":

        for year in range(years):
            data.append(simulations(year, sims, lanes)[2])

        plt.figure(figsize=(12, 9))
        plt.plot(data, "o-")
        plt.title("Years simulated: {:d}\n Simulations per year: {:d}\n Lanes: {:d}".format(years, sims, lanes))
        plt.xlabel("Years")
        plt.ylabel("Max wait in seconds")
        plt.savefig("SimMax_year{:d}_sims{:d}_lane{:d}.png".format(years, sims, lanes))


    # Handles plot of total wait as function of time
    elif timeStyle == "total" or timeStyle == "sum":

        for year in range(years):
            data.append(simulations(year, sims, lanes)[0])

        plt.figure(figsize=(12, 9))
        plt.axhline(y=86400, color="red", label='Seconds per day')
        plt.plot(data, "o-", label="Total wait time per year")
        plt.title("Years simulated: {:d}\n Simulations per year: {:d}\n Lanes: {:d}".format(years, sims, lanes))
        plt.xlabel("Years")
        plt.ylabel("Total wait in seconds")
        plt.legend(fontsize="large")
        plt.savefig("SimTotal_year{:d}_sims{:d}_lane{:d}.png".format(years, sims, lanes))

    # Error handeling
    else:
        print("'TimeStyle' not permitted. Use average, maximum or total")


# Prints usage-description
if len(sys.argv) == 1 or sys.argv[1] == "?":
    print("""
    Either prints the wait time data for one year if plot=True
    or saves a plot of the growth over multiple years

    Parameters
    ----------
    Years: int
        What year the calculation should terminate
    Simulations : int
        Number of simulations to be run for each year.
    Lanes : int
        Number of lanes to be simulated.
    TimeStyle : str
        What type of data to be plotted along the y axis.
        Total => Total wait time
        Average => Average wait time
        Maximum => Maximum wait time
    Plot : bool
        Defines whether or not to plot the data or to return a single year

    Usage:
    >>> name.py Years Simumlations Lanes TimeStyle/Plot

    Example 1:
    >>> airport.py 20 35 2 total

    Example 2:
    >>> airport.py 20 35 2 True
    """)

# Handles arguments if a single datapoint is specified
elif sys.argv[4].lower() == "true":
    try:
        simulations(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), willPrint=True)
    except:
        print("Something went wrong! Please try the command again")

# Handles arguments if multiple datapoints is specified
else:
    try:

        plotGrowth(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4].lower())
        print("Plot has been created in: {:s}".format(os.path.dirname(sys.argv[0])))
    except:
        print("Something went wrong! Please try the command again")
