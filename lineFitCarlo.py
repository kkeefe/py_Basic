#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rv_continuous
import sys

# let distances be measured in cm..
DIST = 6 * (0.1 + 0.5) # y-separation, only 7 vertical bars so 6 gaps
LEN = 20  # bar length
# uncertainties for top and bottom bars, guess 1cm
DX1 = 1
DX2 = 1
# how many total points we want
NUM_MUONS = 1_000

# subclassing rv_continuous
# make sure to define lower(a) and upper(b) bounds..
class gen_cont(rv_continuous):
    "cos^2 distro"
    def _pdf(self, x):
        # normalize and change the bounds for x in [0,1)
        return np.cos(x)**2 / (np.pi/2)

# create a set of a pair of points..
# see which pairs make full detection, and other's that don't
class PointPair():
    def __init__(self, x=0, y=0, theta=0):
        # create the first point info
        self.x1 = x
        self.y1 = y
        self.t1 = theta

        # get the second point info
        self.y2 = DIST + self.y1
        self.x2 = self.get_x2(theta)

        # check to see if the pairs make sense.
        if self.x2 < 0 or self.x2 > 20:
            self.good_pair = False
        else:
            self.good_pair = True

    def get_x2(self, theta):
        """expect that theta is in rads"""
        return self.x1 + DIST * np.tan(theta)

class EventPointPairs(PointPair):
    def __init__(self, x, y, t, dx1, dx2):
        # make the true point pair
        super().__init__(x=x,y=y,theta=t)

        # make the measured points information:
        self.mx1 = self.x1 + dx1
        self.mx2 = self.x2 + dx2
        self.t2 = self.get_theta2()

        # see if we got a good point here..
        if self.mx2 < 0 or self.mx2 > 20:
            self.measured_good_pair = False
        else:
            self.measured_good_pair = True

    def get_theta2(self):
        """give this back in radians"""
        return np.arctan((self.y2 - self.y1) / (self.mx2 - self.mx1))

    # get values of the bar separation
    def get_bar_diff(self, barNum=1):
        """count the bars downward, since muon enters from top"""
        y = DIST * barNum / 6
        return y * ((1/np.tan(self.t2)) - (1/np.tan(self.t1))) + self.mx1 - self.x1


# want a series of uncertainties from hist fits given these random points

# seed it up
np.random.seed(5)

# get the runs
if len(sys.argv) < 2:
    print("running default:", NUM_MUONS)
else:
    try:
        NUM_MUONS = int(sys.argv[1])
    except Exception as ex:
        print(sys.argv[1], ", not an acceptable integer")
        print("please enter a valid integer")
        sys.exit(1)

# begin the carlo stuff
print("running %s event(s).." % NUM_MUONS)
c2 = gen_cont(name="muon", a=-np.pi/2, b=np.pi/2)
thetas = c2.rvs(size=NUM_MUONS)
x1 = 20 * np.random.sample(NUM_MUONS)
y1 = 0 * x1
# make the point errors:
dx1 = np.random.normal(0,DX1,NUM_MUONS)
dx2 = np.random.normal(0,DX2,NUM_MUONS)
good_evts = []
bad_evts = []

# make the points
for i in range(NUM_MUONS):
    p1 = EventPointPairs(x1[i],y1[i],thetas[i],dx1[i],dx2[i])
    if p1.good_pair and p1.measured_good_pair:
        good_evts.append(p1.get_bar_diff(1))
    else:
        bad_evts.append(p1)

y = np.array(good_evts)
