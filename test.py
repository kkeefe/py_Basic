# from IPython import display
import numpy as np
import matplotlib.pyplot as plt

# plt.style.use('ggplot')

#s%matplotlib inline
rnd = np.random.RandomState(seed=10)

n_data = 16 # number of data points
a_true = rnd.uniform(-2, 5) # randomly chosen truth
b_true = rnd.uniform(-5, 5)

print("The true a is {} and the true b is {}".format(a_true, b_true))

x = rnd.uniform(0,2,n_data)
x.sort()

# evaluate the true model at the given x values
y = a_true*x + b_true

# Heteroscedastic Gaussian uncertainties only in y direction
y_err = rnd.uniform(0.5, 1.0, size=n_data) # randomly generate uncertainty for each datum
y = rnd.normal(y, y_err) # re-sample y data with noise

fig = plt.figure(figsize=(16,9))
plt.errorbar(x, y, y_err, linestyle='none', marker='o', color='k')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.tight_layout()
