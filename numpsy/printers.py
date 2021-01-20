import pandas as pd
import sympy as sy

def tabulate_instance(instance):
    output = pd.DataFrame({})
    if hasattr(instance, "name"):
        output["name"] = instance.name
    if hasattr(instance, "name_expression"):
        output["name_expression"] = instance.name_expression
    if hasattr(instance, "numerical"):
        output["numerical"] = instance.numerical
    if hasattr(instance, "symbol"):
        output["symbol"] = "$" + sy.latex(instance.symbol) + "$"
        output["symbol"]
    if hasattr(instance, "symbolic_expression"):
        output["symbolic_expression"] = "$" + sy.latex(instance.symbolic_expression) + "$"
    #if hasattr(instance, "unit"):
    #    output["unit"] = instance.unit
    return output


def __repr__(instance):
    """Main pretty printing instance representation method.

    The goal is that when it prints in IPython it shows its parameters as rows,
    kind of like Pandas tables, except that in this case we would have both
    symbol, symbolic_expression, numerical, unit and name as the default prints.
    Other special methods can print the full instance.

    Note that because Unit is a NumpSy class, we then need to make it embeddable into a
    Variable representation, and both representations should be adaptable. So this representation
    is hierarchical.

    It also aims to enhance the functionality available via the sympy printers
    """
    output = tabulate_instance(instance)
    return instance.__class__.__name__ + str(output)

def _repr_markdown_(instance):
    data = tabulate_instance(instance)
    return data.to_markdown()
