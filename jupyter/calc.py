import numpy as np
import pylab as plt
from natural_constants import *

# ν = 700.0 / cm = 14.2 μm
# λ = 1/700.0 * 1.0e-2
# print(λ)

T = 2.0/5.0 * (sun_Sc * 0.7/c_σ)**0.25
print(T)
print(2.0/5.0, np.sqrt(np.sqrt(1.0/4.0)))
albedo = 0.3
T = (sun_Sc * (1.0-albedo)/c_σ)**0.25
print(T)
θ = np.mgrid[0.0:np.pi*0.5:1000j]
dθ = θ[1] - θ[0] 

S = sun_Sc*(1.0-albedo) * np.cos(θ)
T = (S/c_σ)**0.25
dA = np.sin(θ) * dθ
Tm = np.sum(T * dA) / 2.0
Te = (sun_Sc*(1.0-albedo)/4.0/c_σ)**0.25
print(T0-Tm, Te, T0-Te)
plt.plot(θ, S)
plt.plot(θ, T)
plt.figure()
plt.plot(θ, T*dA)
plt.show()
