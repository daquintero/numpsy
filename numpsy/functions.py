import numpy as np
import sympy as sy
import sympy.functions.special.elliptic_integrals
import scipy as sp
import scipy.special
from . import configuration
from . import core
from . import helpers


def __variable_compatibility_check__(input):
    """
    Args:
        input:

    Returns:

    """
    if hasattr(input, "__parent_class__"):
        if input.__parent_class__ == "Value":
            new = input.__class__()
        else:
            new = core.Variable()
    else:
        new = core.Variable()
    return new

def abs(instance=core.Variable()):
    """
    Args:
        instance:

    Returns:

    """
    if configuration.setup.calculation_style == "numpsy":
        new = __variable_compatibility_check__(instance)
        instance_parameters = helpers.full_variable_generator(instance)
        new.numerical = np.abs(instance_parameters["numerical"])
        # TODO operate on both symbolic variables
        new.symbolic_expression = sy.Abs(instance_parameters["symbolic"])
        new.name_expression = "abs(" + instance_parameters["name"] + ")"
        return new
    if configuration.setup.calculation_style == "numpy":
        new = __variable_compatibility_check__(instance)
        instance_parameters = helpers.full_variable_generator(instance)
        new.numerical = np.abs(instance_parameters["numerical"])
        # TODO operate on both symbolic variables
        # new.symbolic_expression = sy.Abs(instance_parameters["symbolic"])
        # new.name_expression = "abs(" + instance_parameters["name"] + ")"
        return new

def binomial_coefficient(instance=core.Variable(), instance_2=core.Variable()):
    """
    Args:
        instance:
        instance_2:

    Returns:

    """
    if configuration.setup.calculation_style == "numpsy":
        new = __variable_compatibility_check__(instance)
        new_2 = __variable_compatibility_check__(instance_2)
        instance_parameters = helpers.full_variable_generator(instance)
        instance_parameters_2 = helpers.full_variable_generator(instance_2)
        new.numerical = sp.special.binom(instance_parameters["numerical"], instance_parameters_2["numerical"])
        # TODO operate on both symbolic variables
        new.symbolic_expression = sy.binomial(instance_parameters["symbolic"], instance_parameters_2["symbolic"])
        new.name_expression = "binomial(" + instance_parameters["name"] + "," + instance_parameters_2["name"] + ")"
        return new
    if configuration.setup.calculation_style == "numpy":
        new = __variable_compatibility_check__(instance)
        new_2 = __variable_compatibility_check__(instance_2)
        instance_parameters = helpers.full_variable_generator(instance)
        instance_parameters_2 = helpers.full_variable_generator(instance_2)
        new.numerical = sp.special.binom(instance_parameters["numerical"], instance_parameters_2["numerical"])
        # TODO operate on both symbolic variables
        # new.symbolic_expression = sy.binomial(instance_parameters["symbolic"], instance_parameters_2["symbolic"])
        # new.name_expression = "binomial(" + instance_parameters["name"] + "," + instance_parameters_2["name"] + ")"
        return new

def ciel(instance=core.Variable()):
    """
    Args:
        instance:

    Returns:

    """
    if configuration.setup.calculation_style == "numpsy":
        new = __variable_compatibility_check__(instance)
        instance_parameters = helpers.full_variable_generator(instance)
        new.numerical = np.ceil(instance_parameters["numerical"])
        # TODO operate on both symbolic variables
        new.symbolic_expression = sy.ceiling(instance_parameters["symbolic"])
        new.name_expression = "ceil(" + instance_parameters["name"] + ")"
        return new
    if configuration.setup.calculation_style == "numpy":
        new = __variable_compatibility_check__(instance)
        instance_parameters = helpers.full_variable_generator(instance)
        new.numerical = np.ceil(instance_parameters["numerical"])
        # TODO operate on both symbolic variables
        # new.symbolic_expression = sy.ceiling(instance_parameters["symbolic"])
        # new.name_expression = "ceil(" + instance_parameters["name"] + ")"
        return new

