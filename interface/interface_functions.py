from ui.application_gui import AppGui
from interface.basic_functions import BasicFunctions
from interface.basic_functions import AppDatabase
from datetime import datetime

class InterfaceFunctions():
    
    """This class contains all the necessary functions for the regular user and admin interface to work"""
    
    def creating_new_admin_user():
        #Creating new admin user
        AppGui.clear_screen()
        AppGui.adding_admin_interface()
        AppDatabase.add_admin_db(*BasicFunctions.get_user_basic_input())
    
    def creating_new_regular_user():
        #Creating new regular user 
        AppGui.clear_screen()
        AppGui.adding_regular_user_interface()
        AppDatabase.add_regular_user_db(*BasicFunctions.get_user_basic_input())
        
    def creating_new_customer():
        #Creating new customer
        AppGui.clear_screen()
        AppGui.adding_customer_interface()
        AppDatabase.add_customer_db(*BasicFunctions.get_customer_input())
    
    def creating_new_room():
        #Creating new room in hotel
        AppGui.clear_screen()
        AppGui.adding_room_interface()
        AppDatabase.add_new_room_db(*BasicFunctions.get_room_input())
    
    def display_all_admins():
        #Display all admins
        AppGui.clear_screen()
        AppDatabase.display_admin_users_db()
        input('')
    
    def display_all_regular_users():
        #Display all regular users
        AppGui.clear_screen()
        AppDatabase.display_regular_users_db()
        input('')
    
    def display_all_customers():
        #Display all customers
        AppGui.clear_screen()
        AppDatabase.display_customers_db()
        input('')
    
    def display_all_rooms():
        #Display all rooms
        AppGui.clear_screen()
        AppDatabase.display_rooms_db()
        input('')
    
    def display_available_rooms():
        AppGui.clear_screen()
        AppDatabase.display_available_rooms_db()
        input('')
    
    def display_activity_logs():
        #Display activity logs
        AppGui.clear_screen()
        AppDatabase.display_activity_logs_db()
        input('')
    
    def update_admin():
        #Update admin user
        AppGui.clear_screen()
        AppDatabase.display_admin_users_db()
        AppDatabase.update_admin_info_db(*BasicFunctions.get_update_info())
            
    def update_regular_user():
        #Update regular user
        AppGui.clear_screen()
        AppDatabase.display_regular_users_db()
        AppDatabase.update_regular_user_info_db(*BasicFunctions.get_update_info())
                
    def update_customer():
        #Update customer
        AppGui.clear_screen()
        AppDatabase.display_customers_db()
        AppDatabase.update_customer_info_db(*BasicFunctions.get_update_info())
    
    def update_rooms():
        #Update rooms
        AppGui.clear_screen()
        AppDatabase.display_rooms_db()
        AppDatabase.update_room_info_db(*BasicFunctions.get_update_info())
    
    def delete_admin():
        AppGui.clear_screen()
        AppDatabase.display_admin_users_db()
        AppDatabase.delete_admin_db(input('id: '))
    
    def delete_regular_user():
        AppGui.clear_screen()
        AppDatabase.display_regular_users_db()
        AppDatabase.delete_regular_user_db(input('id: '))
    
    def delete_customer():
        AppGui.clear_screen()
        AppDatabase.display_customers_db()
        AppDatabase.delete_customer_db(input('id: '))
    
    def delete_room():
        AppGui.clear_screen()
        AppDatabase.display_rooms_db()
        AppDatabase.delete_room_db(input('id: '))

    def check_in():
        AppGui.clear_screen()
        AppDatabase.display_customers_db()
        AppDatabase.check_in_db(id=input('id: '), time=datetime.utcnow())
    
    def check_out():
        AppGui.clear_screen()
        AppDatabase.display_customers_db()
        AppDatabase.check_out_db(id=input('id: '), time=datetime.utcnow())
        
        