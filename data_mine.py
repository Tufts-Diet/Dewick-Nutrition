from bs4 import BeautifulSoup
import urllib
import re
r = urllib.urlopen('http://menus.tufts.edu/foodpro/shortmenu.asp?sName=Tufts%20Dining&locationNum=11&locationName=Dewick-MacPhie%20Dining%20Center&naFlag=1').read()
soup = BeautifulSoup(r)

result = soup.find_all(onmouseover = "window.status = 'Click for Nutritive Analysis.'; return true;")

for meal in result:
	print("http://menus.tufts.edu/foodpro/" + meal.get('href'))