def complete_elliptical_integral_first_kind(instance=core.Variable()):
    if configuration.setup.calculation_style == "numpsy":
        new = __variable_compatibility_check__(instance)
        instance_parameters = helpers.full_variable_generator(instance)
        new.numerical = sp.special.ellipk(instance_parameters["numerical"])
        new.symbolic_expression = sy.functions.special.elliptic_integrals.elliptic_k(
            instance_parameters["symbolic"]
        )
        new.name_expression = (
            "complete_elliptical_integral_first_kind(" + instance_parameters["name"] + ")"
        )
        # TODO automate this
        new.unit.name = "K(" + instance_parameters["unit"].name + ")"
        # TODO get symbolic parameters
        new.unit.symbolic_expression = sy.functions.special.elliptic_integrals.elliptic_k(
            instance_parameters["unit"].symbolic_expression
        )
        return new
    if configuration.setup.calculation_style == "numpy":
        new = __variable_compatibility_check__(instance)
        instance_parameters = helpers.full_variable_generator(instance)
        new.numerical = sp.special.ellipk(instance_parameters["numerical"])
        # new.symbolic_expression = sy.functions.special.elliptic_integrals.elliptic_k(
        #     instance_parameters["symbolic"]
        # )
        # new.name_expression = (
        #         "complete_elliptical_integral_first_kind(" + instance_parameters["name"] + ")"
        # )
        # # TODO automate this
        # new.unit.name = "K(" + instance_parameters["unit"].name + ")"
        # # TODO get symbolic parameters
        # new.unit.symbolic_expression = sy.functions.special.elliptic_integrals.elliptic_k(
        #     instance_parameters["unit"].symbolic_expression
        # )
        return new

def exp(instance=core.Variable()):
    if configuration.setup.calculation_style == "numpsy":
        new = __variable_compatibility_check__(instance)
        instance_parameters = helpers.full_variable_generator(instance)
        new.numerical = np.exp(instance_parameters["numerical"])
        # TODO operate on both symbolic variables
        new.symbolic_expression = sy.exp(instance_parameters["symbolic"])
        new.name_expression = "exp(" + instance_parameters["name"] + ")"
        return new
    if configuration.setup.calculation_style == "numpy":
        new = __variable_compatibility_check__(instance)
        instance_parameters = helpers.full_variable_generator(instance)
        new.numerical = np.exp(instance_parameters["numerical"])
        # TODO operate on both symbolic variables
        # new.symbolic_expression = sy.exp(instance_parameters["symbolic"])
        # new.name_expression = "exp(" + instance_parameters["name"] + ")"
        return new


def log(instance=core.Variable()):
    if configuration.setup.calculation_style == "numpsy":
        new = __variable_compatibility_check__(instance)
        instance_parameters = helpers.full_variable_generator(instance)
        new.numerical = np.log(instance_parameters["numerical"])
        # TODO operate on both symbolic variables
        new.symbolic_expression = sy.log(instance_parameters["symbolic"])
        new.name_expression = "ln(" + instance_parameters["name"] + ")"
        return new
    if configuration.setup.calculation_style == "numpy":
        new = __variable_compatibility_check__(instance)
        instance_parameters = helpers.full_variable_generator(instance)
        new.numerical = np.log(instance_parameters["numerical"])
        # # TODO operate on both symbolic variables
        # new.symbolic_expression = sy.log(instance_parameters["symbolic"])
        # new.name_expression = "ln(" + instance_parameters["name"] + ")"
        return new

def log2(instance=core.Variable()):
    if configuration.setup.calculation_style == "numpsy":
        new = __variable_compatibility_check__(instance)
        instance_parameters = helpers.full_variable_generator(instance)
        new.numerical = np.log2(instance_parameters["numerical"])
        # TODO operate on both symbolic variables
        new.symbolic_expression = sy.log(instance_parameters["symbolic"], 2)
        new.name_expression = "log2(" + instance_parameters["name"] + ")"
        return new
    if configuration.setup.calculation_style == "numpy":
        new = __variable_compatibility_check__(instance)
        instance_parameters = helpers.full_variable_generator(instance)
        new.numerical = np.log2(instance_parameters["numerical"])
        # TODO operate on both symbolic variables
        # new.symbolic_expression = sy.log(instance_parameters["symbolic"], 2)
        # new.name_expression = "log2(" + instance_parameters["name"] + ")"
        return new

