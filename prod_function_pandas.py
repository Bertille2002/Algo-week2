# Options du menu interactif de tri
def sort_menu():
    print("Choose sorting method : ")
    print("1. Sort by Quantity (QuickSort)")
    print("2. Sort by Price (MergeSort)")
    print("3. Sort by Product in alphabetical order (Bubble sort)")
    sort_choice = input("Choose a method (1-3): ")
    return sort_choice

# Option 1 : Afficher la liste de produits
def view_names():
    try:
        df = pd.read_csv('csv_files')
        print("List of products : ")
        for index, row in df.iterrows():
            print(row['P_name'])
    except FileNotFoundError:
        print("The csv_files file was not found")

# Option 2 : Ajouter un nouveau produit

# Defintion de l'ID du nouveau produit, Permet d'avoir un ID unique pour chaque produit
def next_id():
    try:
        df = pd.read_csv('csv_files')
        last_id = df['ID'].max()
        return int(last_id) + 1
    except FileNotFoundError:
        return 1  # Start with ID 1 if file doesn't exist

# Ajout du nouveau produit dans la liste
def new_product():
    new_prod = input("Enter the name of a new product : ")
    new_quant = input("Enter its quantity : ")
    new_price = input("Enter its price (/kg) : ")
    new_expdate = input("Enter the expiration date (dd-mm-yy) : ")
    new_id = next_id()
    new_row = pd.DataFrame([[new_id, new_prod, new_quant, new_price, new_expdate]],
                          columns=["ID", "P_name", "P_quantity", "P_price (in $/Kg)", "order_date"])
    if isfile('csv_files'):
        new_row.to_csv('csv_files', mode='a', header=False, index=False)
    else:
        new_row.to_csv('csv_files', index=False)
    print("New product added successfully.")

# Option 3 : delete product row
def delete_product():
    row_to_delete = input("Enter the product name to delete: ")
    try:
        df = pd.read_csv('csv_files')
        df = df[df['P_name'] != row_to_delete]
        df.to_csv('csv_files', index=False)
        print(f"The product: {row_to_delete} has been deleted.")
    except FileNotFoundError:
        print(f"Error: The file 'csv_files' does not exist.")
    except KeyError:
        print(f"Error: The column 'P_name' does not exist in the file.")

# binary search
def binary_search():
    product_name = input("Enter product name for search : ")
    try:
        df = pd.read_csv('csv_files')
        rows = df.sort_values(by=['P_name'], key=lambda col: col.str.lower()).to_dict('records')
        low, high = 0, len(rows) - 1
        while low <= high:
            mid = (low + high) // 2
            mid_name = rows[mid]['P_name'].lower()
            if mid_name == product_name.lower():
                print(f"Product '{product_name}' found!")
                return rows[mid]
            elif mid_name < product_name.lower():
                low = mid + 1
            else:
                high = mid - 1
        print(f"Product '{product_name}' not found.")
        return None
    except FileNotFoundError:
        print(f"Error : csv_files not found")
        return None
    except KeyError:
        print("Error : column P_name was not found")