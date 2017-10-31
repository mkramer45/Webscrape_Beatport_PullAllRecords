import bs4
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup 
import sqlite3

my_url = 'https://www.beatport.com/genre/tech-house/11/top-100'

# opening up connecting, grabbing the page
uClient = uReq(my_url)
# this will offload our content into a variable
page_html = uClient.read()
# closes our client
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("li",{"class":"bucket-item ec-item track"})

conn = sqlite3.connect('Beatscrape.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS BeatPortTechHouse(SongName TEXT)')

# MSK, artist name
for container in containers:
	song_Name = container["data-ec-name"]
	cursor.execute("INSERT INTO BeatPortTechHouse VALUES (?)", (song_Name,))

conn.commit()
cursor.close()
conn.close()

