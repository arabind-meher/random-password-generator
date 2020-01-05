import csv

with open('password.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([1, 2, 4])
