import numpy as np
import sympy as sy

undefined_unit_name = "undefined"
undefined_unit_symbol = "Ø"
undefined_unit_symbolic_expression = sy.Symbol(undefined_unit_symbol)

undefined_value_name = "undefined"
undefined_value_symbol = "Ø"
undefined_value_symbolic_expression = sy.Symbol(undefined_value_symbol)

undefined_value_numerical = np.array([])



available_calculation_styles = {
    "numpsy": "numpsy",
    "numpy": "numpy",
    "sympy": "sympy"
}
undefined_calculation_style = None
default_calculation_style = available_calculation_styles["numpsy"]

available_print_styles = {
    "numpsy": "numpsy",
    "numpy": "numpy",
    "sympy": "sympy"
}
undefined_print_style = None
default_print_style = available_print_styles["numpsy"]


class ConfigurationSetup:

    def __init__(self,
                 calculation_style=default_calculation_style,
                 print_style=default_print_style
                 ):
        self.__print_style__ = print_style
        self.__calculation_style__ = calculation_style

    @property
    def calculation_style(self):
        return self.__calculation_style__

    @calculation_style.setter
    def calculation_style(self, value):
        self.__calculation_style__ = value

    @property
    def print_style(self):
        """Return name string"""
        return self.__print_style__

    @print_style.setter
    def print_style(self, value):
        self.__print_style__ = value

setup = ConfigurationSetup()
