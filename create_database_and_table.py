import sqlite3

connection = sqlite3.connect("databse.db")
c = connection.cursor()
c.execute('''CREATE TABLE dixhuit_vingtcinq(datetime text, nb_co real)''')
connection.commit()
connection.close()