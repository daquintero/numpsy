import pandas as pd
from . import core


class Units:
    # TODO append method
    def __init__(self):
        pass

    @property
    def data(self):
        "Full dataframe"
        return pd.DataFrame(
            {
                "Hertz": core.Unit(name="Hertz", symbol="Hz"),
                "Farad": core.Unit(name="Farad", symbol="F"),
                "meter": core.Unit(name="meter", symbol="m"),
                "ohm": core.Unit(name="ohm", symbol="\Omega"),
                "ratio": core.Unit(name="ratio", symbol=""),
                "second": core.Unit(name="second", symbol="s"),
            },
            index=[0],
        ).iloc[0]

    @data.setter
    def data(self, unit):
        raise NotImplementedError("TODO units appender")


u = Units().data
