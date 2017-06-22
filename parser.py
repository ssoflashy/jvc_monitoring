#!/usr/bin/python3

from bs4 import BeautifulSoup
from urllib.request import urlopen
from time import sleep
import sqlite3
import datetime



class Forum():

	def __init__(self, forum, url_forum):
		self.forum = forum
		self.url_forum = url_forum

	def add_to_database(self):
		connection = sqlite3.connect("database.db")
		c = connection.cursor()
		self.now = datetime.datetime.today()
		self.text = "INSERT INTO {0}(datetime, nb_co) VALUES('{1}', '{2}')".format(self.forum, self.now, self.recup_co())
		print(self.forum, self.recup_co())
		c.execute(self.text)
		connection.commit()
		connection.close()
		sleep(5)

	def recup_co(self):
		self.page_html = str(urlopen(self.url_forum).read()) # stockage du contenu de la page dans une variable

		self.page = BeautifulSoup(self.page_html, 'html.parser') 
		self.resultat = self.page.select(".nb-connect-fofo")

		self.nb_co = str(self.resultat) #stockage de la ligne avec le nombre de co

		self.nb_co = self.nb_co[:-27] #modification de la ligne pour ne garder que le nb de co
		self.nb_co = self.nb_co[31:]
		
		return self.nb_co

dixhuit_vingtcinq = Forum("dixhuit_vingtcinq", "http://www.jeuxvideo.com/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm")
moins_quinze = Forum("moins_quinze", "http://www.jeuxvideo.com/forums/0-15-0-1-0-1-0-blabla-moins-de-15-ans.htm")
quinze_dixhuit = Forum("quinze_dixhuit", "http://www.jeuxvideo.com/forums/0-50-0-1-0-1-0-blabla-15-18-ans.htm")
overwatch = Forum("overwatch", "http://www.jeuxvideo.com/forums/0-33972-0-1-0-1-0-overwatch.htm")
while(True):
	dixhuit_vingtcinq.add_to_database()
	moins_quinze.add_to_database()
	quinze_dixhuit.add_to_database()
	overwatch.add_to_database()
	sleep(60)