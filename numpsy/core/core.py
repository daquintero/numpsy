import numpy as np
import pandas as pd
import sympy as sy

def __check_properties__(instance, property):
    if (hasattr(instance.properties, property)):
        out = self.properties[property]
    else:
        out = None

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
    if (hasattr(instance, "numerical")):
        string_list += [" numerical:\""]
        string_list += [str(instance.numerical)]
        string_list += ["\""]
    if (hasattr(instance, "unit")):
        string_list += [" unit:\""]
        string_list += [str(instance.unit)]
        string_list += ["\""]
    string_list += [">"]
    return "".join(string_list)

def __numpsy_str__(instance):
    string_list = list([])
    class_name = instance.__class__.__name__
    string_list += ["<"]
    string_list += [class_name]
    if class_name == "Unit":
        delimeter = "\n\t\t"
    else:
        delimeter = "\n\t"
    if (hasattr(instance, "name")):
        string_list += [delimeter + "name:\""]
        string_list += [str(instance.name)]
        string_list += ["\""]
    if (hasattr(instance, "symbol")):
        string_list += [delimeter + "symbol:\""]
        string_list += [str(instance.symbol)]
        string_list += ["\""]
    if (hasattr(instance, "symbolic_expression")):
        string_list += [delimeter + "symbolic_expression:\""]
        string_list += [str(instance.symbolic_expression)]
        string_list += ["\""]
    if (hasattr(instance, "numerical")):
        string_list += [delimeter + "numerical:\""]
        string_list += [str(instance.numerical)]
        string_list += ["\""]
    if (hasattr(instance, "unit")):
        string_list += [delimeter + "unit:\""]
        string_list += [str(instance.unit)]
        string_list += ["\""]
    string_list += [delimeter + ">"]
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
    
    # def __str__(self):
    #     return __numpsy_str__(self)

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
            new.name = "(" + self.name + "_per_" + other.name + ")" 
        if (hasattr(self, "symbol") and (hasattr(other, "symbol"))):
            new.symbolic_expression = self.symbol / other.symbol
        return new
    
    def __mul__(self, other):
        new = Unit()
        if (hasattr(self, "name") and (hasattr(other, "name"))):
            new.name = "(" + self.name + "_times_" + other.name + ")" 
        if (hasattr(self, "symbol") and (hasattr(other, "symbol"))):
            new.symbolic_expression = self.symbol * other.symbol
        return new
    
    def __add__(self, other):
        new = Unit()
        if (hasattr(self, "name") and (hasattr(other, "name"))):
            new.name = "(" + self.name + "_plus_" + other.name + ")" 
        if (hasattr(self, "symbol") and (hasattr(other, "symbol"))):
            new.symbolic_expression = self.symbol + other.symbol
        return new
    
    def __sub__(self, other):
        new = Unit()
        if (hasattr(self, "name") and (hasattr(other, "name"))):
            new.name = "(" + self.name + "_minus_" + other.name + ")" 
        if (hasattr(self, "symbol") and (hasattr(other, "symbol"))):
            new.symbolic_expression = self.symbol - other.symbol
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
                 numerical = None,
                 unit = None,
                 symbolic_expression = None,
                ):
        self.__name__ = name
        self.__symbol__ = symbol
        self.__numerical__ = numerical
        self.__unit__ = unit
        self.__symbolic_expression__ = symbolic_expression
    
    @property
    def __type__(self):
        return("Value")
    
    def __truediv__(self, other):
        new = Value()
        if (hasattr(self, "name") and (hasattr(other, "name"))):
            new.name = "(" + self.name + "_per_" + other.name + ")" 
        if (hasattr(self, "symbol") and (hasattr(other, "symbol"))):
            new.symbolic_expression = self.symbol / other.symbol
        if (hasattr(self, "numerical") and (hasattr(other, "numerical"))):
            new.numerical = self.numerical / other.numerical
        if (hasattr(self, "unit") and (hasattr(other, "unit"))):
            new.unit = self.unit / other.unit
        return new
    
    def __mul__(self, other):
        new = Value()
        if (hasattr(self, "name") and (hasattr(other, "name"))):
            new.name = "(" + self.name + "_times_" + other.name + ")" 
        if (hasattr(self, "symbol") and (hasattr(other, "symbol"))):
            new.symbolic_expression = self.symbol * other.symbol
        if (hasattr(self, "numerical") and (hasattr(other, "numerical"))):
            new.numerical = self.numerical * other.numerical
        if (hasattr(self, "unit") and (hasattr(other, "unit"))):
            new.unit = self.unit * other.unit
        return new
    
    def __add__(self, other):
        new = Value()
        if (hasattr(self, "name") and (hasattr(other, "name"))):
            new.name = "(" + self.name + "_plus_" + other.name + ")" 
        if (hasattr(self, "symbol") and (hasattr(other, "symbol"))):
            new.symbolic_expression = self.symbol + other.symbol
        if (hasattr(self, "numerical") and (hasattr(other, "numerical"))):
            new.numerical = self.numerical + other.numerical
        if (hasattr(self, "unit") and (hasattr(other, "unit"))):
            new.unit = self.unit + other.unit
        return new
    
    def __sub__(self, other):
        new = Value()
        if (hasattr(self, "name") and (hasattr(other, "name"))):
            new.name = "(" + self.name + "_minus_" + other.name + ")" 
        if (hasattr(self, "symbol") and (hasattr(other, "symbol"))):
            new.symbolic_expression = self.symbol - other.symbol
        if (hasattr(self, "numerical") and (hasattr(other, "numerical"))):
            new.numerical = self.numerical - other.numerical
        if (hasattr(self, "unit") and (hasattr(other, "unit"))):
            new.unit = self.unit - other.unit
        return new
        
    @property
    def numerical(self):
        """Return unit numerical value shorthand"""
        return self.__numerical__
    
    @numerical.setter
    def numerical(self, value):
        self.__numerical__ = value
    
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
    n = numerical
    se = symbolic_expression

class Constant(Value):
    @Value.numerical.setter
    def numerical(self, value):
        raise Warning("Constant cannot be mutated. You cannot set any attribute value. Instantiate a new variable.")
    
    @Value.symbol.setter
    def symbol(self, value):
        raise Warning("Constant cannot be mutated. You cannot set any attribute value. Instantiate a new variable.")
    
    @Value.unit.setter
    def unit(self, value):
        raise Warning("Constant cannot be mutated. You cannot set any attribute value. Instantiate a new variable.")
    
    @Value.symbolic_expression.setter
    def symbolic_expression(self, value):
        """Set symbolic expression shorthand shorthand"""
        raise Warning("Constant cannot be mutated. You cannot set any attribute value. Instantiate a new variable.")
    
    # Shorthands
    u = unit
    s = symbol
    n = numerical
    se = symbolic_expression

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
            "meter": Unit("Meter", "m"),
        }, index=[0])
        
        return data_frame.iloc[0]

u = Units().data

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
    numerical=8.8541878128e-12,
    unit=farad_per_meter)
capacitor_plate_separation = Variable(
    name="capacitor_plate_separation",
    symbol= "d",
    numerical=None,
    unit=u.meter
)
# print(e_0.n)