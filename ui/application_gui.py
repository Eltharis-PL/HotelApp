import os


class AppGui:
    
    def clear_screen():
        """Cleaning terminal screan"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def admin_user_interface():
        print('''
              
----------------------------------------------------------
|             Hotel Administration Interface             |
----------------------------------------------------------
| Please select an option:                               |
|                                                        |
| Creating:                                              |
|                                                        |
| 1. Administrator                                       |
| 2. Regular user                                        |
| 3. Customer                                            |
| 4. Room                                                |
|                                                        |
| Display:                                               |
|                                                        |
| 5. Administrators                                      |
| 6. Regular users                                       |
| 7. Customers                                           |
| 8. Rooms                                               |
|                                                        |
| Update:                                                |
|                                                        |
| 9.  Administrator information                          |
| 10. Regular user information                           |
| 11. Customer information                               |
| 12. Room information                                   |
|                                                        |
| Delete:                                                |
|                                                        |
| 13. Administrator                                      |
| 14. Regular user                                       |
| 15. Customer                                           |
| 16. Room                                               |
|                                                        |
| Other:                                                 |      
| 17. View logs                                          |
| 18. Exit                                               |
----------------------------------------------------------
''')
         
    def regular_user_interface():
        print('''

----------------------------------------------------------
|                   Hotel Interface                       |
----------------------------------------------------------
| Please select an option:                                |
|                                                         |
| 1. Create a new customer                                |
| 2. Display customers                                    |
| 3. Display rooms                                        |
| 4. Display available room                               |
| 5. Update customer information                          |
| 6. Display customer receipts/bills                      |
| 7. Check-in customer                                    |
| 8. Check-out customer                                   |
| 9. Exit                                                 |
----------------------------------------------------------
''')
        
    def adding_admin_interface():
        print("""
----------------------------------------------------------
|               Creating new Admin accont                |
----------------------------------------------------------

Please enter only letters, numbers and special 
characters in these fields.
    
""")
        
    def adding_regular_user_interface():
        print("""
----------------------------------------------------------
|                Creating new user accont                |
----------------------------------------------------------

Please enter only letters, numbers and special 
characters in these fields.
    
""") 
    
    def adding_customer_interface():
        print("""
----------------------------------------------------------
|                  Creating new customer                 |
----------------------------------------------------------

Please enter only letters, numbers and special 
characters in these fields.
    
""")
        
    def adding_room_interface():
        print("""
----------------------------------------------------------
|                  Creating new room                     |
----------------------------------------------------------

Please enter only letters, numbers and special 
characters in these fields.
      
""")
        

        