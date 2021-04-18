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
    if hasattr(instance, "print_style") and bool(instance.print_style):
        if instance.print_style == configuration.available_print_styles["full"]:
            if instance.__class__.__name__ == "Unit":
                display_columns = ["name", "symbol", "symbolic_expression"]
            else:
                display_columns = ["name", "symbol", "symbolic_expression", "numerical", "unit"]
            markdown_instance = copy.deepcopy(instance)
            return markdown_instance.data.loc[:, display_columns].T.to_markdown()

        if instance.print_style == configuration.available_print_styles["numpy"]:
            if instance.__class__.__name__ == "Unit":
                display_columns = ["symbolic_expression"]
                markdown_instance = copy.deepcopy(instance)
                return markdown_instance.data.loc[:, display_columns].T.to_markdown()
            else:
                return instance.numerical

        if instance.print_style == configuration.available_print_styles["sympy"]:
            if instance.__class__.__name__ == "Unit":
                display_columns = ["symbol", "symbolic_expression"]
            else:
                display_columns = ["symbol", "symbolic_expression"]
            markdown_instance = copy.deepcopy(instance)
            return markdown_instance.data.loc[:, display_columns].T.to_markdown()
    else:
        if configuration.setup.print_style == configuration.available_print_styles["full"]:
            if instance.__class__.__name__ == "Unit":
                display_columns = ["name", "symbol", "symbolic_expression"]
            else:
                display_columns = ["name", "symbol", "symbolic_expression", "numerical", "unit"]
            markdown_instance = copy.deepcopy(instance)
            return markdown_instance.data.loc[:, display_columns].T.to_markdown()

        if configuration.setup.print_style == configuration.available_print_styles["numpy"]:
            if instance.__class__.__name__ == "Unit":
                display_columns = ["symbolic_expression"]
                markdown_instance = copy.deepcopy(instance)
                return markdown_instance.data.loc[:, display_columns].T.to_markdown()
            else:
                return instance.numerical


        if configuration.setup.print_style == configuration.available_print_styles["sympy"]:
            if instance.__class__.__name__ == "Unit":
                display_columns = ["symbol", "symbolic_expression"]
            else:
                display_columns = ["symbol", "symbolic_expression"]
            markdown_instance = copy.deepcopy(instance)
            return markdown_instance.data.loc[:, display_columns].T.to_markdown()



def _repr_markdown_(display_dataframe):
    return markdownify(display_dataframe)
