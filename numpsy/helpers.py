import numpy as np
import sympy as sy
from . import configuration
from . import core


def __check_properties__(instance, property):
    if hasattr(instance.properties, property):
        out = instance.properties[property]
    else:
        out = None


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
        if not isinstance(instance.name, str):
            instance_name_variable = str(instance.name)
        else:
            instance_name_variable = instance.name
    else:
        if hasattr(instance, "name_expression"):
            if not isinstance(instance.name_expression, str):
                instance_name_variable = str(instance.name_expression)
            else:
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
    if hasattr(instance, "__symbol__"):
        if instance.__symbol__ == configuration.undefined_unit_symbol:
            if hasattr(instance, "symbolic_expression"):
                if instance.__symbolic_expression__ == configuration.undefined_value_symbolic_expression:
                    if hasattr(instance, "numerical"):
                        instance_symbolic_variable = instance.numerical
                    else:
                        instance_symbolic_variable = sy.Symbol(configuration.undefined_unit_symbol)
                else:
                    instance_symbolic_variable = instance.symbolic_expression
            elif hasattr(instance, "numerical"):
                instance_symbolic_variable = instance.numerical
            else:
                instance_symbolic_variable = sy.Symbol(configuration.undefined_unit_symbol)
        else:
            instance_symbolic_variable = instance.symbol
    # TODO Should this handle numpy arrays?
    elif np.isscalar(instance):
        instance_symbolic_variable = instance
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


def __select_available_property__(first, second, default, *kwargs):
    # TODO how robust is this fix?
    if type(first) == core.Unit:
        first_str = str(symbolic_expression_variable_generator(first))
    else:
        first_str = str(first)

    if type(second) == core.Unit:
        second_str = str(symbolic_expression_variable_generator(second))
    else:
        second_str = str(second)

    if isinstance(default, list):
        default_i_str = str(default[0])
        default_i = default[0]
    else:
        if type(default) == core.Unit:
            default_i_str = str(symbolic_expression_variable_generator(default))
            default_i = default
        else:
            default_i_str = str(default)
            default_i = default

    if (first_str != default_i_str) and (second_str == default_i_str) and bool(first_str):
        return first
    elif (first_str == default_i_str) and (second_str != default_i_str) and bool(second_str):
        return second
    elif (first_str == second_str) and (first_str != default_i_str) and (second_str != default_i_str) and bool(
            first_str):
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
        # TODO Workaround of undiagnosed problem where default_i_str gets a strange default.
        if (first_str != None):
            if configuration.setup.debug_mode == True:
                print(ValueError("Incongruent properties assignments, assigned first: "
                                 + str(first_str)
                                 + ", when second_str: "
                                 + str(second_str) + " and default: " + str(default_i_str)))
            return first
        else:
            if configuration.setup.debug_mode == True:
                raise ValueError("Incongruent properties assignments, first: "
                                     + str(first_str)
                                     + ", second_str: "
                                     + str(second_str) + " default: " + str(default_i_str))
    else:
        if configuration.setup.debug_mode == True:
            print(Warning("Incompatible property assignment, first: " + str(first) + ", second_str: " + str(
                second) + ", assigning default: " + str(default_i)))
        return default_i
