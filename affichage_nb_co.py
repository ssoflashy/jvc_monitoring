import sqlite3
import csv

connection = sqlite3.connect("database.db")
c = connection.cursor()
a = 0
for row in c.execute("SELECT * FROM dixhuit_vingtcinq"):
	print(row)
	a = a + 1
print(a)
c.execute("SELECT MAX(nb_co) FROM dixhuit_vingtcinq")
print(c.fetchone())
data = c.execute("SELECT * FROM dixhuit_vingtcinq")

with open("Output.csv", "w", newline='') as file:
	for i in data:
		a = data.fetchone()
		csv.writer(file).writerow(a)
connection.close()
