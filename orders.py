import csv 

orders_alice = [
    [1,"pomme","5","18.2","12-05-24"],
    [2,"oeuf","9","43.1","27-12-24"],
    [3,"pasta","27","1.05","18-10-27"],
    [4, "riz", "15", "2.3", "01-08-25"],
    [5, "lait", "8", "0.99", "15-02-24"],
    [6, "fromage", "20", "5.5", "30-11-24"]
]

with open('orders_alice.csv', 'w', newline='') as file :
    writer = csv.writer(file)
    field = ["ID","P_name", "P_quantity", "P_price (in $/Kg)", "order_date"]
    writer.writerow(field)
    writer.writerows(orders_alice)

orders_jean = [
    [1,"Lutin","6","21.8","22-06-24"],
    [2,"Ananas","12","6.99","27-12-24"],
    [3,"Chocolat","27","1.05","01-06-27"],
    [4, "Whisky", "5", "89.99", "03-11-40"],
    [5, "Chips", "7", "1.65", "17-12-26"],
    [6, "olives", "9", "5.5", "29-01-24"]
]

with open('orders_jean.csv', 'w', newline='') as file :
    writer = csv.writer(file)
    field = ["ID","P_name", "P_quantity", "P_price (in $/Kg)", "order_date"]
    writer.writerow(field)
    writer.writerows(orders_jean)

orders_simon = [
    [1,"poires","10","15.5","16-12-24"],
    [2,"lardons","3","5.45","28-02-25"],
    [3,"Mozzarella","101","1.05","14-03-25"],
    [4, "huîtres", "30", "45.99", "29-12-24"],
    [5, "salades", "8", "2.50", "15-02-24"],
    [6, "thym", "4", "7.5", "30-11-26"]
]

with open('orders_simon.csv', 'w', newline='') as file :
    writer = csv.writer(file)
    field = ["ID","P_name", "P_quantity", "P_price (in $/Kg)", "order_date"]
    writer.writerow(field)
    writer.writerows(orders_simon)

orders_chloe = [
    [1,"pesto","3","5.55","23-08-25"],
    [2,"morbier","2","14.75","29-02-24"],
    [3,"linguine","5","1.15","05-05-27"],
    [4, "saumon", "1", "25.30", "01-01-25"],
    [5, "clémentines", "16", "6.99", "13-01-24"],
    [6, "poulet", "2", "15.25", "24-02-25"]
]

with open('orders_chloe.csv', 'w', newline='') as file :
    writer = csv.writer(file)
    field = ["ID","P_name", "P_quantity", "P_price (in $/Kg)", "order_date"]
    writer.writerow(field)
    writer.writerows(orders_chloe)

orders_maddie = [
    [1,"Café","4","8.15","12-09-26"],
    [2,"Poivrons","4","4.50","17-12-24"],
    [3,"Huile d'olive","3","15.69","29-07-29"],
    [4, "Crevettes", "30", "34.99", "11-01-25"],
    [5, "Litchi", "45", "9.99", "25-01-25"],
    [6, "Frites", "2", "7.5", "14-03-25"]
]

with open('orders_maddie.csv', 'w', newline='') as file :
    writer = csv.writer(file)
    field = ["ID","P_name", "P_quantity", "P_price (in $/Kg)", "order_date"]
    writer.writerow(field)
    writer.writerows(orders_maddie)

orders_aaron = [
    [1,"Raisins","4","10.15","05-11-24"],
    [2,"Entrecote","3","14.99","20-01-25"],
    [3,"Parmesan","5","5.99","19-03-25"],
    [4, "Carottes", "10", "4.95", "23-12-24"],
    [5, "Dessert", "12", "3.84", "19-03-25"],
    [6, "Crème Fraiche", "4", "6.15", "25-12-24"]
]

with open('orders_aaron.csv', 'w', newline='') as file :
    writer = csv.writer(file)
    field = ["ID","P_name", "P_quantity", "P_price (in $/Kg)", "order_date"]
    writer.writerow(field)
    writer.writerows(orders_aaron)