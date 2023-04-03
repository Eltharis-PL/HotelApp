from interface.interface_functions import InterfaceFunctions
from ui.application_gui import AppGui
from interface.basic_functions import BasicFunctions

class AdminInterface:
    
    def admin_scheme_operations(user):
    
        """"The entire operation scheme of the administrator interface"""
        
        while True:
            
            AppGui.clear_screen()
            AppGui.admin_user_interface()
            user_input = input('')
            
            if user_input == '1':
                #Creating new admin user
                InterfaceFunctions.creating_new_admin_user()
                BasicFunctions.log_activity(user=user[1] + ' ' + user[2], function='Creating admin')
                
            elif user_input == '2':
                #Creating new regular user 
                InterfaceFunctions.creating_new_regular_user()
                BasicFunctions.log_activity(user=user[1] + ' ' + user[2], function='Creating user')
                
            elif user_input == '3':
                #Creating new customer
                InterfaceFunctions.creating_new_customer()
                BasicFunctions.log_activity(user=user[1] + ' ' + user[2], function='Creating customer')
                
            elif user_input == '4':
                #Creating new room in hotel
                InterfaceFunctions.creating_new_room()
                BasicFunctions.log_activity(user=user[1] + ' ' + user[2], function='Creating room')
                
            elif user_input == '5':
                #Display all Admin users
                InterfaceFunctions.display_all_admins()
                BasicFunctions.log_activity(user=user[1] + ' ' + user[2], function='Display Admins')
                
            elif user_input == '6':
                #Display all regular users
                InterfaceFunctions.display_all_regular_users()
                BasicFunctions.log_activity(user=user[1] + ' ' + user[2], function='Display users')
        
            elif user_input == '7':
                #Display all customers
                InterfaceFunctions.display_all_customers()
                BasicFunctions.log_activity(user=user[1] + ' ' + user[2], function='Display customers')
                            
            elif user_input == '8':
                #Display all rooms
                InterfaceFunctions.display_all_rooms()
                BasicFunctions.log_activity(user=user[1] + ' ' + user[2], function='Display rooms')
                
            elif user_input == '9':
                #Update admin user
                InterfaceFunctions.update_admin()
                BasicFunctions.log_activity(user=user[1] + ' ' + user[2], function='Update admin')
            
            elif user_input == '10':
                #Update regular user
                InterfaceFunctions.update_regular_user()
                BasicFunctions.log_activity(user=user[1] + ' ' + user[2], function='Update user')
                
            elif user_input == '11':
                #Update customer
                InterfaceFunctions.update_customer()
                BasicFunctions.log_activity(user=user[1] + ' ' + user[2], function='Update customer')
                
            elif user_input == '12':
                #Update rooms
                InterfaceFunctions.update_rooms()
                BasicFunctions.log_activity(user=user[1] + ' ' + user[2], function='Update room')
                
            elif user_input == '13':
                #Delate admin
                InterfaceFunctions.delete_admin()
                BasicFunctions.log_activity(user=user[1] + ' ' + user[2], function='Delete admin')
                
            elif user_input == '14':
                #Delate regular user
                InterfaceFunctions.delete_regular_user()
                BasicFunctions.log_activity(user=user[1] + ' ' + user[2], function='Delete user')
                
            elif user_input == '15':
                #Delate customer
                InterfaceFunctions.delete_customer()
                BasicFunctions.log_activity(user=user[1] + ' ' + user[2], function='Delete customer')
                
            elif user_input == '16':
                #Delate room
                InterfaceFunctions.delete_room()
                BasicFunctions.log_activity(user=user[1] + ' ' + user[2], function='Delete room')
            
            elif user_input == '17':
                #Display logs
                InterfaceFunctions.display_activity_logs()
                BasicFunctions.log_activity(user=user[1] + ' ' + user[2], function='Display logs')
 
            elif user_input == '18':
                #Exit admin functions
                AppGui.clear_screen()
                return False
        