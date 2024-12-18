import pandas as pd 
from datetime import date 
# Generate unique salt
# import uuid 
import os
# Import products menu function
from menu_products import *
# Import to hash and salt passwords
import hashlib

# Hash and salt password using SHA-256
# def hash_password(password: str) -> str :
#     return hashlib.sha256((password).encode('utf-8')).hexdigest()

# Generate random salt function
# def generate_salt() -> str :
#     return uuid.uuid4().hex

# Menu display options
def display_menu() : 
    print("\n Interactive menu : ")
    print("1. Sign in")
    print("2. Sign up")
    print("3. Change user info")
    print("4. Delete account")
    option = input("Enter your choice : ")
    return option

# read data in df
def load_hashed_user_data():
    user_data = {}
    df = pd.read_csv('users_hashed.csv')
    for _, row in df.iterrows() :
        user_data[row['username']] = {
            'password': row['password']
        }
    return user_data

# login function
def login() : 
    hashed_user_data = load_hashed_user_data()
    input_username = input("Enter your username : ").strip()
    if input_username in hashed_user_data :
        input_password = input("Enter password : ").strip()
        hashed_password = hashed_user_data[input_username]['password']
        input_password_hash = hashlib.sha256(input_password.encode()).hexdigest()
        if input_password_hash == hashed_password :
            print("Login successful !")
            # redirect to 'products_function.py' 
            products_main(input_username)
        else :
            print("Incorrect password.")
    else :
        print("Username not found. Try again or create an account.")

# sign up function 

# find last id for unique IDs
def get_last_ID() : 
    df = pd.read_csv('users_hashed.csv')
    if not df.empty :
        last_id = df['ID'].iloc[-1]
        return last_id
    else :
        print("CSV file is empty")
        return 0

# add user function
def new_user() :
    last_id = get_last_ID()
    # read existing user data
    try :
        users_df = pd.read_csv('users_hashed.csv')
    except :
        users_df = pd.DataFrame(columns=["ID", "first_name", "last_name", "username", "password", "order_date"])
    # ask for sign up details 
    new_name = input("Enter your first name : ")
    new_lname = input("Enter your last name : ")
    new_username = input("Enter your username : ")
    new_password = input("Enter your password : ")
    new_date = 'NA'
    new_id = last_id + 1
    # Define the folder path for products csv file creation 
    folder_path = 'csv_files'
    if not os.path.exists(folder_path) :
        os.makedirs(folder_path)
    # check if username already exists 
    if new_username in users_df['username'].values :
        print("Username already exists.")
        return
    # Genertate salt and hash for password 
    # salt = generate_salt()
    hashed_password = hashlib.sha256(new_password.encode())
    # Define new row
    new_user_data = {
        'ID': [new_id],
        'first_name': [new_name],
        'last_name': [new_lname],
        'username': [new_username],
        'password': [hashed_password],
        'order_date': [new_date]
    }
    new_df = pd.DataFrame(new_user_data)
    # add new user info to csv file
    if not users_df.empty :
        new_df.to_csv('users_hashed.csv', mode='a',index=False, header=False)
    else :
        new_df.to_csv('users_hashed.csv', mode='w',index=False, header=True)
    print("New user added successfully!")
    # Create new csv products file
    orders_file = os.path.join(folder_path,f'orders_{new_username}.csv')
    if not os.path.exists(orders_file) :
        orders_df = pd.DataFrame(columns=["ID", "first_name", "last_name", "username", "password", "order_date"])
        orders_df.to_csv(orders_file, index=False)
    print(f"Orders file '{orders_file}' created in '{folder_path}' folder.")

# delete user 
def delete_user():
    print("You can only delete your own account.")
    hashed_user_data = load_hashed_user_data()
    print("Please login first : ")
    input_username = input("Enter your username : ").strip()
    if input_username in hashed_user_data :
        input_password = input("Enter password : ").strip()
        hashed_password = hashed_user_data[input_username]['password']
        if hashlib.sha256(input_password.encode()).hexdigest() == hashed_password :
            print("Successful login, you can now delete your account.")
            user_to_delete = input("Enter the account you wish to delete: ")
            #Lecture des données d'utilisateur csv en pandas
            df = pd.read_csv('users_hashed.csv')
            #Vérificatin de la présence de l'utilisateur dans la DataBase
            if user_to_delete not in df['username'].values:
                print(f"No user with Name = '{user_to_delete}' was found.")
                return
            #Séléction de l'utilisateur à supprimer de la DataFrame 
            df = df[df['username'] != user_to_delete]
            #Enregistrement de la DataFRame modifée dans le fichier csv 
            df.to_csv('users_hashed.csv', index=False)
            print(f"The account: {user_to_delete} has been deleted.")
        else :
            print("Incorrect password.")
    else :
        print("username not found.")

# Change data
def change_data() : 
    hashed_user_data = load_hashed_user_data()
    print("Please login first : ")
    input_username = input("Enter your username : ").strip()
    if input_username in hashed_user_data :
        input_password = input("Enter password : ").strip()
        hashed_password = hashed_user_data[input_username]['password']
        if hashlib.sha256(input_password.encode()).hexdigest() == hashed_password :
            print("Successful login, you can now change your user data.")
            row_to_change = input("Enter your username : ")
            value_to_change = input("Enter the data you wish to change (username, password) : ")
            if value_to_change not in ['username', 'password'] :
                print("Invalid input")
                return 
            replacement_value = input(f"Enter your new {value_to_change} : ") 
            row_index = df.loc[df['username'] == row_to_change]
            try : 
                if value_to_change == 'username' : 
                    new_username = input(f"Enter your new username : ")
                    df.loc[row_index, 'username'] = new_username 
                    print("Username successfully updated ! ")
                elif value_to_change == 'password' : 
                    new_password = input(f"Enter your new password : ")
                    hashed_new_password = hashlib.sha256(new_password.encode()).hexdigest()
                    df.loc[row_index, 'password'] = hashed_new_password
                    print("Password successfully updated ! ")
                else :
                    print("Invalid input")
            except FileNotFoundError : 
                print("Error : database not found")
        else :
            print("Incorrect password.")
    else :
        print("username not found.")

