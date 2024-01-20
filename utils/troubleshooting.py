DATE_TIME = """[%H:%M:%S] - [%d/%m/%Y]"""

MODULE_NOT_FOUND_ERROR = """
#--------------------------------------------------------------------------------------------------#
# [red]ModuleNotFoundError[/]
#--------------------------------------------------------------------------------------------------#
# [cyan]Description[/]:
#--------------------------------------------------------------------------------------------------#
# - [green]Indicates that the specified module is not installed.[/]
#--------------------------------------------------------------------------------------------------#
# [cyan]Possible Solution[/]:
#--------------------------------------------------------------------------------------------------#
# - [green]Run pip install example_module to install the missing module.[/]
#
# - [green]Ensure that all dependencies are installed: `pip install -r requirements.txt.`[/]
#--------------------------------------------------------------------------------------------------#
"""

VALUE_ERROR = """
#--------------------------------------------------------------------------------------------------#
# [red]ValueError[/]
#--------------------------------------------------------------------------------------------------#
# [cyan]Description[/]:
#--------------------------------------------------------------------------------------------------#
# - [green]Indicates that the provided input format is not valid.[/]
#--------------------------------------------------------------------------------------------------#
# [cyan]Possible Solution[/]:
#--------------------------------------------------------------------------------------------------#
# - [green]Check if the input is in the correct format by referring to the documentation.[/]
#--------------------------------------------------------------------------------------------------#
"""

FILE_NOT_FOUND_ERROR = """
#--------------------------------------------------------------------------------------------------#
# [red]FileNotFoundError[/]
#--------------------------------------------------------------------------------------------------#
# [cyan]Description[/]:
#--------------------------------------------------------------------------------------------------#
# - [green]Indicates that the specified file was not found.[/]
#--------------------------------------------------------------------------------------------------#
# [cyan]Possible Solution[/]:
#--------------------------------------------------------------------------------------------------#
# - [green]Check if the file is in the correct location.[/]
#--------------------------------------------------------------------------------------------------#
"""

FILE_EXISTS_ERROR = """
#--------------------------------------------------------------------------------------------------#
# [red]FileExistsError[/]
#--------------------------------------------------------------------------------------------------#
# [cyan]Description[/]:
#--------------------------------------------------------------------------------------------------#
# - [green]Indicates that the file you are trying to create already exists.[/]
#--------------------------------------------------------------------------------------------------#
# [cyan]Possible Solution[/]:
#--------------------------------------------------------------------------------------------------#
# - [green]Check if the file already exists before attempting to create it.[/]
#--------------------------------------------------------------------------------------------------#
"""

PERMISSION_ERROR = """
#--------------------------------------------------------------------------------------------------#
# [red]PermissionError[/]
#--------------------------------------------------------------------------------------------------#
# [cyan]Description[/]:
#--------------------------------------------------------------------------------------------------#
# - [green]Indicates that the program does not have permission to access the specified file.[/]
#--------------------------------------------------------------------------------------------------#
# [cyan]Possible Solution[/]:
#--------------------------------------------------------------------------------------------------#
# - [green]Check the file and directory permissions.[/]
#
# - [green]Run the program with elevated permissions if necessary.[/]
#--------------------------------------------------------------------------------------------------#
"""

SYNTAX_ERROR = """
#--------------------------------------------------------------------------------------------------#
# [red]SyntaxError[/]
#--------------------------------------------------------------------------------------------------#
# [cyan]Description[/]:
#--------------------------------------------------------------------------------------------------#
# - [green]Indicates a syntax error in the code, often due to a mistake in the code structure.[/]
#--------------------------------------------------------------------------------------------------#
# [cyan]Possible Solution[/]:
#--------------------------------------------------------------------------------------------------#
# - [green]Review the code around the reported line and fix any syntax errors.[/]
#--------------------------------------------------------------------------------------------------#
"""

INDENTATION_ERROR = """
#--------------------------------------------------------------------------------------------------#
# [red]IndentationError[/]
#--------------------------------------------------------------------------------------------------#
# [cyan]Description[/]:
#--------------------------------------------------------------------------------------------------#
# - [green]Occurs when there is an issue with the indentation of the code block.[/]
#--------------------------------------------------------------------------------------------------#
# [cyan]Possible Solution[/]:
#--------------------------------------------------------------------------------------------------#
# - [green]Check and correct the indentation in the specified code block.[/]
#--------------------------------------------------------------------------------------------------#
"""

