import pint
u = pint.UnitRegistry()
pint.UnitRegistry(system='mks')
import numpy as np
import os


c_h   = 6.582119569e-34  # J * s
c_e   = 1.602176634e-19  # C
c_ϵ_0 = 8.8541878128e-12 # A s / (V m)
c_m_e = 9.1093837015e-31 # kg
c_c_0 = 2.99792458e8     # m/s
c_k_B = 1.38064852e-23   # J / K
c_σ   = 5.670374419e-8   # W / m**2 / K**4
c_h   = 6.62607015e-34   # J s
c_R   = 8.314462618      # J / mol / K
c_NA  = 6.02214076e23    # 1 / mol
c_m   = 1.6605390666e-27 # kg


u_h   = c_h   * u.J * u.s
u_e   = c_e   * u.A * u.s
u_ϵ_0 = c_ϵ_0 * u.A * u.s / (u.V * u.m)
u_m_e = c_m_e * u.kg
u_c_0 = c_c_0 * u.m / u.s
u_k_B = c_k_B * u.J / u.K
u_σ   = c_σ   * u.W / u.m**2 / u.K**4
u_h   = c_h   * u.J * u.s
u_R   = c_R   * u.J / u.mol / u.K
u_NA  = c_NA  / u.mol
u_m   = c_m   * u.kg


sun_Ts             = 5778.0 # K 
sun_Sc             = 1367.0 # W/m^2
sun_earth_distance = 1.496e11 # m  
sun_radius         = 6.96342e8 # m  

T0                 = 273.16  # K, 0 = C


def Boltzman(λ, T):
    """Radiation density [W m^{-3}] J/s / m²  (1/m)   
    
    Arguments:
        λ {float} -- wavelength
        T {float} -- temperature
    
    Returns:
        float -- power / per area / per wavelength interval
    """
    x = c_h * c_c_0 / (c_k_B * T * λ)
    U = 2.0 * np.pi * c_h * c_c_0**2 / λ**5 / (np.exp(x) - 1.0)
    return U

