import numpy as np
import sympy as sy
from . import core
from . import helpers


def sinh(instance=core.Variable()):
    if hasattr(instance, "__parent_class__"):
        if instance.__parent_class__ == "Value":
            new = instance.__class__()
        else:
            new = core.Variable()
    else:
        new = core.Variable()
    print(instance)
    instance_parameters = helpers.full_variable_generator(instance)
    print(instance_parameters)
    new.numerical = np.sinh(instance_parameters["numerical"])
    new.symbolic_expression = sy.sinh(instance_parameters["symbolic"])
    new.name_expression = instance_parameters["name"]
    return new


# if __name__ == "__main__":
#     sinh()
