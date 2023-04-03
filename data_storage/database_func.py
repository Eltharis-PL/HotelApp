import sqlite3
from prettytable import PrettyTable


class AppDatabase:
    
    """This class contains all the necessary functions to create a new database and make it work"""
    
    def create_database():
        """Creating new Database with admin accont"""
        try:
            with sqlite3.connect('data_storage/hotel_app_database.db') as conn:
                c = conn.cursor()
                
                #Table "employess"
                c.execute('''CREATE TABLE IF NOT EXISTS regular_users
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            fname TEXT NOT NULL,
                            lname TEXT NOT NULL,
                            email TEXT NOT NULL UNIQUE,
                            password TEXT NOT NULL)''')
                
                #Table "admins"
                c.execute('''CREATE TABLE IF NOT EXISTS admins
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            fname TEXT NOT NULL,
                            lname TEXT NOT NULL,
                            email TEXT NOT NULL UNIQUE,
                            password TEXT NOT NULL)''')

                #Table "customers"
                c.execute('''CREATE TABLE IF NOT EXISTS customers
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            fname TEXT NOT NULL,
                            lname TEXT NOT NULL,
                            phone_number TEXT NOT NULL,
                            email TEXT NOT NULL UNIQUE,
                            check_in DATETIME,
                            check_out DATETIME,
                            bill FLOAT NOT NULL)''')

                #Table "rooms"
                c.execute('''CREATE TABLE IF NOT EXISTS rooms
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            room_number TEXT NOT NULL,
                            number_of_people INTEGER NOT NULL,
                            location TEXT NOT NULL,
                            status TEXT NOT NULL,
                            price FLOAT NOT NULL)''')
                
                #Table of activity logs
                c.execute('''CREATE TABLE IF NOT EXISTS activity_log
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user TEXT NOT NULL,
                            function TEXT NOT NULL,
                            timestamp DATETIME NOT NULL)''')
                
                c.execute("INSERT INTO admins (fname, lname, email, password) VALUES (?, ?, ?, ?)",
                    ('Kolego', 'Złoty', 'admin1', "admin1"))
                c.execute("INSERT INTO regular_users (fname, lname, email, password) VALUES (?, ?, ?, ?)",
                    ('Elacia', 'Tomczuk', 'regular1', "regular1"))
                c.execute("INSERT INTO rooms (room_number, number_of_people, location, status, price) VALUES (?, ?, ?, ?, ?)",
                    ('A1', 2, 'first floor', "available", 50.50))
                
                conn.commit()
                
        except Exception as error:
            #Display a general error message
            print(f"There was an error creating a new database. Cause: {error}")
    
        finally:
            if conn:
                conn.close()
    
    def add_admin_db(fname, lname, email, password):
        """Adding new administrator to database.

        Args:
            fname (str): First name
            lname (str): Last name 
            email (str): Email 
            password (str): password     
        """
        try:
            with sqlite3.connect('data_storage/hotel_app_database.db') as conn:
                c = conn.cursor()
                c.execute("INSERT INTO admins (fname, lname, email, password) VALUES (?, ?, ?, ?)",
                    (fname, lname, email, password))
                conn.commit()
                
        except sqlite3.IntegrityError as error:
            #Display an error message related to the database
            print(f"Unable to add employee {fname} {lname}. Cause: {error}")
        
        except Exception as error:
            #Display a general error message
            print(f"There was an error adding an employee {fname} {lname}. Cause: {error}")
        
        finally:
            if conn:
                conn.close()
    
    def add_regular_user_db(fname, lname, email, password):
        """Adding new regular user to database.

        Args:
            fname (str): First name
            lname (str): Last name
            email (str): Email
            password (str): password
        """
        try:
            with sqlite3.connect('data_storage/hotel_app_database.db') as conn:
                c = conn.cursor()
                c.execute("INSERT INTO regular_users (fname, lname, email, password) VALUES (?, ?, ?, ?)",
                    (fname, lname, email, password))
                conn.commit()
                
        except sqlite3.IntegrityError as error:
            #Display an error message related to the database
            print(f"Unable to add employee {fname} {lname}. Cause: {error}")
        
        except Exception as error:
            #Display a general error message
            print(f"There was an error adding an employee {fname} {lname}. Cause: {error}")
        
        finally:
            if conn:
                conn.close()
    
    def add_customer_db(fname, lname, phone_number, email, bill):
        """
        Adds a new customer to the database.

        Args:
        - fname: string, first name
        - lname: string, last name 
        - phone_number: int, phone number 
        - email: string, email 
        - bill: float, bill
        """
        try:
            with sqlite3.connect('data_storage/hotel_app_database.db') as conn:
                c = conn.cursor()
                c.execute("INSERT INTO customers (fname, lname, phone_number, email, bill) VALUES (?, ?, ?, ?, ?)",
                    (fname, lname, phone_number, email, bill))
                conn.commit()
                
        except sqlite3.IntegrityError as error:
            #Display an error message related to the database
            print(f"Unable to add customer {fname} {lname}. Cause: {error}")
        
        except Exception as error:
            #Display a general error message
            print(f"There was an error adding an customer {fname} {lname}. Cause: {error}")
        
        finally:
            if conn:
                conn.close()
    
    def add_new_room_db(room_number, number_of_people, location, status, price):
        """
        Adds a new room to the database.
        
        Parameters:
        - room_number: str, representing the room number
        - number_of_people: int, representing the maximum number of people allowed in the room
        - location: str, representing the location of the room
        - status: str, (e.g., available, occupied, under maintenance)
        - price: float, representing the price per night of the room
        
        Raises:
        - sqlite3.IntegrityError: if there is a problem with the database integrity (e.g., room number already exists)
        - Exception: for any other type of error
        
        Returns: None
        """
        try:
            with sqlite3.connect('data_storage/hotel_app_database.db') as conn:
                c = conn.cursor()
                c.execute("INSERT INTO rooms (room_number, number_of_people, location, status, price) VALUES (?, ?, ?, ?, ?)",
                    (room_number, number_of_people, location, status, price))
                conn.commit()
        except sqlite3.IntegrityError as error:
            #Display an error message related to the database
            print(f"Unable to add room {room_number}. Cause: {error}")
        
        except Exception as error:
            #Display a general error message
            print(f"There was an error adding an new room Nr:{room_number}. Cause: {error}")
        
        finally:
            if conn:
                conn.close()
            
    def display_admin_users_db():
        """Display all Hotel employess"""
        try:
            with sqlite3.connect('data_storage/hotel_app_database.db') as conn:
                c = conn.cursor()
                c.execute("SELECT * FROM admins")
                rows = c.fetchall()
                table = PrettyTable()
                table.field_names = ['Id', 'fname', 'lname', 'email', 'password']
                for row in rows:
                    table.add_row(row)
                print(table)
                    
        except Exception as error:
            #Display a general error message
            print(f"There was an error displaying employees. Cause: {error}")
               
        finally:
            if conn:
                conn.close()
                
    def display_regular_users_db():
        """Display all Hotel employess"""
        try:
            with sqlite3.connect('data_storage/hotel_app_database.db') as conn:
                c = conn.cursor()
                c.execute("SELECT * FROM regular_users")
                rows = c.fetchall()
                table = PrettyTable()
                table.field_names = ['Id', 'fname', 'lname', 'email', 'password']
                for row in rows:
                    table.add_row(row)
                print(table)
                
        except Exception as error:
            #Display a general error message
            print(f"There was an error displaying employees. Cause: {error}") 
             
        finally:
            if conn:
                conn.close()
               
    def display_customers_db():
        """Display all custommers"""
        try:
            with sqlite3.connect('data_storage/hotel_app_database.db') as conn:
                c = conn.cursor()
                c.execute("SELECT * FROM customers")
                rows = c.fetchall()
                table = PrettyTable()
                table.field_names = ['id', 'fname', 'lname', 'phone_number', 'email', 'check_in', 'check_out', 'bill']
                for row in rows:
                    table.add_row(row)
                print(table)
                
        except Exception as error:
            #Display a general error message
            print(f"There was an error displaying customers. Cause: {error}")
            
        finally:
            if conn:
                conn.close()
             
    def display_rooms_db():
        """Display all Hotel rooms"""
        try:
            with sqlite3.connect('data_storage/hotel_app_database.db') as conn:
                c = conn.cursor()
                c.execute("SELECT * FROM rooms")
                rows = c.fetchall()
                table = PrettyTable()
                table.field_names = ['id', 'room_number', 'number_of_people', 'location', 'status', 'price']
                for row in rows:
                    table.add_row(row)
                print(table)
                    
        except Exception as error:
            #Display a general error message
            print(f"There was an error displaying rooms. Cause: {error}")
        
        finally:
            if conn:
                conn.close()
                
    def display_available_rooms_db():
        """Display available Hotel rooms"""
        try:
            with sqlite3.connect('data_storage/hotel_app_database.db') as conn:
                c = conn.cursor()
                c.execute("SELECT * FROM rooms WHERE status='available'")
                rows = c.fetchall()
                table = PrettyTable()
                table.field_names = ['id', 'room_number', 'number_of_people', 'location', 'status', 'price']
                for row in rows:
                    table.add_row(row)
                    print(table)
                        
        except Exception as error:
            #Display a general error message
            print(f"There was an error displaying rooms. Cause: {error}")
            
        finally:
            if conn:
                conn.close()
      
    def display_activity_logs_db():
        """Display activity_logs"""
        try:
            with sqlite3.connect('data_storage/hotel_app_database.db') as conn:
                c = conn.cursor()
                c.execute("SELECT * FROM activity_log")
                rows = c.fetchall()
                table = PrettyTable()
                table.field_names = ['id', 'user', 'function', 'timestamp']
                for row in rows:
                    table.add_row(row)
                print(table)
                    
        except Exception as error:
            #Display a general error message
            print(error)
        
        finally:
            if conn:
                conn.close()
    
    def update_admin_info_db(id, name_group, update_value):
        """Update Admins informaction"""
        try:
            with sqlite3.connect('data_storage/hotel_app_database.db') as conn:
                c = conn.cursor()
                c.execute(f"UPDATE admins SET {name_group} = ? WHERE id = ?", (update_value, id))
                conn.commit()
                
        except Exception as error:
            print(f"There was an error updating the admin {name_group}. Cause: {error}")
            
        finally:
            if conn:
                conn.close()
        
    def update_regular_user_info_db(id, name_group, update_value):
        """Update Regular user informaction"""
        try:
            with sqlite3.connect('data_storage/hotel_app_database.db') as conn:
                c = conn.cursor()
                c.execute(f"UPDATE regular_users SET {name_group} = ? WHERE id = ?", (update_value, id))
                conn.commit()
                
        except Exception as error:
            print(f"There was an error updating the admin {name_group}. Cause: {error}")
        
        finally:
            if conn:
                conn.close()
         
    def update_customer_info_db(id, name_group, update_value):
        """Update Customer informaction"""
        try:
            with sqlite3.connect('data_storage/hotel_app_database.db') as conn:
                c = conn.cursor()
                c.execute(f"UPDATE customers SET {name_group} = ? WHERE id = ?", (update_value, id))
                conn.commit()
                
        except Exception as error:
            print(f"There was an error updating the admin {name_group}. Cause: {error}")
            
        finally:
            if conn:
                conn.close()
            
    def update_room_info_db(id, name_group, update_value):
        """Update room info"""
        try:
            with sqlite3.connect('data_storage/hotel_app_database.db') as conn:
                c = conn.cursor()
                c.execute(f"UPDATE rooms SET {name_group} = ? WHERE id = ?", (update_value, id))
                conn.commit()
        except Exception as error:
            print(f"There was an error updating the admin {name_group}. Cause: {error}")
        
        finally:
            if conn:
                conn.close()
                
    def delete_admin_db(id):
        """Delate Admin """
        try:
            with sqlite3.connect('data_storage/hotel_app_database.db') as conn:
                c = conn.cursor()
                c.execute("DELETE FROM admins WHERE id=?", (id))
                conn.commit()
                print("Deleted successfully.")
                input('')

        except sqlite3.Error as error:
            print(f"Failed to delete. Error: {error}")

        finally:
            if conn:
                conn.close()
    
    def delete_regular_user_db(id):
        """Delate Admin """
        try:
            with sqlite3.connect('data_storage/hotel_app_database.db') as conn:
                c = conn.cursor()
                c.execute("DELETE FROM regular_users WHERE id=?", (id))
                conn.commit()
                print("Deleted successfully.")
                input('')

        except sqlite3.Error as error:
            print(f"Failed to delete. Error: {error}")

        finally:
            if conn:
                conn.close()
                
    def delete_customer_db(id):
        """Delate customer """
        try:
            with sqlite3.connect('data_storage/hotel_app_database.db') as conn:
                c = conn.cursor()
                c.execute("DELETE FROM customers WHERE id=?", (id))
                conn.commit()
                print("Deleted successfully.")
                input('')

        except sqlite3.Error as error:
            print(f"Failed to delete. Error: {error}")

        finally:
            if conn:
                conn.close()
                
    def delete_room_db(id):
        """Delate room"""
        try:
            with sqlite3.connect('data_storage/hotel_app_database.db') as conn:
                c = conn.cursor()
                c.execute("DELETE FROM rooms WHERE id=?", (id))
                conn.commit()
                print("Deleted successfully.")
                input('')

        except sqlite3.Error as error:
            print(f"Failed to delete. Error: {error}")

        finally:
            if conn:
                conn.close()
    
    def check_in_db(id, time):
        try:
            with sqlite3.connect('data_storage/hotel_app_database.db') as conn:
                c = conn.cursor()
                c.execute("UPDATE customers SET check_in = ? WHERE id = ?", (time, id))
                conn.commit()
                print("operation successfully.")
                input('')

        except sqlite3.Error as error:
            print(f"Error: {error}")

        finally:
            if conn:
                conn.close()
    
    def check_out_db(id, time):
        try:
            with sqlite3.connect('data_storage/hotel_app_database.db') as conn:
                c = conn.cursor()
                c.execute("UPDATE customers SET check_out = ? WHERE id = ?", (time, id))
                conn.commit()
                print("operation successfully.")
                input('')

        except sqlite3.Error as error:
            print(f"Error: {error}")

        finally:
            if conn:
                conn.close()
    