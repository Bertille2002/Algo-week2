import csv
import pandas as pd 

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
  sort_choice = input("Choose a method (1-3): ") # Inviter l'utilisateur a choisir une methode de tri en saissant un chiffre (1, 2 ou 3)
  return sort_choice

# Option 1 : Afficher la liste de produits 
def view_names() :
  with open(produits, 'r') as file : # Ouvre notre liste de produit avec le mode read 
    reader = csv.DictReader(file) # Lecture d'un fichier csv et convertion en dictionnaire Python 
    print("List of products : ")
    for row in reader : # Parcours les lignes de donnees a partir du fichier csv 
      print(row['P_name']) # Montre la colonne avec les noms des produits uniquement 

# Option 2 : Ajouter un nouveau produit 

# Defintion de l'ID du nouveau produit, Permet d'avoir un ID unique pour chaque produit
def next_id() : 
  with open(produits,'r',newline='') as file : # Ouvre notre liste de produit avec le mode read
    reader = csv.reader(file)
    rows = list(reader)
    last_row = rows[-1]
    last_id = int(last_row[0]) # Trouver la derniere ID dans la liste
    return last_id + 1 # résultat : ID pour nouveau produit

# Ajout du nouveau produit dans la liste
def new_product() : 
  # Demande des détails du produit à l'utilisateur 
  new_prod = input("Enter the name of a new product : ") 
  new_quant = input("Enter its quantity : ") 
  new_price = input("Enter its price (/kg) : ") 
  new_expdate = input("Enter the expiration date (dd-mm-yy) : ") 
  new_id = next_id() # Defintion de l'ID du nouveau produit grace a la fonction next_id()
  new_row = [new_id,new_prod,new_quant,new_price,new_expdate] # Définition de la nouvelle ligne dans la liste
  with open(produits, 'a', newline='') as file :
    writer = csv.writer(file) # Lecture du fichier csv et convertion en dictionnaire Python 
    writer.writerow(new_row) 
  print("New product added successfully.")
  with open(produits, 'r', newline='') as file :
    content = file.read() # Lecture du contenu du fichier 
    print(content)

# Option 3 : delete product row
def delete_product() :
  row_to_delete = input("Enter the row you wish to delete.")
  try : # Utilisation de try en cas d'erreurs du fichier 
    with open(produits, 'r') as file : 
      reader = csv.DictReader(file)
      rows = [row for row in reader if row["P_name"] != row_to_delete] # Définir les lignes qui ne correspondent pas à celle indiqué pour deletion
    with open(produits,'r') as file : 
      total_rows = sum(1 for _ in file) # Calcul du nombre total de lignes
    if len(rows) == 0 or len(rows) == total_rows - 1 :
      print(f"No row with Name = '{row_to_delete}' was found.") # Indiqué si la ligne n'éxiste pas
      return
    with open(produits, 'w', newline='') as file :
      fieldnames = reader.fieldnames
      writer = csv.DictWriter(file, fieldnames=fieldnames)
      writer.writeheader()
      writer.writerows(rows) # Réecrire liste sans la ligne définis pour deletion
    print(f"The product : {row_to_delete} has been deleted.")

  except FileNotFoundError:
    print(f"Error: The file '{produits}' does not exist.")
  except KeyError:
    print(f"Error: The column 'P_name' does not exist in the file.")

# binary search
def binary_search() :
    product_name = input("Enter product name for search : ") # Demander quel produit à rechercher 
    try :
        with open(produits, 'r') as file :
            reader = csv.DictReader(file)
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
        print(f"Error : {produits} not found") # Erreur si le fichier n'est pas trouvé
        return None
    except KeyError :
        print("Error : column P_name was not found") # Erreur si la colonne n'est pas trouvée

# load data 
def load_data(filename):
  data = []
  with open(filename, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Ignorer la ligne header
    for row in reader:
      data.append(row)
  return data # Rendre uniquement les données de la liste

# quicksort quantity
def quicksort(data) :
  if len(data) <= 1 : # Si la liste a 1 ou moins d'elements, c'est deja trié
    return data
  else : 
    pi = data[0] # Choisir le pivot donc le premier element
    # Division de la liste en 2 sous-listes autour du pivot
    left = [x for x in data[1:] if x <= pi] # Comparaison des quantitées
    right = [x for x in data[1:] if x > pi] # Comparaison des quantitées
    return quicksort(left) + [pi] + quicksort(right) # Tri récursif des sous-listes et les combiner avec le pivot

def sorted_table(sorted_data) :
  print("Sorted Table by Quantity (Ascending):")
  for row in sorted_data:
    print(row)

# sorted_data = quicksort(data)

# merge sort price
def merge_sort(data, key_index) :
  if len(data) > 1 :
    mid = len(data) // 2 # Trouver le milieu la liste
    left_half = data[:mid]
    right_half = data[mid:]
    # Division de la liste
    merge_sort(left_half, key_index)
    merge_sort(right_half, key_index)
    i = j = k = 0 # Initialisation des indices 
    while i < len(left_half) and j < len(right_half) : #Fusionne les deux moitiées dans la liste principale
      if float(left_half[i][key_index]) < float(right_half[i][key_index]) : #Compare les valeurs sur la clé index
        data[k] = left_half[i] #Si la valeur de gauche est plus petite elle sera placée dans la liste déjà triée
        i += 1 # Bouge l'index de gauche en avant 
      else :
        data[k] = right_half[j] #Si la valeur de gauche est plus petite ou égale elle sera placée dans la liste triée
        j += 1 # Bouge l'index de droite en avant
      k += 1 #Avance l'index de la liste principale 
    while i < len(left_half) : #Si il reste des éléments dans la moitié de gauche, ils sont ajoutés dans la liste triée
      data[k] = left_half[i]
      i += 1
      k += 1
    while j < len(right_half) : #Si il reste des éléments dans le moitié de droite, ils seront ajoutés dans la liste triée
      data[k] = right_half[j]
      j += 1
      k += 1

# Option 5.3 : alphabetical bubble sort of product names
def sort_alphabetically(data) :
  n = len(data) # Trouver le nombre de lignes dans la bdd
  for i in range(n) : # Bubble sort sur colonne P_name
    for j in range(0, n - i - 1) : # Comparer les lignes adjacentes et échanger si l'ordre est mauvais
    # Boucle exécutée n-i-1 fois : les i derniers éléments sont déjà triés à chaque itération
      if data[j][1].lower() > data[j + 1][1].lower() : # Comparer les P_names aux positions j et j+1
        data[j], data[j + 1] = data[j + 1], data[j]  
        # Si le nom en j est superieur a celui en j+1 on les échange pour avoir l'ordre correct
  for row in data :
    print(row) # Tri terminé, affichage de la liste triée