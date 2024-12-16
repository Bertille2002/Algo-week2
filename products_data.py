### Création d'un fichier pour enregistrer nos données###
import csv

data = [
    [1,"pomme","5","18.2","12-05-24"],
    [2,"oeuf","9","43.1","27-12-24"],
    [3,"pasta","27","1.05","18-10-27"],
    [4, "riz", "15", "2.3", "01-08-25"],
    [5, "lait", "8", "0.99", "15-02-24"],
    [6, "fromage", "20", "5.5", "30-11-24"]
]

with open('produits.csv', 'w', newline='') as file :
    writer = csv.writer(file)
    field = ["ID","P_name", "P_quantity", "P_price (in $/Kg)", "expiration_date"]
    writer.writerow(field)
    writer.writerows(data)

with open('produits.csv', 'r', newline='') as file :
  content = file.read()
  print(content)