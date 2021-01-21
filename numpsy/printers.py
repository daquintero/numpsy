import pandas as pd
import sympy as sy
import copy
from . import configuration


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
    output = instance.data
    return instance.__class__.__name__ + str(output)

def markdownify(instance):
    if instance.__class__.__name__ == "Unit":
        display_columns = ["name", "symbol", "symbolic_expression"]
    else:
        display_columns = ["name", "symbol", "symbolic_expression", "numerical", "unit"]
    markdown_instance = copy.deepcopy(instance)
    return markdown_instance.data.loc[:, display_columns]

def _repr_markdown_(display_dataframe):
      return markdownify(display_dataframe).T.to_markdown()
