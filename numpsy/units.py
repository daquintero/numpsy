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
                "Hertz": core.Unit("Hertz", "Hz"),
                "Farad": core.Unit("Farad", "F"),
                "meter": core.Unit("meter", "m"),
                "ohm": core.Unit("ohm", "\Omega"),
                "ratio": core.Unit("ratio", ""),
                "second": core.Unit("second", "s"),
            },
            index=[0],
        ).iloc[0]

    @data.setter
    def data(self, unit):
        raise NotImplementedError("TODO units appender")


u = Units().data
