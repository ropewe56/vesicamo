import pint
u = pint.UnitRegistry()
pint.UnitRegistry(system='mks')
from numpy import *
import os

# with units
u_e   = 1.602176634e-19  * u.A * u.s
u_ϵ_0 = 8.8541878128e-12 * u.A * u.s / (u.V * u.m)
u_m_e = 9.1093837015e-31 * u.kg
u_c_0 = 2.99792458e8     * u.m / u.s
u_k_B = 1.38064852e-23   * u.J / u.K
u_σ   = 6.670374419e-8   * u.W / u.m**2 / u.K**4
u_h   = 6.62607015e-34   * u.J * u.s
u_g   = 9.81             * u.m / u.second**2

# Universal gas constant
# R = C_p(mol) - C_v(mol)
u_N_A = 6.022140e23 /  u.mol
u_R = u_N_A * u_k_B
u_R = 8.3144598 * u.joule / u.mol / u.K   

# without units
c_e   = 1.602176634e-19  # C
c_ϵ_0 = 8.8541878128e-12 # A s / (V m)
c_m_e = 9.1093837015e-31 # kg
c_c_0 = 2.99792458e8     # m/s
c_k_B = 1.38064852e-23   # J / K
c_σ   = 6.670374419e-8   # W / m**2 / K**4
c_h   = 6.62607015e-34   # J s
u_g   = 9.81             # m / s**2

c_N_A = 6.022140e23      # 1 / mol
c_R   = c_N_A * c_k_B    # J/mol/K

#calorific value (heating value)  MJ/kg , t/m³
Petrol       = [41.0    * u.megajoule/u.kg, 0.75   * 1.0e3 * u.kg/u.m**3]
Ethanol      = [26.8    * u.megajoule/u.kg, 0.7894 * 1.0e3 * u.kg/u.m**3]
Methanol     = [19.9    * u.megajoule/u.kg, 0.7869 * 1.0e3 * u.kg/u.m**3]
Diesel       = [42.6    * u.megajoule/u.kg, 0.830  * 1.0e3 * u.kg/u.m**3]
H2           = [119.972 * u.megajoule/u.kg, 10.783         * u.megajoule/u.m**3] # MJ/kg, MJ/m³,  (0 °C und 101325 Pa) 
Methan       = [50.013  * u.megajoule/u.kg, 35.883         * u.megajoule/u.m**3] 
NaturalGas   = [0.5*(32+45) * u.megajoule/u.kg, 0.5*(31 + 41) * u.megajoule/u.m**3]


# Specific gas constant
# M - molar masse
# Rs = R / M 

# Ideal gas equation
# p * V = n * R * T
# p * V = N * k_B * T
# p * V = m * R_s * T

# internal energy
# U = 3/2 * n * R * T
# U = 3/2 * N * k_B * T

material = {'H2'  : {'Rs' : 4124.2 * u.J / u.kg / u.K, 'M' :  2.016 * u.g / u.mol},
            'CH4' : {'Rs' :  518.4 * u.J / u.kg / u.K, 'M' : 16.04  * u.g / u.mol},
            'Air' : {'Rs' : 287.08 * u.J / u.kg / u.K, 'M' : 32.00  * u.g / u.mol} }


material = {'Hydrogen'    : {'Rs'       : 4124.2              * u.J / u.kg / u.K, 
                             'M'        :  2.016              * u.g / u.mol,
                             'CalorificValue' : 119.972             * u.megajoule/u.kg, 
                             'rho'      : (10.783 / 119.9729) * u.kg/u.m**3},
            'Methan'      : {'Rs'       : 518.4               * u.J / u.kg / u.K, 
                             'M'        :  16.04              * u.g / u.mol,
                             'CalorificValue' : 50.013              * u.megajoule/u.kg,
                             'rho'      : (35.883 / 50.013)   * u.kg/u.m**3},
            'Air'         : {'Rs'       : 287.08              * u.J / u.kg / u.K, 
                             'M'        : 32.00               * u.g / u.mol},
            'Fuel'        : {'CalorificValue' : 41.0                * u.megajoule/u.kg, 
                             'rho'      : 0.75 * 1.0e3        * u.kg/u.m**3},
            'Ethanol'     : {'CalorificValue' : 26.8                * u.megajoule/u.kg, 
                             'rho'      : 0.7894 * 1.0e3      * u.kg/u.m**3},
            'Methanol'    : {'CalorificValue' : 19.9                * u.megajoule/u.kg, 
                             'rho'      : 0.7869 * 1.0e3      * u.kg/u.m**3},
            'Diesel'      : {'CalorificValue' : 42.6                * u.megajoule/u.kg, 
                             'rho'      : 0.830  * 1.0e3      * u.kg/u.m**3},
            'NatGas'      : {'CalorificValue' : 0.5*(32+45)         * u.megajoule/u.kg, 
                             'rho'      : 0.5*(31 + 41) / (0.5*(32+45)) * u.kg / u.m*3},
}