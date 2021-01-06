import numpy as np
import pandas as pd
import sympy as sy

class Unit():
    def __init__(self,
                 unit_name,
                 unit_symbol,
                ):
        self.unit = {
                "name": unit_name,
                "symbol": unit_symbol,
        }
        
    def __div__(self, other):
        if type(self.s) == type(other.s):
            return self.s / other.s
        
    @property
    def s(self):
        """Return unit symbol shorthand from Sympy"""
        return sy.Symbol(self.unit["symbol"])

class Units():
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
                 variable_name,
                 symbol,
                 numerical = None,
                 unit = None,
                 expression = None,
                ):
        self.value = {
                "name": variable_name,
                "symbol": symbol,
                "numerical": numerical,
                "unit": unit,
                "expression": expression,
        }
    
    @property
    def __type__(self):
        return("Value")
    
    def __div__(self, other):
        if type(self) == type(other):
            if (hasattr(self, "s") and (hasattr(other, "s")))
            return self.s / other.s
        
    @property
    def n(self):
        """Return unit numerical value shorthand"""
        return self.value["numerical"]
    
    @property
    def s(self):
        """Return unit symbol value shorthand"""
        return sy.Symbol(self.value["symbol"])
    
    @property
    def se(self):
        """Return symbolic expression shorthand shorthand"""
        return self.constant["expression"]
    
    


class Constant(Value):
    def __init__(self,
                 variable_name,
                 symbol,
                 numerical,
                 unit = None
                ):
        self.constant = {
                "name": variable_name,
                "symbol": symbol,
                "numerical": numerical,
                "unit": unit,
        }
        
    @property
    def n(self):
        """Return unit numerical value shorthand"""
        return self.constant["numerical"]
    
    @property
    def s(self):
        """Return unit symbol value shorthand"""
        return sy.Symbol(self.constant["symbol"])
    
class Variable(Value):
    
        

class Constants():
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
    
c =  Constants().data

