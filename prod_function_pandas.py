# Options du menu interactif
import pandas as pd
from os.path import isfile

# Options du menu interactif
def display_menu():
    print("\nInteractive Menu:")
    print("1. View products only")
    print("2. Add a new product")
    print("3. Delete a product")
    print("4. Search for a specific product")
    print("5. Sort table")
    print("6. Close file")
    option = input("Enter your choice (1-6): ")
    return option

# Options du menu interactif de tri
def sort_menu():
    print("Choose sorting method : ")
    print("1. Sort by Quantity (QuickSort)")
    print("2. Sort by Price (MergeSort)")
    print("3. Sort by Product in alphabetical order (Bubble sort)")
    sort_choice = input("Choose a method (1-3): ")  # Inviter l'utilisateur a choisir une methode de tri en saissant un chiffre (1, 2 ou 3)
    return sort_choice

# Option 1 : Afficher la liste de produits
def view_names():
    #prod_df = pd.DataFrame(columns=["ID", "P_name", "P_quantity", "P_price (in $/Kg)", "order_date"])  # Ouvre notre liste de produit avec le mode read
    #prod_df.to_csv(products_function, index=False)  # Lecture d'un fichier csv et convertion en dictionnaire Python
    #print("List of products : ")
    #The line below uses a file that is not opened
    #for row in reader:  # Parcours les lignes de donnees a partir du fichier csv
    #    print(row['P_name'])  # Montre la colonne avec les noms des produits uniquement
    #The below lines would print the product names.
    try:
        df = pd.read_csv('csv_files')
        print("List of products : ")
        for index, row in df.iterrows():
            print(row['P_name'])
    except FileNotFoundError:
        print("The products.csv file was not found")

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
    # Demande des détails du produit à l'utilisateur
    new_prod = input("Enter the name of a new product : ")
    new_quant = input("Enter its quantity : ")
    new_price = input("Enter its price (/kg) : ")
    new_expdate = input("Enter the expiration date (dd-mm-yy) : ")
    new_id = next_id()  # Defintion de l'ID du nouveau produit grace a la fonction next_id()
    new_row = [new_id, new_prod, new_quant, new_price, new_expdate]
    #The below line was incorrectly indented causing the error.
    prod_df = pd.DataFrame(columns=["ID", "P_name", "P_quantity", "P_price (in $/Kg)", "order_date"])  # Ouvre notre liste de produit avec le mode read

    prod_df.to_csv('csv_files', index=False, mode='a', header=not isfile('csv_files'))  # Lecture du fichier csv et convertion en dictionnaire Python
    # writer.writerow(new_row)
    print("New product added successfully.")
    prod_df = pd.DataFrame(columns=["ID", "P_name", "P_quantity", "P_price (in $/Kg)", "order_date"])  # Ouvre notre liste de produit avec le mode read
    prod_df.to_csv(products.csv, index=False)  # Lecture du contenu du fichier

# Option 3 : delete product row
def delete_product():
  row_to_delete = input("Enter the row you wish to delete.")
  try:  # Utilisation de try en cas d'erreurs du fichier
    df = pd.read_csv('csv_files')  # Changed from 'products_functions.py' to 'products.csv'
    reader = pd.DataFrame(open('csv_files'))  # Added open function to read the csv
    rows = [row for row in reader if row["P_name"] != row_to_delete]  # Définir les lignes qui ne correspondent pas à celle indiqué pour deletion
    #Fixed indentation of next line
    total_rows = len(df) # sum(1 for _ in open('products.csv'))  # Calcul du nombre total de lignes
    if len(rows) == 0 or len(rows) == total_rows:
      print(f"No row with Name = '{row_to_delete}' was found.")  # Indiqué si la ligne n'éxiste pas
      return
    #Fixed indentation and removed pd.DataFrame call on a string
    df = pd.read_csv('csv_files', 'w', newline='') as file:
      fieldnames = reader.fieldnames
      writer = csv.DictWriter(file, fieldnames=fieldnames)
      writer.writeheader()
      writer.writerows(rows)  # Réecrire liste sans la ligne définis pour deletion
    print(f"The product : {row_to_delete} has been deleted.")

  except FileNotFoundError:
    print(f"Error: The file '{produits}' does not exist.") #'produits' variable is not defined. You should use products.csv or the defined filename
  except KeyError:
    print(f"Error: The column 'P_name' does not exist in the file.")

# binary search
def binary_search() :
    product_name = input("Enter product name for search : ") # Demander quel produit à rechercher
    try :
        df = pd.read_csv('products.csv') # Changed from 'products_functions.py' to 'products.csv'
        with open('products.csv', 'r') as file: #Added open to read file. This was not opened previously
            reader = csv.DictReader(file) #Fixed indentation
            rows = sorted(reader, key=lambda row: row['P_name'].lower()) # Trier liste par la colonne 'P_name' avec sorted()
            # utliser lambda comme fonction anonyme pour convertir toutes les lettres en minuscule
        low, high = 0, len(rows) - 1 # Définir le champ de recherche
        # low : début de la list
        # high : fin de la liste
        while low <= high :
            mid = (low + high) // 2 # Calcul de l'index du milieu
            mid_name = rows[mid]['P_name'].lower() # Trouver la valeur de l'index du milieu
            if mid_name == product_name.lower() : # Vérifier si la valeur du mid est le produit cherché
              print(f"Product '{product_name}' found!")
              return rows[mid]
            elif mid_name < product_name.lower() :
                low = mid + 1
                # Si l'élément mid est inférieur a celui de la recherche, on réduit la partie fin de la liste
            else :
                high = mid - 1
                # Si l'élément mid est supérieur a celui de la recherche, on réduit la partie début de la liste
        print(f"Product '{product_name}' not found.") # Réponse si le produit n'est pas trouvé
        return None
    except FileNotFoundError :
        print(f"Error : products.csv not found") #'produits' variable is not defined. You should use products.csv or the defined filename # Erreur si le fichier n'est pas trouvé
        return None
    except KeyError :
        print("Error : column P_name was not found") # Erreur si la colonne n'est pas trouvée