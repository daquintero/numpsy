import numpy as np
import pandas as pd
import sympy as sy

def __check_properties__(instance, property):
    if (hasattr(instance.properties, property)):
        out = self.properties[property]
    else:
        out = None

def __numpsy_repr__(instance):
    class_name = instance.__class__.__name__
   
    return "<Unit name:\"" \
            + str(self.properties["name"]) \
            + "\" symbol:\"" \
            + str(self.properties["symbol"]) \
            + "\">"

class InstanceMixin():
    def __init__(self,
                 name = None,
                ):
        self.__name__ = name
        
    @property
    def name(self):
        """Return name string"""
        return self.__name__
    
    @name.setter
    def name(self, value):
        self.__name__ = value

class Unit(InstanceMixin):
    
    def __type__(self):
        return("Dimension")
    
    def __init__(self,
                 name = None,
                 symbol = None,
                ):
        self.__name__ = name
        self.__symbol__ = symbol

    def __truediv__(self, other):
        new = Unit()
        if (hasattr(self, "name") and (hasattr(other, "name"))):
            new.name = "(" + self.name + "_by_" + other.name + ")" 
        if (hasattr(self, "symbol") and (hasattr(other, "symbol"))):
            new.symbol = self.symbol / other.symbol
        return new
    
    @property
    def symbol(self):
         """Return unit symbol shorthand from Sympy"""
         return sy.Symbol(self.__symbol__)
    
    @symbol.setter
    def symbol(self, value):
        self.__symbol__ = value
            
    s = symbol

class Value(InstanceMixin):
    
    def __init__(self,
                 name = None,
                 symbol = None,
                 number = None,
                 unit = None,
                 symbolic_expression = None,
                ):
        self.__name__ = name
        self.__symbol__ = symbol
        self.__number__ = number
        self.__unit__ = unit
        self.__symbolic_expression__ = symbolic_expression
    
    @property
    def __type__(self):
        return("Value")
    
    def __truediv__(self, other):
        new = Value()
        if (hasattr(self, "symbol") and (hasattr(other, "symbol"))):
            new.symbol = self.symbol / other.symbol
        if (hasattr(self, "number") and (hasattr(other, "number"))):
            new.number = self.number / other.number
        if (hasattr(self, "unit") and (hasattr(other, "unit"))):
            new.unit = self.unit / other.unit
        return new
        
    @property
    def number(self):
        """Return unit numerical value shorthand"""
        return self.__number__
    
    @number.setter
    def number(self, value):
        self.__number__ = value
    
    @property
    def symbol(self):
        """Return unit symbol value shorthand"""
        return sy.Symbol(self.__symbol__)
    
    @symbol.setter
    def symbol(self, value):
        self.__symbol__ = value
    
    @property
    def unit(self):
        """Return unit symbol unit shorthand"""
        return self.__unit__
    
    @unit.setter
    def unit(self, value):
        self.__unit__ = value
    
    @property
    def symbolic_expression(self):
        """Return symbolic expression shorthand shorthand"""
        return self.__symbolic_expression__
    
    @symbolic_expression.setter
    def symbolic_expression(self, value):
        """Set symbolic expression shorthand shorthand"""
        self.__symbolic_expression__ = value
    
    u = unit
    s = symbol
    n = number
    se = symbolic_expression

class Constant(Value):
    pass

class Variable(Value):
    pass

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
                                            self.units.Farad / self.units.Meter
                                           ),
        }, index=[0])
        
        return data_frame.iloc[0]

