import numpy as np
import sympy as sy

undefined_note = ""

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

available_matrix_operation_mode = {
    "vectorial": "vectorial",
}
default_matrix_operation_mode = available_matrix_operation_mode["vectorial"]

available_print_styles = {
    "numpsy": "numpsy",
    "numpy": "numpy",
    "sympy": "sympy"
}
undefined_print_style = None
default_print_style = available_print_styles["numpsy"]
default_debug_mode = False

default_numpsy_value_printer_columns = ["name", "symbol", "symbolic_expression", "numerical", "unit", "note"]

class ConfigurationSetup:

    def __init__(self,
                 calculation_style=default_calculation_style,
                 debug_mode=default_debug_mode,
                 matrix_operation_mode=default_matrix_operation_mode,
                 print_style=default_print_style,
                 value_printer_columns=default_numpsy_value_printer_columns
                 ):
        self.__calculation_style__ = calculation_style
        self.__debug_mode__ = debug_mode
        self.__matrix_operation_mode__ = matrix_operation_mode
        self.__print_style__ = print_style
        self.__value_printer_columns__ = value_printer_columns

    @property
    def debug_mode(self):
        """Return name string"""
        return self.__debug_mode__

    @debug_mode.setter
    def debug_mode(self, value):
        self.__debug_mode__ = value

    @property
    def calculation_style(self):
        """
        Part of the complexity is that there are some circumstances where for a local operation, a calculation_style may be desired, but not necessarily for a global case.
        """
        return self.__calculation_style__

    @calculation_style.setter
    def calculation_style(self, value):
        self.__calculation_style__ = value

    @property
    def matrix_operation_mode(self):
        return self.__matrix_operation_mode__

    @matrix_operation_mode.setter
    def matrix_operation_mode(self, value):
        self.__matrix_operation_mode__ = value

    @property
    def print_style(self):
        """Return name string"""
        return self.__print_style__

    @print_style.setter
    def print_style(self, value):
        self.__print_style__ = value

    @property
    def value_printer_columns(self):
        """Return name string"""
        return self.__value_printer_columns__

    @value_printer_columns.setter
    def value_printer_columns(self, value):
        self.__value_printer_columns__ = value

setup = ConfigurationSetup()
