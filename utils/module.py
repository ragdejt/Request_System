#--------------------------------------------------------------------------------------------------#
# Import necessary libraries.                                                                      #
#--------------------------------------------------------------------------------------------------#
import time
from utils.troubleshooting import *
from pathlib import Path
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
#--------------------------------------------------------------------------------------------------#
# Add request.                                                                                     #
#--------------------------------------------------------------------------------------------------#
def add_request():
    print("[Add request]".center(100, "-"))
    add_name = input("[Name]: ")
    add_phone = input("[Phone]: ")
    add_address = input("[Address]: ")
    add_request = input("[Request obs]: ")
    print(
        "\n[Encrypting data]\n"
        f"[Name]: {add_name}\n"
        f"[Phone]: {add_phone}\n"
        f"[Address]: {add_address}\n"
        f"[Request]: {add_request}\n"
    )
    data = (
        f"[Name]: {add_name}\n"
        f"[Phone]: {add_phone}\n"
        f"[Address]: {add_address}\n"
        f"[Request]: {add_request}\n"
    )
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypt_msg = fernet.encrypt(data.encode())
    request_file = request_folder / (add_name + ".txt")
    if not request_file.exists():
        with open(request_file, "xb+") as file:
            file.write(encrypt_msg)
        print(
        "\n[Encrypted data]\n"
        f"\n{encrypt_msg}\n"
        )
    else:
        print(FILE_EXISTS_ERROR)
#--------------------------------------------------------------------------------------------------#
# Remove Request.                                                                                  #
#--------------------------------------------------------------------------------------------------#
def rem_request():
    print("[Remove Request]".center(100, "-"))

#--------------------------------------------------------------------------------------------------#
# List of requests.                                                                                #
#--------------------------------------------------------------------------------------------------#
def list_requests():
    print("[List of requests]".center(100, "-"))

#--------------------------------------------------------------------------------------------------#
# Read request.                                                                                    #
#--------------------------------------------------------------------------------------------------#
def read_request():
    print("[Read request]".center(100, "-"))

#--------------------------------------------------------------------------------------------------#
# Menu.                                                                                            #
#--------------------------------------------------------------------------------------------------#
def menu():
    while True:
        print("Menu".center(100, "-"))
        print(
            "[Enter one of the avaliable options]:\n"
            "[0]: [green]Exit[/]\n"
            "[1]: [green]Add request[/]\n"
            "[2]: [green]Remove request[/]\n"
            "[3]: [green]List requests[/]\n"
            "[4]: [green]Read request[/]\n"
        )
        try:
            menu_choice = int(input("[Your answer]: "))
            match menu_choice:
                case 0:
                    exit()
                case 1:
                    add_request()
                case 2:
                    rem_request()
                case 3:
                    list_requests()
                case 4:
                    read_request()
                case _:
                    print(VALUE_ERROR)
        except ValueError:
            print(VALUE_ERROR)