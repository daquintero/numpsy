import sympy as sy
import pandas as pd
from . import configuration
from . import helpers
from . import printers


class DataMixin:
    def __init__(self):
        super(DataMixin, self).__init__()

    @property
    def data(self):
        data = {}
        if hasattr(self, "name"):
            data["name"] = self.name
        if hasattr(self, "name_expression"):
            data["name_expression"] = self.name_expression
        if hasattr(self, "numerical"):
            data["numerical"] = self.numerical
        if hasattr(self, "symbol"):
            if bool(self.symbol):
                a = sy.latex(self.symbol, mode="equation")
                data["symbol"] = a
            else:
                raise ValueError("Sympy incompatible symbol input: self.symbol: " + str(self.__symbol__) + " for class: " + str(self.__class__))
        if hasattr(self, "symbolic_expression"):
            if sy.latex(self.symbolic_expression):
                b = sy.latex(self.symbolic_expression, mode="equation")
            else:
                b = ""
            data["symbolic_expression"] = b
        if hasattr(self, "unit"):
            # if self.unit.symbol:
            #    data["unit"] = "$" + self.unit.__symbol__ + "$"
            # else:
            #    data["unit"] = "$" + sy.latex(self.unit.data.symbolic_expression) + "$"
            self.unit.data.symbol = "$" + self.unit.data.symbol + "$"
            self.unit.data.symbolic_expression = (
                "$" + self.unit.data.symbolic_expression + "$"
            )
            data["unit"] = (
                "Symbol: "
                + self.unit.data["symbol"].values[0]
                + "\n"
                + "Symbolic Expression: "
                + self.unit.data["symbolic_expression"].values[0]
            )
        return pd.DataFrame([data], index=[self.__class__.__name__])

    @data.setter
    def data(self, value):
        if hasattr(self, "name") & hasattr(value, "name"):
            self.name = value.name
        if hasattr(self, "name_expression") & hasattr(value, "name_expression"):
            self.name_expression = value.name_expression
        if hasattr(self, "numerical") & hasattr(value, "numerical"):
            self.numerical = value.numerical
        if hasattr(self, "symbol") & hasattr(value, "symbol"):
            self.symbol = value.__symbol__
        if hasattr(self, "symbolic_expression") & hasattr(value, "symbolic_expression"):
            self.symbolic_expression = value.__symbolic_expression__
        if hasattr(self, "unit") & hasattr(value, "unit"):
            self.unit = value.unit


class InstanceMixin(DataMixin):
    def __init__(
        self,
        name=configuration.undefined_unit_name,
        n=configuration.undefined_unit_name,
        name_expression=configuration.undefined_unit_name,
    ):
        super(InstanceMixin, self).__init__()
        self.__name__ = helpers.__select_available_property__(name,
                                                              n,
                                                              configuration.undefined_unit_name)
        self.__name_expression__ = helpers.__select_available_property__(name_expression,
                                                                         self.__name__,
                                                                         configuration.undefined_unit_name)
        self.data

    @property
    def name(self):
        """Return name string"""
        return self.__name__

    @name.setter
    def name(self, value):
        self.__name__ = value

    @property
    def name_expression(self):
        """Return name expression consisting of an equivalent string representation to name"""
        return self.__name_expression__

    @name_expression.setter
    def name_expression(self, value):
        """Set name expression consisting of an equivalent string representation to name."""
        self.__name_expression__ = value

    def __repr__(self):
        return printers.__repr__(self)

    def _repr_markdown_(self):
        return printers._repr_markdown_(self)

    na = name
    nae = name_expression


