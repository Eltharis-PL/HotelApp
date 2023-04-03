from interface.basic_functions import BasicFunctions
from interface.admin_interface import AdminInterface
from interface.user_interface import UserInterface
from ui.application_gui import AppGui
"""
    This program is used to register hotel guests in the appropriate accommodation.
    Autor: Rafał Zakrzewski
    email: crazypython.dev@gmail.com
    Data: 01.03.2023
    Wersja: on bulid
"""

def main():
    #Database chaking and init new when file is missing.  
    BasicFunctions.database_init()
    while True:
        # Login user and seting permissions
        try: 
            user = BasicFunctions.login()
            user_type = BasicFunctions.set_user_permissions(user)
            AppGui.clear_screen()
            
            if user_type == 'admin':
                #Admin is log with interface
                AdminInterface.admin_scheme_operations(user)
                   
            else:
                #Regular user is log with interface.
                UserInterface.regular_user_scheme_operations(user)
                
        except Exception:
            #If we have error after inputing wrong email or password. 
            input('')
            AppGui.clear_screen()      
        
if __name__ == "__main__":
    main()