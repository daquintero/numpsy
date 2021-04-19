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
    first_str = str(first)
    second_str = str(second)
    if isinstance(default, list):
        default_i_str = str(default[0])
        default_i = default[0]
    else:
        default_i_str = str(default)
        default_i = default

    if (first_str != default_i_str) and (second_str == default_i_str) and bool(first_str):
        return first
    elif (first_str == default_i_str) and (second_str != default_i_str) and bool(second_str):
        return second
    elif (first_str == second_str) and (first_str != default_i_str) and (second_str != default_i_str) and bool(first_str):
        return first
    elif (first_str == default_i_str) and (second_str == default_i_str):
        try:
            if bool(kwargs):
                for kwarg in kwargs:
                    if isinstance(default, list):
                        if bool(kwarg) and all((kwarg != str(default_j)) for default_j in default):
                            return kwarg
                    else:
                        if (kwarg != default_i_str):
                            return kwarg
                return default_i
            else:
                return default_i
        except:
            return default_i
    elif (first_str != second_str) and (first_str != default_i_str) and (second_str != default_i_str):
        raise ValueError("Incongruent properties assignments, first: " + str(first) + ", second_str: " + str(second) + " default: " + str(default_i))
    else:
        print(Warning("Incompatible property assignment, first: " + str(first) + ", second_str: " + str(
            second) + ", assigning default: " + str(default_i)))
        return default_i

def __validate_numeric__(input):
    # TODO implement
    return input

def __unit_variable_generator__(instance):
    if hasattr(instance, "unit"):
        if instance.unit == "":
            # TODO in case we want show other default
            instance_unit_variable = instance.unit
        else:
            instance_unit_variable = instance.unit
    else:
        instance_unit_variable = core.undefined_unit_default
    return instance_unit_variable

def __unit_variables_generator__(first, second):
    first_unit_variable = __unit_variable_generator__(first)
    second_unit_variable = __unit_variable_generator__(second)
    return [first_unit_variable, second_unit_variable]


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
            if hasattr(instance, "symbolic_expression"):
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
