import numpy as np
import pandas as pd
import sympy as sy

def __check_properties__(instance, property):
    if (hasattr(instance.properties, property)):
        out = self.properties[property]
    else:
        out = None

"""def __numpsy_repr__(instance):
    string_list = list([])
    class_name = instance.__class__.__name__
    string_list += ["<"]
    string_list += class_name
    if (hasattr(instance, "symbol")):
        string_list += ["\""]
        string_list += [instance.symbol]
        string_list += ["\""]
    if (hasattr(instance, "number")):
        string_list += ["\""]
        string_list += [instance.number]
        string_list += ["\""]
    if (hasattr(instance, "unit")):
        string_list += ["\""]
        string_list += [instance.unit.symbol]
        string_list += ["\""]
    string_list += [">"]
    print(strig)
    return "".join(string_list)"""

def __numpsy_repr__(instance):
    string_list = list([])
    class_name = instance.__class__.__name__
    string_list += ["<"]
    string_list += [class_name]
    if (hasattr(instance, "name")):
        string_list += [" name:\""]
        string_list += [str(instance.name)]
        string_list += ["\""]
    if (hasattr(instance, "symbol")):
        string_list += [" symbol:\""]
        string_list += [str(instance.symbol)]
        string_list += ["\""]
    if (hasattr(instance, "symbolic_expression")):
        string_list += [" symbolic_expression:\""]
        string_list += [str(instance.symbolic_expression)]
        string_list += ["\""]
    if (hasattr(instance, "number")):
        string_list += [" number:\""]
        string_list += [str(instance.number)]
        string_list += ["\""]
    if (hasattr(instance, "unit")):
        string_list += [" unit:\""]
        string_list += [str(instance.unit)]
        string_list += ["\""]
    string_list += [">"]
    return "".join(string_list)
            
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
        
    def __repr__(self):
        return __numpsy_repr__(self)

class Unit(InstanceMixin):
    
    def __type__(self):
        return("Dimension")
    
    def __init__(self,
                 name = "",
                 symbol = "",
                 symbolic_expression = "",
                ):
        self.__name__ = name
        self.__symbol__ = symbol
        self.__symbolic_expression__ = symbolic_expression

    def __truediv__(self, other):
        new = Unit()
        if (hasattr(self, "name") and (hasattr(other, "name"))):
            new.name = "(" + self.name + "_by_" + other.name + ")" 
        if (hasattr(self, "symbol") and (hasattr(other, "symbol"))):
            new.symbolic_expression = self.symbol / other.symbol
        return new
    
    @property
    def symbol(self):
         """Return unit symbol shorthand from Sympy"""
         return sy.Symbol(self.__symbol__)
    
    @symbol.setter
    def symbol(self, value):
        self.__symbol__ = value
        
    @property
    def symbolic_expression(self):
        """Return symbolic expression shorthand shorthand"""
        return self.__symbolic_expression__
    
    @symbolic_expression.setter
    def symbolic_expression(self, value):
        """Set symbolic expression shorthand shorthand"""
        self.__symbolic_expression__ = value
            
    s = symbol
    se = symbolic_expression

class Value(InstanceMixin):
    
    def __init__(self,
                 name = "",
                 symbol = "",
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
            new.symbolic_expression = self.symbol / other.symbol
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
    
    # Shorthands
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

farad_per_meter = Unit("Farad", "F") / Unit("meter", "m")
e_0 = Constant(
    name="permittivity_vaccum",
    symbol= "\epsilon_0",
    number=8.8541878128e-12,
    unit=farad_per_meter)
print(e_0.s)