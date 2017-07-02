#!/usr/bin/python3

from bs4 import BeautifulSoup
from time import sleep
import sqlite3
import datetime
import requests
import re



class Forum:

	def __init__(self, forum, url_forum):
		self.forum = forum
		self.url_forum = url_forum

		pattern = '([0-9]{1,5})'
		self.pattern = re.compile(pattern)

	def add_to_database(self):
		connection = sqlite3.connect("database.db")
		c = connection.cursor()
		now = datetime.datetime.today()
		nb_co = self.recup_co()

		text = "INSERT INTO {0}(datetime, nb_co) VALUES('{1}', '{2}')".format(self.forum, now, nb_co)
		c.execute(text)
		connection.commit()
		connection.close()

		print(now, self.forum, str(nb_co))
		sleep(1)

	def recup_co(self):
		r = requests.get(self.url_forum)
		page_html = str(r.text)
		page = BeautifulSoup(page_html, 'html.parser') 
		resultat = page.select(".nb-connect-fofo")

		nb_co = re.search(self.pattern, str(resultat))

		return nb_co.group(0)

def main():
	dixhuit_vingtcinq = Forum("dixhuit_vingtcinq", "http://www.jeuxvideo.com/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm")
	moins_quinze = Forum("moins_quinze", "http://www.jeuxvideo.com/forums/0-15-0-1-0-1-0-blabla-moins-de-15-ans.htm")
	quinze_dixhuit = Forum("quinze_dixhuit", "http://www.jeuxvideo.com/forums/0-50-0-1-0-1-0-blabla-15-18-ans.htm")
	overwatch = Forum("overwatch", "http://www.jeuxvideo.com/forums/0-33972-0-1-0-1-0-overwatch.htm")

	forums = [dixhuit_vingtcinq, moins_quinze, quinze_dixhuit, overwatch]

	while(True):
		for forum in forums:
			try:
				forum.add_to_database()
			except:
				print("An error occured with the forum '{0}' at {1}".format(forum.forum, datetime.datetime.today()))
				sleep(5)
		sleep(60)

main()