import sympy as sy
from . import configuration
from . import core


def __check_properties__(instance, property):
    if hasattr(instance.properties, property):
        out = instance.properties[property]
    else:
        out = None


def __select_available_property__(first, second, default, *kwargs):
    # TODO check this fix might be a bit dodgy for sympy comparisons.
    first = str(first)
    second = str(second)
    default = str(default)

    if (first != default) and (second == default) and bool(first):
        return first
    elif (first == default) and (second != default) and bool(second):
        return second
    elif (first == second) and (first != default) and (second != default) and bool(first):
        return first
    elif (first == default) and (second == default):
        try:
            if bool(kwargs):
                for kwarg in kwargs:
                    if bool(kwarg) and (kwarg != default):
                        return kwarg
                return default
            else:
                return default
        except:
            return default
    elif (first != second) and (first != default) and (second != default):
        raise ValueError("Incongruent properties assignments, first: " + str(first) + ", second: " + str(second) + " default: " + str(default))
    else:
        print(Warning("Incompatible property assignment, first: " + str(first) + ", second: " + str(
            second) + ", assigning default: " + str(default)))
        return default


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
            instance_symbolic_variable = instance.symbolic_expression
        else:
            instance_symbolic_variable = instance.symbol
    elif str(instance).isnumeric():
        return instance
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
