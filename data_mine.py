from bs4 import BeautifulSoup
import urllib
import re
menu = urllib.urlopen('http://menus.tufts.edu/foodpro/shortmenu.asp?sName=Tufts%20Dining&locationNum=11&locationName=Dewick-MacPhie%20Dining%20Center&naFlag=1').read()
soup = BeautifulSoup(menu)

result = soup.find_all(onmouseover = "window.status = 'Click for Nutritive Analysis.'; return true;")

for meal in result:
	l = urllib.urlopen("http://menus.tufts.edu/foodpro/" + meal.get('href')).read()
	soup_l = BeautifulSoup(l)
	foods = soup_l.find_all(onmouseover = "window.status = 'Click for label of this item.'; return true;")
	for food in foods:
		#print food.get('href')
		f = urllib.urlopen("http://menus.tufts.edu/foodpro/" + food.get('href')).read()
		soup_f = BeautifulSoup(f)
		bold = []
		font = []
		for b in soup_f.find_all('font'):
			strip_tags(b)
			bold.append(b)
			print b
		#for r in soup_f.find_all(font size="3" face="arial"):
		#	font.append(f)
		#	print f
		#nut = Nutrients
		#nut.cals = 
		


class Nutrients:
	cals = 0
	fat = 0
	sod = 0
	prot = 0

from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