def log10(instance=core.Variable()):
    if configuration.setup.calculation_style == "numpsy":
        new = __variable_compatibility_check__(instance)
        instance_parameters = helpers.full_variable_generator(instance)
        new.numerical = np.log10(instance_parameters["numerical"])
        # TODO operate on both symbolic variables
        new.symbolic_expression = sy.log(instance_parameters["symbolic"], 10)
        new.name_expression = "exp(" + instance_parameters["name"] + ")"
        return new
    if configuration.setup.calculation_style == "numpy":
        new = __variable_compatibility_check__(instance)
        instance_parameters = helpers.full_variable_generator(instance)
        new.numerical = np.log10(instance_parameters["numerical"])
        # TODO operate on both symbolic variables
        # new.symbolic_expression = sy.log(instance_parameters["symbolic"], 10)
        # new.name_expression = "exp(" + instance_parameters["name"] + ")"
        return new

def prod(instance=core.Variable(),
         sum_variable_string="i",
         minimum_range_amount=0,
         maximum_range_amount=None
         ):
    if configuration.setup.calculation_style == "numpsy":
        new = __variable_compatibility_check__(instance)
        instance_parameters = helpers.full_variable_generator(instance)
        new.numerical = np.prod(instance_parameters["numerical"])
        # TODO operate on both symbolic variables
        new.symbolic_expression = sy.Product(instance_parameters["symbolic"], (sy.Symbol(sum_variable_string),
                                                                               minimum_range_amount,
                                                                               maximum_range_amount))
        new.name_expression = "prod(" + instance_parameters["name"] + ")"
        return new
    if configuration.setup.calculation_style == "numpy":
        new = __variable_compatibility_check__(instance)
        instance_parameters = helpers.full_variable_generator(instance)
        new.numerical = np.prod(instance_parameters["numerical"])
        # TODO operate on both symbolic variables
        # new.symbolic_expression = sy.Product(instance_parameters["symbolic"], (sy.Symbol(sum_variable_string),
        #                                                                        minimum_range_amount,
        #                                                                        maximum_range_amount))
        # new.name_expression = "prod(" + instance_parameters["name"] + ")"
        return new

def repeat(instance=core.Variable(), repeats=1):
    if configuration.setup.calculation_style == "numpsy":
        # TODO unconvinced about the symbolic implementation of this.
        new = __variable_compatibility_check__(instance)
        instance_parameters = helpers.full_variable_generator(instance)
        # print(instance_parameters["numerical"])
        new.numerical = np.repeat(instance_parameters["numerical"], repeats)
        # TODO operate on both symbolic variables
        new.symbolic_expression = instance_parameters["symbolic"]
        new.name_expression = "repeat(" + instance_parameters["name"] + ")"
        return new
    if configuration.setup.calculation_style == "numpy":
        # TODO unconvinced about the symbolic implementation of this.
        new = __variable_compatibility_check__(instance)
        instance_parameters = helpers.full_variable_generator(instance)
        # print(instance_parameters["numerical"])
        new.numerical = np.repeat(instance_parameters["numerical"], repeats)
        # # TODO operate on both symbolic variables
        # new.symbolic_expression = instance_parameters["symbolic"]
        # new.name_expression = "repeat(" + instance_parameters["name"] + ")"
        return new

