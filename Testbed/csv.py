# csv.py
""" Play wtih csv files """

import csv

data = [
    [100, "Jones", 24.98],
    [200, "Doe", 345.67],
    [300, "White", 0.0],
    [400, "Stone", -42.16],
    [500, "Rich", 224.62]
]

with open("Testbed/data.csv", 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerows(data)

df = pd.read_csv("Testbed/data.csv", names = ['account', 'name', 'balance'])
print(df)