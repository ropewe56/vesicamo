import pint
u = pint.UnitRegistry()
pint.UnitRegistry(system='mks')
from numpy import *

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