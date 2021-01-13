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
                "pi": core.Constant(
                    "pi",
                    "\pi",
                    sp.pi,
                    self.units.ratio,
                ),
                "speed_of_light": core.Constant(
                    "speed_of_light",
                    "c",
                    299792458,
                    self.units.meter / self.units.second,
                ),
                "permittivity_vaccum": core.Constant(
                    "permittivity_vaccum",
                    "\epsilon_0",
                    8.8541878128e-12,
                    self.units.Farad / self.units.meter,
                ),
            },
            index=[0],
        )

        return data_frame.iloc[0]


c = Constants().data
