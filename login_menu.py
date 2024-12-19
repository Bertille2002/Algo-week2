import pandas as pd 
from user_functions import * 

def main():
    users = 'users.csv'
    while True :
        input = display_menu()
        if input == "1" :
            login()
        elif input == "2" :
            new_user()
        elif input == "3" :
            change_data()
        elif input == "4" : 
            delete_user()
        elif input == "5" :
            print("Closing program.")
            break
        else :
            print("Invalid input.")

if __name__ == "__main__" :
    main()