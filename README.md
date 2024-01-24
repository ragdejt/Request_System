# Request System.

***`Author` Ragdejt***

***`Date Created` 20/01/2024***

***`Description`***

This script is designed to manage requests using a command-line interface.
#
The script defines several constants at the top, such as:

- DATE_TIME
- MODULE_NOT_FOUND_ERROR
- FILE_NOT_FOUND_ERROR
- FILE_EXISTS_ERROR
- VALUE_ERROR
- PERMISSION_ERROR
- SYNTAX_ERROR
- INDENTATION_ERROR
- NAME_ERROR
- TYPE_ERROR
- INDEX_ERROR
- KEY_ERROR
- ATTRIBUTE_ERROR
- ZERO_DIVISION_ERROR
- IMPORT_ERROR

Which are used throughout the script to provide clear and consistent error messages and prompts to the user.
#
The `create_directory()` function creates the necessary directories for the script to function. It creates a script directory, a request directory, and a keys directory within the script directory. It also sets the keys directory to be hidden.
#
The `date_time()` function prints the current date and time in a formatted manner and prompts the user to press ENTER to continue.
#
The `add_request()` function is designed to add a new request. It prompts the user to enter their name, phone number, address, and any observations regarding the request. The data is then encrypted using a Fernet key and saved to a text file with the name of the requester in the requests directory. A corresponding key file is also saved in the keys directory.
#
The `rem_request()` function is designed to remove a request. It prompts the user to enter the name of the requester and then deletes the corresponding text file from the requests directory.
#
The `menu()` function displays a menu of options to the user and waits for them to enter a valid option. If the user enters an invalid option, the script will display an error message and prompt the user to try again. If the user enters the option to exit the program (0), the script will exit. Otherwise, the script will call the appropriate function based on the user's selection.
#

# Security Notes

- Before running any script, carefully review and understand the code. This helps you to ensure that the script aligns with its intended purpose and does not have unintended consequences.

- This script is for educational purposes only.
    
- Do not use against any network that you don't own or have authorization to test.

- Make sure you run this script in a secure environment.This can help prevent unintended interactions with other applications and libraries.

#

# Troubleshooting

### ***`ModuleNotFoundError`*** 

***`Description:`***

- Indicates that the specified module is not installed.

***`Possible Solution:`*** 

- Run pip install example_module to install the missing module.

- Ensure that all dependencies are installed by running `pip install -r requirements.txt.`

#

### ***`ValueError`***

***`Description:`***

-  Indicates that the provided input format is not valid.

***`Possible Solution:`***

- Check if the input is in the correct format by referring to the documentation.

#

### ***`FileNotFoundError`***

***`Description:`***

- Indicates that the specified file was not found.

***`Possible Solution:`***

- Check if the file is in the correct location.

#

### ***`FileExistsError`***

***`Description:`***

- Indicates that the file you are trying to create already exists.

***`Possible Solution:`***

- Check if the file already exists before attempting to create it.

#

### ***`PermissionError`***

***`Description:`***

- Indicates that the program does not have permission to access the specified file.

***`Possible Solution:`***

- Check the file and directory permissions.

- Run the program with elevated permissions if necessary.

#

# Contributing

### Report Bugs

- *If you are reporting a bug, please include:*

        1. Your operating system name and version.

        2. Python Version.

        3. Any additional details about your local setup that might be helpful in troubleshooting.

        4. Detailed steps to reproduce the bug.

#

### Fix Bugs

- *If you are fixing a bug, please include:*

        1. Description of the Bug:

        Provide a clear and concise description of the bug.

        2. Steps to Reproduce:

        Outline the steps that lead to the occurrence of the bug.

        3. Expected Behavior:

        Describe what the expected behavior should have been without the bug.

        4. Environment Information:

        Mention your operating system, Python version, and any other relevant environment details.

#

### Implement Features

- *If you are proposing a feature:*

        1. Explain in detail how it would work.

        2. Keep the scope as narrow as possible, to make it easier to implement.

        3. Remember that this is a volunteer-driven project, and that contributions are welcome.

#

### Write Documentation

- If you are writing documentation, please include:

        1. Documented Feature/Function:
        
        Specify which feature or function the documentation covers

        2. Documentation Details:

        Provide clear and comprehensive details about the usage, parameters, and expected outcomes.

        3. Code Examples:

        Include code examples that demonstrate the usage of the documented feature.

        4. Formatting Guidelines:

        If there are specific formatting guidelines for documentation, mention them.

#

### Submit Feedback

- If you are submitting feedback, please include:

        1. Nature of Feedback:

        Clearly state whether the feedback is a suggestion, bug report, or general comment.

        2. Specific Section/Functionality:

        Identify the specific section or functionality your feedback is related to.

        3. Detailed Feedback:

        Provide detailed information to explain your feedback, including any suggestions for improvement.

        4. Reproducibility (if applicable):

        If it's a bug report, mention if you can consistently reproduce the issue and the steps to do so.

#

# Requirements

This script requires Python 3 and the following libraries:  

* rich

* cryptography

# Repository

- You can find the script and its source code in the following repository:   
https://www.github.com/ragdejt/
