#--------------------------------------------------------------------------------------------------#
# Import necessary libraries.                                                                      #
#--------------------------------------------------------------------------------------------------#
import os
import time
from utils.ascii_text import *
from utils.troubleshooting import *
from pathlib import Path
from rich import print
from cryptography.fernet import Fernet
#--------------------------------------------------------------------------------------------------#
# Variables.                                                                                       #
#--------------------------------------------------------------------------------------------------#

#--------------------------------------------------------------------------------------------------#
# Path's                                                                                           #
#--------------------------------------------------------------------------------------------------#
user_path = Path.home()
script_path = user_path / ("Request_System")
request_folder = script_path / ("Requests")
#--------------------------------------------------------------------------------------------------#
# Create directory                                                                                 #
#--------------------------------------------------------------------------------------------------#
def create_directory():
    script_path.mkdir(exist_ok=True)
    request_folder.mkdir(exist_ok=True)    
#--------------------------------------------------------------------------------------------------#
# Date / Time.                                                                                     #
#--------------------------------------------------------------------------------------------------#
def date_time():
    print(time.strftime(DATE_TIME).center(100, "-"))
    input("[Press ENTER to continue]".center(100, "-"))
#--------------------------------------------------------------------------------------------------#
# Add request.                                                                                     #
#--------------------------------------------------------------------------------------------------#
def add_request():
    print(ADD_REQUEST)
    add_name = input("[Name]: ")
    add_phone = input("[Phone]: ")
    add_address = input("[Address]: ")
    add_request = input("[Request obs]: ")
    data = (
        f"[Name]: {add_name}\n"
        f"[Phone]: {add_phone}\n"
        f"[Address]: {add_address}\n"
        f"[Request]: {add_request}\n"
    )
    global key
    key = Fernet.generate_key()
    fernet = Fernet(key)
    global encrypt_msg
    encrypt_msg = fernet.encrypt(data.encode())
    request_file = request_folder / (add_name + ".txt")
    if not request_file.exists():
        with open(request_file, "xb+") as file:
            file.write(encrypt_msg)
        print(
        "\n[!] [Encrypted data]:\n"
        f"\n{encrypt_msg}\n"
        )
    else:
        print(FILE_EXISTS_ERROR)
#--------------------------------------------------------------------------------------------------#
# Remove Request.                                                                                  #
#--------------------------------------------------------------------------------------------------#
def rem_request():
    print(REMOVE_REQUEST)
    remove_choice = str(input("[Name of the request]: "))
    remove_file = request_folder / (remove_choice + ".txt")
    if remove_file.exists():
        remove_file.unlink()
        print("\n[!] [File removed]\n")
    else:
        print(FILE_NOT_FOUND_ERROR)
#--------------------------------------------------------------------------------------------------#
# List of requests.                                                                                #
#--------------------------------------------------------------------------------------------------#
def list_requests():
    print(LIST_OF_REQUESTS)
    for i, dir in enumerate(os.listdir(request_folder)):
        print(f"[{i}]:[green]{dir}[/]")
#--------------------------------------------------------------------------------------------------#
# Read request.                                                                                    #
#--------------------------------------------------------------------------------------------------#
def read_request():
    print(READ_REQUEST)
    read_choice = str(input("[Name of the request you want to read]: "))
    read_file = request_folder / (read_choice + ".txt")
    if read_file.exists():
        pass
#--------------------------------------------------------------------------------------------------#
# Menu.                                                                                            #
#--------------------------------------------------------------------------------------------------#
def menu():
    while True:
        print(MENU)
        try:
            menu_choice = int(input("[Your answer]: "))
            match menu_choice:
                case 0:
                    exit()
                case 1:
                    add_request()
                    date_time()
                case 2:
                    rem_request()
                    date_time()
                case 3:
                    list_requests()
                    date_time()
                case 4:
                    read_request()
                    date_time()
                case _:
                    print(VALUE_ERROR)
                    date_time()
        except ValueError:
            print(VALUE_ERROR)
            date_time()