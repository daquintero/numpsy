import numpy as np
import sympy as sy
import scipy as sp
import scipy.special
from . import core
from . import helpers

def variable_compatibility_check(input):
    if hasattr(input, "__parent_class__"):
        if input.__parent_class__ == "Value":
            new = input.__class__()
        else:
            new = core.Variable()
    else:
        new = core.Variable()
    return new

def sqrt(instance=core.Variable()):
    new = variable_compatibility_check(instance)
    instance_parameters = helpers.full_variable_generator(instance)
    new.numerical = np.sqrt(instance_parameters["numerical"])
    new.symbolic_expression = sy.sqrt(instance_parameters["symbolic"])
    new.name_expression = "square_root(" + instance_parameters["name"] + ")"
    # TODO automate this
    new.unit.name = "square_root(" + instance_parameters["unit"].name + ")"
    # TODO get symbolic parameters
    new.unit.symbolic_expression = sy.sqrt(instance_parameters["unit"].symbolic_expression)
    return new

def sinh(instance=core.Variable()):
    new = variable_compatibility_check(instance)
    instance_parameters = helpers.full_variable_generator(instance)
    new.numerical = np.sinh(instance_parameters["numerical"])
    # TODO operate on both symbolic variables
    new.symbolic_expression = sy.sinh(instance_parameters["symbolic"])
    new.name_expression = "sinh(" + instance_parameters["name"] + ")"
    return new

#def ellipk(instance=core.Variable()):
#    sp.special.ellipk(m)


# if __name__ == "__main__":
#     sinh()
