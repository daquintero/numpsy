import numpy as np
import sympy as sy
import sympy.functions.special.elliptic_integrals
import scipy as sp
import scipy.special
from . import core
from . import helpers


def __variable_compatibility_check__(input):
    if hasattr(input, "__parent_class__"):
        if input.__parent_class__ == "Value":
            new = input.__class__()
        else:
            new = core.Variable()
    else:
        new = core.Variable()
    return new


def complete_elliptical_integral_first_kind(instance=core.Variable()):
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


def sqrt(instance=core.Variable()):
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


def sinh(instance=core.Variable()):
    new = __variable_compatibility_check__(instance)
    instance_parameters = helpers.full_variable_generator(instance)
    new.numerical = np.sinh(instance_parameters["numerical"])
    # TODO operate on both symbolic variables
    new.symbolic_expression = sy.sinh(instance_parameters["symbolic"])
    new.name_expression = "sinh(" + instance_parameters["name"] + ")"
    return new

def exp(instance=core.Variable()):
    new = __variable_compatibility_check__(instance)
    instance_parameters = helpers.full_variable_generator(instance)
    new.numerical = np.exp(instance_parameters["numerical"])
    # TODO operate on both symbolic variables
    new.symbolic_expression = sy.exp(instance_parameters["symbolic"])
    new.name_expression = "exp(" + instance_parameters["name"] + ")"
    return new


def log(instance=core.Variable()):
    new = __variable_compatibility_check__(instance)
    instance_parameters = helpers.full_variable_generator(instance)
    new.numerical = np.log(instance_parameters["numerical"])
    # TODO operate on both symbolic variables
    new.symbolic_expression = sy.log(instance_parameters["symbolic"])
    new.name_expression = "exp(" + instance_parameters["name"] + ")"
    return new

def log10(instance=core.Variable()):
    new = __variable_compatibility_check__(instance)
    instance_parameters = helpers.full_variable_generator(instance)
    new.numerical = np.log10(instance_parameters["numerical"])
    # TODO operate on both symbolic variables
    new.symbolic_expression = sy.log(instance_parameters["symbolic"], 10)
    new.name_expression = "exp(" + instance_parameters["name"] + ")"
    return new


e = exp


# def ellipk(instance=core.Variable()):
#    sp.special.ellipk(m)


# if __name__ == "__main__":
#     sinh()