NAME_ERROR = """
#--------------------------------------------------------------------------------------------------#
# [red]NameError[/]
#--------------------------------------------------------------------------------------------------#
# [cyan]Description[/]:
#--------------------------------------------------------------------------------------------------#
# - [green]Occurs when trying to access a key that does not exist in a dictionary.[/]
#--------------------------------------------------------------------------------------------------#
# [cyan]Possible Solution[/]:
#--------------------------------------------------------------------------------------------------#
# - [green]Check if the key exists in the dictionary before trying to access it.[/]
#--------------------------------------------------------------------------------------------------#
"""

TYPE_ERROR = """
#--------------------------------------------------------------------------------------------------#
# [red]TypeError[/]
#--------------------------------------------------------------------------------------------------#
# [cyan]Description[/]:
#--------------------------------------------------------------------------------------------------#
# - [green]Indicates that an operation is performed on an inappropriate data type.[/]
#--------------------------------------------------------------------------------------------------#
# [cyan]Possible Solution[/]:
#--------------------------------------------------------------------------------------------------#
# - [green]Check the data types involved in the operation and adjust as necessary.[/]
#--------------------------------------------------------------------------------------------------#
"""

INDEX_ERROR = """
#--------------------------------------------------------------------------------------------------#
# [red]IndexError[/]
#--------------------------------------------------------------------------------------------------#
# [cyan]Description[/]:
#--------------------------------------------------------------------------------------------------#
# - [green]Occurs when you try to access an index that is out of bounds for a list, tuple, or string.[/]
#--------------------------------------------------------------------------------------------------#
# [cyan]Possible Solution[/]:
#--------------------------------------------------------------------------------------------------#
# - [green]Make sure the index is within the bounds of the object.[/]
#--------------------------------------------------------------------------------------------------#
"""

KEY_ERROR = """
#--------------------------------------------------------------------------------------------------#
# [red]KeyError[/]
#--------------------------------------------------------------------------------------------------#
# [cyan]Description[/]:
#--------------------------------------------------------------------------------------------------#
# - [green]Occurs when you try to access a key that does not exist in a dictionary.[/]
#--------------------------------------------------------------------------------------------------#
# [cyan]Possible Solution[/]:
#--------------------------------------------------------------------------------------------------#
# - [green]Verify that the key you are trying to access exists in the dictionary.[/]
#--------------------------------------------------------------------------------------------------#
"""

ATTRIBUTE_ERROR = """
[red]AttributeError[/]

[cyan]Description[/]:

- [green]Indicates that an object does not have a certain attribute.[/]

[cyan]Possible Solution[/]:

- [green]Ensure the object has the desired attribute or correct the attribute name.[/]
"""

ZERO_DIVISION_ERROR = """
#--------------------------------------------------------------------------------------------------#
# [red]ZeroDivisionError[/]
#--------------------------------------------------------------------------------------------------#
# [cyan]Description[/]:
#--------------------------------------------------------------------------------------------------#
# - [green]Occurs when division or modulo by zero is attempted.[/]
#--------------------------------------------------------------------------------------------------#
# [cyan]Possible Solution[/]:
#--------------------------------------------------------------------------------------------------#
# - [green]Ensure that denominators in division operations are not zero before performing the operation.[/]
#
# - [green]Implement conditional checks to handle cases where division by zero could occur.[/]
#--------------------------------------------------------------------------------------------------#
"""

IMPORT_ERROR = """
#--------------------------------------------------------------------------------------------------#
# [red]ImportError[/]
#--------------------------------------------------------------------------------------------------#
# [cyan]Description[/]:
#--------------------------------------------------------------------------------------------------#
# - [green]Occurs when a module cannot be imported.[/]
#--------------------------------------------------------------------------------------------------#
# [cyan]Possible Solution[/]:
#--------------------------------------------------------------------------------------------------#
# - [green]Check if the module is installed `pip install module_name`[/]
#
# - [green]Check if there's an issue with the module's name.[/]
#
# - [green]Ensure that the module is in the correct directory or update the Python path.[/]
#--------------------------------------------------------------------------------------------------#
"""