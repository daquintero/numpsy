import pandas as pd
import scipy as sp
from . import core
from . import units


class Constants:
    # TODO connect to scipy library
    # TODO import from Pandas CSV
    def __init__(self):
        self.units = units.Units().data

    @property
    def data(self):
        "Symbols from Sympy"
        data_frame = pd.DataFrame(
            {
                "impedance_free_space": core.Constant(
                    name="impedance_free_space",
                    symbol="\eta_0",
                    numerical=377,
                    unit=self.units.ohm,
                ),
                "permeability_relative_vaccum": core.Constant(
                    name="permeability_relative_vaccum",
                    symbol="\mu_{r0}",
                    numerical=1,
                    unit=self.units.Henry / self.units.meter,
                ),
                "permittivity_relative_intrinsic_silicon": core.Constant(
                    name="permeability_relative_intrinsic_silicon",
                    symbol="\epsilon_{Si}",
                    numerical=11.7,
                    unit=self.units.Farad / self.units.meter,
                ),
                "permittivity_relative_silicon_dioxide": core.Constant(
                    name="permeability_relative_silicon_dioxide",
                    symbol="\epsilon_{SiO2}",
                    numerical=3.9,
                    unit=self.units.Farad / self.units.meter,
                ),
                "permittivity_relative_vaccum": core.Constant(
                    name="permeability_relative_vaccum",
                    symbol="\epsilon_{r0}",
                    numerical=1,
                    unit=self.units.Farad / self.units.meter,
                ),
                "permittivity_vaccum": core.Constant(
                    name="permittivity_vaccum",
                    symbol="\epsilon_0",
                    numerical=8.8541878128e-12,
                    unit=self.units.Farad / self.units.meter,
                ),
                "pi": core.Constant(
                    name="pi",
                    symbol="\pi",
                    numerical=sp.pi
                ),
                "speed_of_light": core.Constant(
                    name="speed_of_light",
                    symbol="c",
                    numerical=299792458,
                    unit=self.units.meter / self.units.second,
                ),
            }, index=[0])

        data_frame["c"] = data_frame.speed_of_light
        data_frame["e_0"] = data_frame.permittivity_vaccum
        data_frame["e_r_0"] = data_frame.permittivity_relative_vaccum
        data_frame["e_r_si"] = data_frame.permittivity_relative_intrinsic_silicon
        data_frame["e_r_sio2"] = data_frame.permittivity_relative_silicon_dioxide
        data_frame["eta_0"] = data_frame.impedance_free_space
        data_frame["mu_r_0"] = data_frame.permeability_relative_vaccum

        return data_frame.iloc[0]

# TODO potentially rename to constants library
c = Constants().data
