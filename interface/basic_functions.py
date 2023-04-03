import os
import sys
import sqlite3
from datetime import datetime
from data_storage.database_func import AppDatabase


class BasicFunctions():
    
    def database_init():
        """ 1st stage: The beginning of the program along with the initialization of the database, 
        if there is no db file, a new one is created along with the admin account"""
        
        if not os.path.exists('data_storage/hotel_app_database.db'):
            user_input = input('Database does not exist do you want to create a new one?\nYes (Y), No (N) ')
            
            if user_input == 'Y':
                AppDatabase.create_database()
                print('Database created')
                
            else:
                sys.exit()
        else:
            print('Database loaded')

    def login():
        """
        Login funkcion by email and password, first cheking regular users.
        if is not in database then serching in admins.
        """
        print('''
----------------------------------------------------------
|   Welcome to the hotel reservation management system   |
----------------------------------------------------------
    ''')
        print("\nLogin")
        print('-'*15)
        user_email_input = input('Email:    ')
        user_password_input = input('Password: ')
        conn = sqlite3.connect('data_storage/hotel_app_database.db')
        c = conn.cursor()
        c.execute('SELECT * FROM regular_users WHERE email = ? AND password = ?', (user_email_input, user_password_input))
        user = c.fetchone()
        if user is None:
            c.execute('SELECT * FROM admins WHERE email = ? AND password = ?', (user_email_input, user_password_input))
            user = c.fetchone()
        if user is not None:
            print('\nLogin user: ', user[1], user[2])
            user_data = (user[0], user[1], user[2], user[3])
            return user_data
        else:
            print('\nIncorrect login')
        
        conn.close()

    def set_user_permissions(user_data):
        """Set user permissions based on user type"""
        conn = sqlite3.connect('data_storage/hotel_app_database.db')
        c = conn.cursor()

        user_type = 'regular'
        c.execute('SELECT email FROM admins')
        admin_emails = [r[0] for r in c.fetchall()]  # get all admin emails from database

        if user_data[3] in admin_emails:  # check if user email is in admin_emails
            user_type = 'admin'

        conn.close()

        return user_type

    def get_user_basic_input():
        '''
        Get input from user: first name, last name, email and password 
        and if is correct return this values.
        '''
        fname = input('First name: ')
        lname = input('Last name:  ')
        email = input('email:      ')
        password = input('Password:   ')
        
        if input('\nIs this information correct? (Y/N)\n') == 'Y':
            return fname, lname, email, password

    def get_customer_input():
        """
        Get input from user: fist name, last name, phone_number, email, bill
        and if is correct return this values.
        """
        fname = input('First name:   ')
        lname = input('Last name:    ')
        phone_number = int(input('Phone number: '))
        email = input('Email:        ')
        bill = float(input('Bill:         '))
        
        if input('\nIs this information correct? (Y/N)\n') == 'Y':
            return fname, lname, phone_number, email, bill
        
    def get_room_input():
        '''
        Get input from user room_number, number_of_people, location, status, price
        if is correct return this values.
        '''
        room_number = input('Room number:                  ')
        number_of_people = int(input('Number of people it contains: '))
        location = input('Location:                     ')
        status = input('Status:                       ')
        price = float(input('Price for day:                '))
        
        if input('\nIs this information correct? (Y/N)\n') == 'Y':
            return room_number, number_of_people, location, status, price
         
    def get_update_info():
        """
        Get input from user to use it for update values in database tables.
        """
        id = int(input('\nid: '))
        name_group = input('Group: ')
        update_value = input('New value: ')
        
        if input('\nIs this information correct? (Y/N)\n') == 'Y':
            return id, name_group, update_value
        
    def log_activity(user, function):
        """log activity"""
        try:
            with sqlite3.connect('data_storage/hotel_app_database.db') as conn:
                c = conn.cursor()
                timestamp = datetime.utcnow()
                c.execute("INSERT INTO activity_log (user, function, timestamp) VALUES (?, ?, ?)", (user, function, timestamp))
                conn.commit()

        except sqlite3.Error as error:
            print(error)
        finally:
            if conn:
                conn.close()