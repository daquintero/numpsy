import numpy as np
import pandas as pd
import sympy as sy

class Unit():
    def __type__(self):
        return("Dimension")
    
    def __init__(self,
                 name = None,
                 symbol = None,
                ):
        self.unit = {
                "name": name,
                "symbol": symbol,
        }
        
    def __truediv__(self, other):
        # TODO rearchitecht if self.__type__ == other.__type__ == "Dimension":
        return self.s / other.s
        
    @property
    def s(self):
        """Return unit symbol shorthand from Sympy"""
        return sy.Symbol(self.unit["symbol"])

class Units():
    # TODO append method
    def __init__(self):
         pass
        
    @property
    def data(self):
        "Full dataframe"
        data_frame =  pd.DataFrame({
            "Farad": Unit("Farad", "F"),
            "Meter": Unit("Meter", "m"),
        }, index=[0])
        
        return data_frame.iloc[0]


class Value():
    def __init__(self,
                 name = None,
                 symbol = None,
                 number = None,
                 unit = None,
                 expression = None,
                ):
        self.value = {
                "name": name,
                "symbol": symbol,
                "number": number,
                "unit": unit,
                "expression": expression,
        }
    
    @property
    def __type__(self):
        return("Value")
    
    def __truediv__(self, other):
        out = Value()
        # TODO rearchitect
        # if type(self) == type(other):
        if (hasattr(self, "s") and (hasattr(other, "s"))):
            out.value["symbol"] = self.s / other.s
        if (hasattr(self, "n") and (hasattr(other, "n"))):
            out.value["number"] = self.n / other.n
        # if (hasattr(self, "u") and (hasattr(other, "u"))):
        #    out.value["unit"].unit["symbol"] = self.u / other.u
        return out
        
    @property
    def n(self):
        """Return unit numerical value shorthand"""
        return self.value["number"]
    
    @property
    def s(self):
        """Return unit symbol value shorthand"""
        return sy.Symbol(self.value["symbol"])
    
    @property
    def u(self):
        """Return unit symbol unit shorthand"""
        return self.value["unit"]
    
    @property
    def se(self):
        """Return symbolic expression shorthand shorthand"""
        return self.constant["expression"]
    

class Constant(Value):
    pass

class Variable(Value):
    pass
        

class Constants():
    # TODO import from Pandas CSV
    def __init__(self):
        self.units = Units().data
    
    @property
    def data(self):
        "Symbols from Sympy"
        data_frame =  pd.DataFrame({
            "permittivity_vaccum": Constant("permittivity_vaccum",
                                            "\epsilon_0",
                                            8.8541878128e-12,
                                            self.units.Farad.s / self.units.Meter.s
                                           ),
        }, index=[0])
        
        return data_frame.iloc[0]

