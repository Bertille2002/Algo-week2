# login with hashed password db
from hashlib import sha256
import pandas as pd 

# read data in df
def load_user_data():
    user_data = {}
    try:
        df = pd.read_csv('users.csv')
        user_data = pd.Series(df['password'].values, index=df['username']).to_dict()
    except FileNotFoundError:
        print(f"Error: The file 'users.csv' does not exist.")
    return user_data

def login() : 
    user_data = load_user_data()
    input_username = input("Enter your username : ").strip()
    if input_username in user_data :
        input_password = input("Enter password : ").strip()

        if input_password == user_data[input_username] :
            print("Login successful !")
            # redirect to 'products_function.py' 
            products_main(input_username)
        else :
            print("Incorrect password.")
    else :
        print("Username not found. Try again or create an account.")



# Generate salted hashing
def hash_password(password, salt=None) :
    if not salt :
        salt = os.urandom(16).hex()
    salted_password = salt + password
    hashed_password = hashlib.sha512(salted_password.encode('utf-8')).hexdigest()
    return salt, hashed_password

def new_user() :
    last_id = get_last_ID()
    # read existing user data
    try :
        users_df = pd.read_csv('users.csv')
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
        new_df.to_csv('users.csv', mode='a',index=False, header=False)
    else :
        new_df.to_csv('users.csv', mode='w',index=False, header=True)
    print("New user added successfully!")
    # Create new csv products file
    orders_file = os.path.join(folder_path,f'orders_{new_username}.csv')
    if not os.path.exists(orders_file) :
        orders_df = pd.DataFrame(columns=["ID", "first_name", "last_name", "username", "password", "order_date"])
        orders_df.to_csv(orders_file, index=False)
    print(f"Orders file '{orders_file}' created in '{folder_path}' folder.")