def sqrt(instance=core.Variable()):
    if configuration.setup.calculation_style == "numpsy":
        new = __variable_compatibility_check__(instance)
        instance_parameters = helpers.full_variable_generator(instance)
        new.numerical = np.sqrt(instance_parameters["numerical"])
        new.symbolic_expression = sy.sqrt(instance_parameters["symbolic"])
        new.name_expression = "square_root(" + instance_parameters["name"] + ")"
        # TODO automate this
        new.unit.name = "square_root(" + instance_parameters["unit"].name + ")"
        # TODO get symbolic parameters
        new.unit.symbolic_expression = sy.sqrt(
            instance_parameters["unit"].symbolic_expression
        )
        return new
    if configuration.setup.calculation_style == "numpy":
        new = __variable_compatibility_check__(instance)
        instance_parameters = helpers.full_variable_generator(instance)
        new.numerical = np.sqrt(instance_parameters["numerical"])
        # new.symbolic_expression = sy.sqrt(instance_parameters["symbolic"])
        # new.name_expression = "square_root(" + instance_parameters["name"] + ")"
        # # TODO automate this
        # new.unit.name = "square_root(" + instance_parameters["unit"].name + ")"
        # # TODO get symbolic parameters
        # new.unit.symbolic_expression = sy.sqrt(
        #     instance_parameters["unit"].symbolic_expression
        # )
        return new

def sinh(instance=core.Variable()):
    if configuration.setup.calculation_style == "numpsy":
        new = __variable_compatibility_check__(instance)
        instance_parameters = helpers.full_variable_generator(instance)
        new.numerical = np.sinh(instance_parameters["numerical"])
        # TODO operate on both symbolic variables
        new.symbolic_expression = sy.sinh(instance_parameters["symbolic"])
        new.name_expression = "sinh(" + instance_parameters["name"] + ")"
        return new
    if configuration.setup.calculation_style == "numpsy":
        new = __variable_compatibility_check__(instance)
        instance_parameters = helpers.full_variable_generator(instance)
        new.numerical = np.sinh(instance_parameters["numerical"])
        # # TODO operate on both symbolic variables
        # new.symbolic_expression = sy.sinh(instance_parameters["symbolic"])
        # new.name_expression = "sinh(" + instance_parameters["name"] + ")"
        return new

def sum(instance=core.Variable(),
        sum_variable_string="i",
        minimum_range_amount=0,
        maximum_range_amount=0,
        axis=0):
    if configuration.setup.calculation_style == "numpsy":
        new = __variable_compatibility_check__(instance)
        instance_parameters = helpers.full_variable_generator(instance)
        new.numerical = np.sum(instance_parameters["numerical"], axis=axis)
        # TODO operate on both symbolic variables
        new.symbolic_expression = sy.Sum(instance_parameters["symbolic"], (sy.Symbol(sum_variable_string),
                                                                           minimum_range_amount,
                                                                           maximum_range_amount))
        new.name_expression = "sum(" + instance_parameters["name"] + ")"
        return new
    if configuration.setup.calculation_style == "numpy":
        new = __variable_compatibility_check__(instance)
        instance_parameters = helpers.full_variable_generator(instance)
        new.numerical = np.sum(instance_parameters["numerical"], axis=axis)
        # TODO operate on both symbolic variables
        # new.symbolic_expression = sy.Sum(instance_parameters["symbolic"], (sy.Symbol(sum_variable_string),
        #                                                                    minimum_range_amount,
        #                                                                    maximum_range_amount))
        # new.name_expression = "sum(" + instance_parameters["name"] + ")"
        return new

def tanh(instance=core.Variable()):
    if configuration.setup.calculation_style == "numpsy":
        new = __variable_compatibility_check__(instance)
        instance_parameters = helpers.full_variable_generator(instance)
        new.numerical = np.tanh(instance_parameters["numerical"])
        # TODO operate on both symbolic variables
        new.symbolic_expression = sy.tanh(instance_parameters["symbolic"])
        new.name_expression = "tanh(" + instance_parameters["name"] + ")"
        return new
    if configuration.setup.calculation_style == "numpy":
        new = __variable_compatibility_check__(instance)
        instance_parameters = helpers.full_variable_generator(instance)
        new.numerical = np.tanh(instance_parameters["numerical"])
        # TODO operate on both symbolic variables
        # new.symbolic_expression = sy.tanh(instance_parameters["symbolic"])
        # new.name_expression = "tanh(" + instance_parameters["name"] + ")"
        return new



e = exp
