import pint
u = pint.UnitRegistry()
pint.UnitRegistry(system='mks')
import numpy as np

c_h   = 6.582119569e-34  # J * s
c_e   = 1.602176634e-19  # C
c_ϵ0  = 8.8541878128e-12 # A s / (V m)
c_me  = 9.1093837015e-31 # kg
c_m   = 1.6605390666e-27 # kg
c_c   = 2.99792458e8     # m/s
c_kB  = 1.38064852e-23   # J / K
c_σ   = 5.670374419e-8   # W / m**2 / K**4
c_h   = 6.62607015e-34   # J s
c_R   = 8.314462618      # J / mol / K
c_NA  = 6.02214076e23    # 1 / mol
c_T0  = 273.16           # K, 0 = C


u_h   = c_h   * u.J * u.s
u_e   = c_e   * u.A * u.s
u_ϵ0  = c_ϵ0  * u.A * u.s / (u.V * u.m)
u_me  = c_me  * u.kg
u_m   = c_m   * u.kg
u_c   = c_c   * u.m / u.s
u_kB  = c_kB  * u.J / u.K
u_σ   = c_σ   * u.W / u.m**2 / u.K**4
u_h   = c_h   * u.J * u.s
u_R   = c_R   * u.J / u.mol / u.K
u_NA  = c_NA  / u.mol
u_T0  = c_T0  * u.K

sun_surface_temp   = 5778.0    * u.K
solar_const        = 1367.0    * u.W/u.m**2
sun_earth_distance = 1.496e11  * u.m
sun_radius         = 6.96342e8 * u.m
earth_radius       = 6.371e8   * u.m

def uval(v):
    if isinstance(v, np.ndarray):
        return [x.magnitude for x in v]
    return v.magnitude


def uPlanckLaw(λ, T):
    x = uval(u_h * u_c / (u_kB * T * λ))
    x = np.where(x > 400.0, 400.0, x)
    U = 2.0 * np.pi * u_h * u_c**2 / λ**5 / (np.exp(x) - 1.0)
    return U

def  PlanckLaw(λ, T):
    """Radiation density [W m^{-3}] J/s / m²  (1/m)

    Arguments:
        λ {float} -- wavelength
        T {float} -- temperature

    Returns:
        float -- power / per area / per wavelength interval
    """
    x = c_h * c_c_0 / (c_k_B * T * λ)
    x = np.where(x > 400.0, 400.0, x)
    U = 2.0 * np.pi * c_h * c_c_0**2 / λ**5 / (np.exp(x) - 1.0)
    return U

