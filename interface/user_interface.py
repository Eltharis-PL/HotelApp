from interface.interface_functions import InterfaceFunctions
from ui.application_gui import AppGui
from interface.basic_functions import BasicFunctions


class UserInterface:
    
    def regular_user_scheme_operations(user):
        
        """The entire operation scheme of the Regular user interface"""
        
        while True:
            
            AppGui.regular_user_interface()
            user_input = input('')
            
            if user_input == '1':
                #Creating new customer
                InterfaceFunctions.creating_new_customer()
                BasicFunctions.log_activity(user=user[1] + ' ' + user[2], function='Creating customer')
                
            elif user_input == '2':
                #Display all customers
                InterfaceFunctions.display_all_customers()
                BasicFunctions.log_activity(user=user[1] + ' ' + user[2], function='Display customers')
                
            elif user_input == '3':
                #Display all rooms
                InterfaceFunctions.display_all_rooms()
                BasicFunctions.log_activity(user=user[1] + ' ' + user[2], function='Display rooms')
                
            elif user_input == '4':
                #Display available rooms
                InterfaceFunctions.display_available_rooms()
                BasicFunctions.log_activity(user=user[1] + ' ' + user[2], function='Display available rooms')
    
            elif user_input == '5':
                #Update customer info 
                InterfaceFunctions.update_customer()
                BasicFunctions.log_activity(user=user[1] + ' ' + user[2], function='Update customer')
                
            elif user_input == '7':
                InterfaceFunctions.check_in()
                BasicFunctions.log_activity(user=user[1] + ' ' + user[2], function='check_in')
                
            elif user_input == '8':
                InterfaceFunctions.check_out()
                BasicFunctions.log_activity(user=user[1] + ' ' + user[2], function='check_out')
    
            elif user_input == '9':
                #Exit admin functions
                AppGui.clear_screen()
                return False