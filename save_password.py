import csv

with open('newfile.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.appedrow([1, 2, 4])