class Unit(InstanceMixin):
    def __init__(
        self,
        name=configuration.undefined_unit_name,
        na=configuration.undefined_unit_name,
        name_expression=configuration.undefined_unit_name,
        symbol=configuration.undefined_unit_symbol,
        s=configuration.undefined_unit_symbol,
        symbolic_expression=sy.Symbol(configuration.undefined_unit_symbol),
    ):
        super(Unit, self).__init__()
        self.__name__ = helpers.__select_available_property__(name,
                                                              na,
                                                              [configuration.undefined_unit_name,
                                                               configuration.undefined_unit_symbol],
                                                              symbol,
                                                              s)
        self.__name_expression__ = helpers.__select_available_property__(name_expression,
                                                                         self.__name__,
                                                                         configuration.undefined_unit_name)
        self.__symbol__ = helpers.__select_available_property__(symbol,
                                                                s,
                                                                [configuration.undefined_unit_symbol,
                                                                 configuration.undefined_unit_name],
                                                                name)
        self.__symbolic_expression__ = helpers.__select_available_property__(symbolic_expression,
                                                                             self.__symbol__,
                                                                             configuration.undefined_unit_symbolic_expression)
        self.data

    def __truediv__(self, other):
        new = Unit()
        name_variables = helpers.name_variables_generator(self, other)
        new.name = "(" + name_variables[0] + ")_per_(" + name_variables[1] + ")"
        symbol_variables = helpers.symbolic_expression_variables_generator(self, other)
        new.symbolic_expression = symbol_variables[0] / symbol_variables[1]
        return new

    def __mul__(self, other):
        new = Unit()
        name_variables = helpers.name_variables_generator(self, other)
        new.name = "(" + name_variables[0] + "_times_" + name_variables[1] + ")"
        symbol_variables = helpers.symbolic_expression_variables_generator(self, other)
        new.symbolic_expression = symbol_variables[0] * symbol_variables[1]
        return new

    def __add__(self, other):
        new = Unit()
        name_variables = helpers.name_variables_generator(self, other)
        new.name = "(" + name_variables[0] + "_plus_" + name_variables[1] + ")"
        symbol_variables = helpers.symbolic_expression_variables_generator(self, other)
        new.symbolic_expression = symbol_variables[0] + symbol_variables[1]
        return new

    def __sub__(self, other):
        new = Unit()
        name_variables = helpers.name_variables_generator(self, other)
        new.name = "(" + name_variables[0] + "_minus_" + name_variables[1] + ")"
        symbol_variables = helpers.symbolic_expression_variables_generator(self, other)
        new.symbolic_expression = symbol_variables[0] - symbol_variables[1]
        return new

    def __pow__(self, other):
        new = Unit()
        name_variables = helpers.name_variables_generator(self, other)
        new.name = "(" + name_variables[0] + "_power_" + name_variables[1] + ")"
        symbol_variables = helpers.symbolic_expression_variables_generator(self, other)
        new.symbolic_expression = symbol_variables[0] ** symbol_variables[1]
        return new

    @property
    def symbol(self):
        """Return unit symbol shorthand from Sympy"""
        if bool(self.__symbol__):
            return sy.Symbol(self.__symbol__)
        else:
            raise ValueError("Sympy incompatible symbol input: self.symbol" + str(self.__symbol__) + "for class: " + str(self.__class__))

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


def unit_variable_generator(first, second):
    undefined_unit_default = Unit(name=configuration.undefined_unit_name,
                                  symbol=configuration.undefined_unit_symbol)
    if hasattr(first, "unit"):
        if first.unit == "":
            # TODO in case we want show other default
            first_unit_variable = first.unit
        else:
            first_unit_variable = first.unit
    else:
        first_unit_variable = undefined_unit_default
    if hasattr(second, "unit"):
        if second.unit == "":
            # TODO in case we want to show some other default
            second_unit_variable = second.unit
        else:
            second_unit_variable = second.unit
    else:
        second_unit_variable = undefined_unit_default
    return [first_unit_variable, second_unit_variable]


