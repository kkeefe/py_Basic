#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import sys

# randomize the inputs
class Rand():
    def __init__(self, mean, sigma, counts):
        self.c = counts
        self.m = mean
        self.s = sigma
        self.vals = np.random.normal(mean, sigma, counts)

    # get the stuff
    def get_vals(self):
        return self.vals

    # get the mean
    def get_mean(self):
        return self.vals.mean()

# find the difference between points
class Point():

    def __init__(self, a=0,b=0):
        # get the true positions
        self.x = a
        self.y = b

        # get the skewed positions


if __name__ == '__main__':
    # seed it up
    np.random.seed(5)

    # get the runs
    if len(sys.argv) < 2:
        runs = 1_000
    else:
        try:
            runs = int(sys.argv[1])
        except Exception as ex:
            print(sys.argv[1], ", not an acceptable integer")
            print("please enter a valid integer")
            sys.exit(1)
    # begin the carlo stuff
    print("running %s event(s).." % runs)

    # insert the mean stuff
    mean = 5
    sigma = 1

    # means
    means = []

    # loop are we doing random things?
    for i in range(1000):
        # make the distro
        r1 = Rand(mean=mean, sigma=sigma, counts=runs)

        # add this mean in there
        means.append(r1.get_mean())

    # make the figure:
    # plt.hist(means)

    # define a function to want to graph
    x = np.arange(-np.pi/2,np.pi/2,0.1)
    y = np.cos(x)**2
    plt.plot(x,y)

    # graph it
    plt.show()
