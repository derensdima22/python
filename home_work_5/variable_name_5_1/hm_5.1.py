import keyword
import string
import re

variable_name = input("Enter variable name: ")

def is_validate_name(name):
    if (name in keyword.kwlist
            or (name and name[0].isdigit())
            or (name.count('_') > 1 and name == '_' * len(name))
            or (' ' in name)
            or (any(name.isupper() for name in name))):
        return False

    for simbol in string.punctuation:
        if simbol != '_' and simbol in name:
            return False

    return True

print(is_validate_name(variable_name))

# V 2

variable_name_v2 = input("Enter variable name v2: ")

pattern = r'^[a-z_][a-z0-9_]*$'

if (variable_name_v2 == "_"
        or (re.fullmatch(pattern, variable_name_v2)
            and variable_name_v2 not in keyword.kwlist
            and not re.fullmatch(r'_+', variable_name_v2))):
    print("You can use the variable name")
else:
    print("Cannot use variable name")