class Value(InstanceMixin):
    @property
    def __parent_class__(self):
        return "Value"

    def __init__(
        self,
        name=configuration.undefined_value_name,
        na=configuration.undefined_value_name,
        name_expression=configuration.undefined_value_name,
        numerical=configuration.undefined_value_numerical,
        symbol=configuration.undefined_unit_symbol,
        s=configuration.undefined_unit_symbol,
        symbolic_expression=configuration.undefined_value_symbolic_expression,
        se=configuration.undefined_value_symbolic_expression,
        unit=Unit(),
    ):
        super(Value, self).__init__()
        self.__name__ = helpers.__select_available_property__(name,
                                                              na,
                                                              configuration.undefined_value_name,
                                                              symbol,
                                                              s
                                                              )
        self.__name_expression__ = helpers.__select_available_property__(name_expression,
                                                                         self.__name__,
                                                                         configuration.undefined_value_name)
        self.__symbol__ = helpers.__select_available_property__(symbol,
                                                                s,
                                                                configuration.undefined_value_symbol)
        self.__symbolic_expression__ = helpers.__select_available_property__(symbolic_expression,
                                                                             se,
                                                                             configuration.undefined_value_symbolic_expression,
                                                                             )
        self.__numerical__ = numerical
        self.__unit__ = unit

    @property
    def __type__(self):
        return "Value"

    def __truediv__(self, other):
        new = Value()
        name_variables = helpers.name_variables_generator(self, other)
        new.name_expression = (
            "(" + name_variables[0] + ")_per_(" + name_variables[1] + ")"
        )
        symbol_variables = helpers.symbolic_expression_variables_generator(self, other)
        new.symbolic_expression = symbol_variables[0] / symbol_variables[1]
        numerical_variables = helpers.numerical_variables_generator(self, other)
        new.numerical = numerical_variables[0] / numerical_variables[1]
        unit_variables = unit_variable_generator(self, other)
        new.unit = unit_variables[0] / unit_variables[1]
        return new

    def __rtruediv__(self, other):
        new = Value()
        name_variables = helpers.name_variables_generator(other, self)
        new.name_expression = (
            "(" + name_variables[0] + ")_per_(" + name_variables[1] + ")"
        )
        symbol_variables = helpers.symbolic_expression_variables_generator(other, self)
        new.symbolic_expression = symbol_variables[0] / symbol_variables[1]
        numerical_variables = helpers.numerical_variables_generator(other, self)
        new.numerical = numerical_variables[0] / numerical_variables[1]
        unit_variables = unit_variable_generator(other, self)
        new.unit = unit_variables[0] / unit_variables[1]
        return new

    def __mul__(self, other):
        new = Value()
        name_variables = helpers.name_variables_generator(self, other)
        new.name_expression = (
            "(" + name_variables[0] + "_times_" + name_variables[1] + ")"
        )
        symbol_variables = helpers.symbolic_expression_variables_generator(self, other)
        new.symbolic_expression = symbol_variables[0] * symbol_variables[1]
        numerical_variables = helpers.numerical_variables_generator(self, other)
        new.numerical = numerical_variables[0] * numerical_variables[1]
        unit_variables = unit_variable_generator(self, other)
        new.unit = unit_variables[0] * unit_variables[1]
        return new

    def __rmul__(self, other):
        new = Value()
        name_variables = helpers.name_variables_generator(other, self)
        new.name_expression = (
            "(" + name_variables[0] + "_times_" + name_variables[1] + ")"
        )
        symbol_variables = helpers.symbolic_expression_variables_generator(other, self)
        new.symbolic_expression = symbol_variables[0] * symbol_variables[1]
        numerical_variables = helpers.numerical_variables_generator(other, self)
        new.numerical = numerical_variables[0] * numerical_variables[1]
        unit_variables = unit_variable_generator(other, self)
        new.unit = unit_variables[0] * unit_variables[1]
        return new

    def __add__(self, other):
        new = Value()
        name_variables = helpers.name_variables_generator(self, other)
        new.name_expression = (
            "(" + name_variables[0] + "_plus_" + name_variables[1] + ")"
        )
        symbol_variables = helpers.symbolic_expression_variables_generator(self, other)
        new.symbolic_expression = symbol_variables[0] + symbol_variables[1]
        numerical_variables = helpers.numerical_variables_generator(self, other)
        new.numerical = numerical_variables[0] + numerical_variables[1]
        unit_variables = unit_variable_generator(self, other)
        new.unit = unit_variables[0] + unit_variables[1]
        return new

    def __radd__(self, other):
        new = Value()
        name_variables = helpers.name_variables_generator(other, self)
        new.name_expression = (
            "(" + name_variables[0] + "_plus_" + name_variables[1] + ")"
        )
        symbol_variables = helpers.symbolic_expression_variables_generator(other, self)
        new.symbolic_expression = symbol_variables[0] + symbol_variables[1]
        numerical_variables = helpers.numerical_variables_generator(other, self)
        new.numerical = numerical_variables[0] + numerical_variables[1]
        unit_variables = unit_variable_generator(other, self)
        new.unit = unit_variables[0] + unit_variables[1]
        return new

    def __sub__(self, other):
        new = Value()
        name_variables = helpers.name_variables_generator(self, other)
        new.name_expression = (
            "(" + name_variables[0] + "_minus_" + name_variables[1] + ")"
        )
        symbol_variables = helpers.symbolic_expression_variables_generator(self, other)
        new.symbolic_expression = symbol_variables[0] - symbol_variables[1]
        numerical_variables = helpers.numerical_variables_generator(self, other)
        new.numerical = numerical_variables[0] - numerical_variables[1]
        unit_variables = unit_variable_generator(self, other)
        new.unit = unit_variables[0] - unit_variables[1]
        return new

    def __rsub__(self, other):
        new = Value()
        name_variables = helpers.name_variables_generator(other, self)
        new.name_expression = (
            "(" + name_variables[0] + "_minus_" + name_variables[1] + ")"
        )
        symbol_variables = helpers.symbolic_expression_variables_generator(other, self)
        new.symbolic_expression = symbol_variables[0] - symbol_variables[1]
        numerical_variables = helpers.numerical_variables_generator(other, self)
        new.numerical = numerical_variables[0] - numerical_variables[1]
        unit_variables = unit_variable_generator(other, self)
        new.unit = unit_variables[0] - unit_variables[1]
        return new

    def __pow__(self, other):
        new = Value()
        name_variables = helpers.name_variables_generator(self, other)
        new.name_expression = (
            "(" + name_variables[0] + "_power_" + name_variables[1] + ")"
        )
        symbol_variables = helpers.symbolic_expression_variables_generator(self, other)
        new.symbolic_expression = symbol_variables[0] ** symbol_variables[1]
        numerical_variables = helpers.numerical_variables_generator(self, other)
        new.numerical = numerical_variables[0] ** numerical_variables[1]
        unit_variables = unit_variable_generator(self, other)
        new.unit = unit_variables[0] ** unit_variables[1]
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
    def symbolic_expression(self):
        """Return symbolic expression consisting of an equivalent mathemtical representation to symbol"""
        return self.__symbolic_expression__

    @symbolic_expression.setter
    def symbolic_expression(self, value):
        """Set symbolic expression consisting of an equivalent mathemtical representation to symbol."""
        self.__symbolic_expression__ = value

    @property
    def unit(self):
        """Return unit symbol unit shorthand"""
        return self.__unit__

    @unit.setter
    def unit(self, value):
        self.__unit__ = value

    # Shorthands
    u = unit
    s = symbol
    n = numerical
    se = symbolic_expression


class Constant(Value):
    @Value.numerical.setter
    def numerical(self, value):
        print(
            Warning(
                "Constant cannot be mutated. You cannot set any attribute value. Instantiate a new variable."
            )
        )

    @Value.symbol.setter
    def symbol(self, value):
        print(
            Warning(
                "Constant cannot be mutated. You cannot set any attribute value. Instantiate a new variable."
            )
        )

    @Value.unit.setter
    def unit(self, value):
        print(
            Warning(
                "Constant cannot be mutated. You cannot set any attribute value. Instantiate a new variable."
            )
        )

    @Value.symbolic_expression.setter
    def symbolic_expression(self, value):
        """Set symbolic expression shorthand shorthand"""
        print(
            Warning(
                "Constant cannot be mutated. You cannot set any attribute value. Instantiate a new variable."
            )
        )

    # Shorthands
    u = unit
    s = symbol
    n = numerical
    se = symbolic_expression


class Variable(Value):
    pass
