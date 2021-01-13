import sympy as sy
from . import configuration
from . import core


def __check_properties__(instance, property):
    if hasattr(instance.properties, property):
        out = instance.properties[property]
    else:
        out = None


def __numpsy_repr__(instance):
    string_list = list([])
    class_name = instance.__class__.__name__
    string_list += ["<"]
    string_list += [class_name]
    if hasattr(instance, "name"):
        string_list += [' name:"']
        string_list += [str(instance.name)]
        string_list += ['"']
    if hasattr(instance, "name_expression"):
        string_list += [' name_expression:"']
        string_list += [str(instance.name_expression)]
        string_list += ['"']
    if hasattr(instance, "symbol"):
        string_list += [' symbol:"']
        string_list += [str(instance.symbol)]
        string_list += ['"']
    if hasattr(instance, "symbolic_expression"):
        string_list += [' symbolic_expression:"']
        string_list += [str(instance.symbolic_expression)]
        string_list += ['"']
    if hasattr(instance, "numerical"):
        string_list += [' numerical:"']
        string_list += [str(instance.numerical)]
        string_list += ['"']
    if hasattr(instance, "unit"):
        string_list += [' unit:"']
        string_list += [str(instance.unit)]
        string_list += ['"']
    string_list += [">"]
    return "".join(string_list)


def __numpsy_str__(instance):
    string_list = list([])
    class_name = instance.__class__.__name__
    string_list += ["<"]
    string_list += [class_name]
    if class_name == "Unit":
        delimeter = "\n\t\t"
    else:
        delimeter = "\n\t"
    if hasattr(instance, "name"):
        string_list += [delimeter + 'name:"']
        string_list += [str(instance.name)]
        string_list += ['"']
    if hasattr(instance, "symbol"):
        string_list += [delimeter + 'symbol:"']
        string_list += [str(instance.symbol)]
        string_list += ['"']
    if hasattr(instance, "symbolic_expression"):
        string_list += [delimeter + 'symbolic_expression:"']
        string_list += [str(instance.symbolic_expression)]
        string_list += ['"']
    if hasattr(instance, "numerical"):
        string_list += [delimeter + 'numerical:"']
        string_list += [str(instance.numerical)]
        string_list += ['"']
    if hasattr(instance, "unit"):
        string_list += [delimeter + 'unit:"']
        string_list += [str(instance.unit)]
        string_list += ['"']
    string_list += [delimeter + ">"]
    return "".join(string_list)


def name_variable_generator(instance):
    if hasattr(instance, "name") and (instance.name != ""):
        instance_name_variable = instance.name
    else:
        if hasattr(instance, "name_expression"):
            instance_name_variable = instance.name_expression
        else:
            instance_name_variable = str(instance)
    return instance_name_variable


def name_variables_generator(first, second):
    first_name_variable = name_variable_generator(first)
    second_name_variable = name_variable_generator(second)
    return [first_name_variable, second_name_variable]


def numerical_variable_generator(instance):
    if hasattr(instance, "numerical"):
        instance_numerical = instance.numerical
    else:
        instance_numerical = instance
    return instance_numerical


def numerical_variables_generator(first, second):
    first_numerical = numerical_variable_generator(first)
    second_numerical = numerical_variable_generator(second)
    return [first_numerical, second_numerical]


def symbolic_expression_variable_generator(instance):
    if hasattr(instance, "symbol"):
        if instance.__symbol__ == configuration.undefined_unit_symbol:
            if instance.symbolic_expression == sy.Symbol(""):
                instance_symbolic_variable = instance.symbolic_expression
            else:
                instance_symbolic_variable = instance.symbolic_expression
        else:
            instance_symbolic_variable = instance.symbol
    else:
        instance_symbolic_variable = sy.Symbol(configuration.undefined_unit_symbol)
    return instance_symbolic_variable


def symbolic_expression_variables_generator(first, second):
    first_symbolic_variable = symbolic_expression_variable_generator(first)
    second_symbolic_variable = symbolic_expression_variable_generator(second)
    return [first_symbolic_variable, second_symbolic_variable]


def unit_variable_generator(instance):
    if hasattr(instance, "unit"):
        return instance.unit
    else:
        return core.Unit()


def full_variable_generator(instance):
    name_variable = name_variable_generator(instance)
    symbolic_variable = symbolic_expression_variable_generator(instance)
    numerical_variable = numerical_variable_generator(instance)
    unit_variable = unit_variable_generator(instance)
    return {
        "name": name_variable,
        "symbolic": symbolic_variable,
        "numerical": numerical_variable,
        "unit": unit_variable,
    }
