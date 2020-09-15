import sys
import os
import platform

import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn
import scipy
from scipy.stats import uniform
from scipy.stats import bernoulli
from scipy.stats import rv_discrete
from scipy.stats import norm
from scipy.stats import gamma
from scipy.stats import kstest

RANDOM_STATE = 31415

# let's do some carlo things
ages = range(1,100,1)

# norm stuff
mean, std_div = 3, 2
norm_dis = norm(loc = mean, scale = std_div)
x = np.linspace(-6, 12, 200)
print("values we got for x are:", x)
_, ax = plt.subplots(1, 1)
ax.plot(x, norm_dis.pdf(x), '-', lw=2)
plt.title("bologna")
plt.show()

# gamma stuff
gamma_distribution = gamma(loc = 3, scale = 3, a = 1)
x = np.linspace(0, 12, 200)
_, ax = plt.subplots(1, 1)
ax.plot(x, gamma_distribution.pdf(x), '-', lw=2)
plt.title('Exponential distribution (gamma with a = 1)')
plt.show()

def fit_and_plot(dist):
    params = dist.fit(ages)
    arg = params[:-2]
    loc = params[-2]
    scale = params[-1]
    x = np.linspace(0, 80, 80)
    _, ax = plt.subplots(1, 1)
    plt.hist(ages, bins = 80, range=(0, 80))
    ax2 = ax.twinx()
    ax2.plot(x, dist.pdf(x, loc=loc, scale=scale, *arg), '-', color = "r", lw=2)
    plt.show()
    return dist, loc, scale, arg

fit_and_plot(scipy.stats.norm)

# monte carlo intro
_90_conf_interval = 3.29
maintenance = norm(loc = (20 + 10) / 2, scale = (20 - 10) / _90_conf_interval)
labor = norm(loc = (8 + -2) / 2, scale = (8 - -2) / _90_conf_interval)
raw_material = norm(loc = (9 + 3) / 2, scale = (9 - 3) / _90_conf_interval)
prod_level = norm(loc = (35000 + 15000) / 2, scale = (35000 - 15000) / _90_conf_interval)
number_of_simulations = 1000000
maintenance_results = maintenance.rvs(number_of_simulations)
labor_results = labor.rvs(number_of_simulations)
raw_materials_results = raw_material.rvs(number_of_simulations)
prod_level_results = prod_level.rvs(number_of_simulations)
data = pd.DataFrame({
    "maintenance_savings_per_unit": maintenance_results,
    "labor_savings_per_unit": labor_results,
    "raw_materials_savings_per_unit": raw_materials_results,
    "production_level": prod_level_results
})
data["total_savings"] = (data.maintenance_savings_per_unit + data.labor_savings_per_unit + data.raw_materials_savings_per_unit) * data.production_level

plt.hist(data.total_savings, bins = 100)
plt.axvline(x = 400000, c = "r")
plt.show()

print(data[data["total_savings"] < 400000].count()["total_savings"] / 1000000)

# monte carlo 2
avg = 1
std_dev = .1
num_reps = 500
num_simulations = 1000
pct_to_target = np.random.normal(avg, std_dev, num_reps).round(2)
print(pct_to_target[:10]) # print only the first 10
