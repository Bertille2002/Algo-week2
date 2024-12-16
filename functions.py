import pandas as pd 
from datetime import date 
import csv

# Menu display options
def display_menu() : 
    print("\n Interactive menu : ")
    print("1. Sign in")
    print("2. Sign up")
    option = input("Enter your choice : ")
    return option

# read data in df
def load_user_data():
    user_data = {}
    try:
        with open('users.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user_data[row['username']] = row['password']
    except FileNotFoundError:
        print(f"Error: The file 'users.csv' does not exist.")
    return user_data

# login function
def login() : 
    user_data = load_user_data('users.csv')
    input_username = input("Enter your username : ").strip()
    if input_username in user_data :
        input_password = input("Enter password : ").strip()
        if input_password == user_data[input_username] :
            print("Login successful !")
            # redirect to product menu :)))))))))))))))))))
        else :
            print("Incorrect password.")
    else :
        print("Username not found. Try again or create an accout.")

# sign up function 

# find last id for unique IDs
def get_last_ID() : 
    df = pd.read_csv('users.csv')
    if not df.empty :
        last_id = df['ID'].iloc[-1]
        return last_id
    else :
        print("CSV file is empty")
        return 0

# add user function
def new_user() :
    last_id = get_last_ID()
    # ask for sign up details 
    new_name = input("Enter your first name : ")
    new_lname = input("Enter your last name : ")
    new_username = input("Enter your username : ")
    new_password = input("Enter your password : ")
    new_date = 'NA'
    new_id = last_id + 1
    # Define new row
    new_user_data = {
        'ID': [new_id],
        'first_name': [new_name],
        'last_name': [new_lname],
        'username': [new_username],
        'password': [new_password],
        'order_date': [new_date]
    }
    new_df = pd.DataFrame(new_user_data)
    # add new user info to csv file
    new_df.to_csv('users.csv', mode='a',index=False, header=False)
    print("New user added successfully!")
    
    # create blank csv with fieldnames and name the file 'orders'_'username'.csv















































# Change data
# def change_data() : 
#     row_to_change = input("Enter your username : ")
#     value_to_change = input("Enter the data you wish to change (username, password) : ")
#     if value_to_change not in ['username', 'password'] :
#         print("Invalid input")
#         return 
#     replacement_value = input(f"Enter your new {value_to_change} : ") 
#     row_index = df.loc[df['username'] == row_to_change]
#     try : 
#         if value_to_change == 'username' : 
#             new_username = input(f"Enter your new username : ")
#             df.loc[row_index, 'username'] = new_username 
#             print("Username successfully updated ! ")
#         elif value_to_change == 'password' : 
#             new_password = input(f"Enter your new password : ")
#             df.loc[row_index, 'password'] = new_password
#             print("Password successfully updated ! ")
#         else :
#             print("Invalid input")
#             break
#     except FileNotFoundError : 
#         print("Error : database not found")

