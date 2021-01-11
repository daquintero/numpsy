import pandas as pd
from . import core
from . import units


class Constants:
    # TODO import from Pandas CSV
    def __init__(self):
        self.units = units.Units().data

    @property
    def data(self):
        "Symbols from Sympy"
        data_frame = pd.DataFrame(
            {
                "permittivity_vaccum": core.Constant(
                    "permittivity_vaccum",
                    "\epsilon_0",
                    8.8541878128e-12,
                    self.units.Farad / self.units.Meter,
                ),
            },
            index=[0],
        )

        return data_frame.iloc[0]
