using Unitful
using Common
using UPhysConst

sun_surface_temp   = 5778.0    * u"K "
solar_const        = 1367.0    * u"W/m^2"
sun_earth_distance = 1.496e11  * u"m"
sun_radius         = 6.96342e8 * u"m"

"""
    Radiation density [W m^{-3}] J/s / m²  (1/m)

    λ {float} -- wavelength
    T {float} -- temperature
    float -- power / per area / per wavelength interval
"""
function  PlanckLaw(λ, T)
    x = @. u_h * u_c / (u_kB * T * λ)
    U = @. 2.0 * π  * u_h * u_c^2 / λ^5 / (exp(x) - 1.0)
    U
end

