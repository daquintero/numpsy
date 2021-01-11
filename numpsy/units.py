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
                "Farad": core.Unit("Farad", "F"),
                "meter": core.Unit("meter", "m"),
                "ratio": core.Unit("ratio", ""),
            },
            index=[0],
        ).iloc[0]

    @data.setter
    def data(self, unit):
        raise NotImplementedError("TODO units appender")


u = Units().data
