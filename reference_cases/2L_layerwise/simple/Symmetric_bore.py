import numpy as np

from shallowpy import run_model

model = '2L_layerwise'

# ## Domain size
L = 3   # domain length [m]
Hmax = 5   # water height [m]

# ## Grid parameters
tmax = 1  # s  max time
Nx = 500  # spatial grid points number (evenly spaced)
x = np.linspace(0, L, Nx)
dx = L/(Nx - 1)

# ## Numerical parameters
theta = 1

# ## bore properties
# gaussian
x0 = L/2
h0 = 1
sigma_0 = 0.2

# window
l0 = 3*sigma_0

# ## Initial condition
# Bottom topography
Z = 0*x

# layer 2 (lower)
h2 = np.ones_like(x) + h0*np.exp(-((x - x0)/sigma_0)**2) - Z  # gaussian
# h2 = np.ones_like(x) + np.where((x >= x0 - l0/2) &
#                                 (x <= x0 + l0/2), h0, 0) - Z  # window
q2 = np.zeros_like(x)

# layer 1 (upper) - h2
h1 = Hmax*np.ones_like(x) - h2
q1 = np.zeros_like(x)

W0 = np.array([h1, q1, h2, q2, Z])

# %% Run model
U, t = run_model(model, W0, tmax, dx, g=9.81, r=0.7, plot_fig=True,
                 dN_fig=100, x=x, Z=Z, theta=theta, dt_fact=0.5)