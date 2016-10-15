from bs4 import BeautifulSoup
import urllib
import re
r = urllib.urlopen('http://menus.tufts.edu/foodpro/shortmenu.asp?sName=Tufts%20Dining&locationNum=11&locationName=Dewick-MacPhie%20Dining%20Center&naFlag=1').read()
soup = BeautifulSoup(r)

result = soup.find_all(onmouseover = "window.status = 'Click for Nutritive Analysis.'; return true;")

for meal in result:
	print(meal.get('href'))

longmenu.asp?sName=Tufts+Dining&locationNum=11&locationName=Dewick%2DMacPhie+Dining+Center&naFlag=1&WeeksMenus=This+Week%27s+Menus&dtdate=10%2F15%2F2016&mealName=Dinner

