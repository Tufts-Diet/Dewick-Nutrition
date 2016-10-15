from bs4 import BeautifulSoup
import urllib
import re
import string #########!

def removeNonAscii(s): return "".join(i for i in s if ord(i)<128)
#def removeBadDots(s): 
#	if s[0] == ".":
#		s[0] = ''
#	if s[len(s)-1] == '.':
#		s[len(s)-1] = ''


menu = urllib.urlopen('http://menus.tufts.edu/foodpro/shortmenu.asp?sName=Tufts%20Dining&locationNum=11&locationName=Dewick-MacPhie%20Dining%20Center&naFlag=1').read()
soup = BeautifulSoup(menu)

result = soup.find_all(onmouseover = "window.status = 'Click for Nutritive Analysis.'; return true;")
i = 0

for meal in result:
	i += 1
	l = urllib.urlopen("http://menus.tufts.edu/foodpro/" + meal.get('href')).read()
	soup_l = BeautifulSoup(l)
	foods = soup_l.find_all(onmouseover = "window.status = 'Click for label of this item.'; return true;")
	for food in foods:
		#print food.get('href')
		f = urllib.urlopen("http://menus.tufts.edu/foodpro/" + food.get('href')).read()
		soup_f = BeautifulSoup(f)
		bold = []
		font = []
		label = []
		
		label.append(soup_f.body.find('div').string)
#			label.append(removeBadDots(removeNonAscii(c.string)))
		for b in soup_f.find_all('hr'):
			thing1 = b.find_previous_sibling().string
			font.append(thing1)
		for a in soup_f.find_all('b'):
			bold.append(removeNonAscii(a.string))
		if len(font) == 0:
			break
		elif len(label) ==0:
			break
		bold[1] = bold[1][8:]
		bold[1] = int(bold[1])
		if bold[1] >= 50:	
			print label[0]
			print bold[1]
			print bold[7]
			font[18] = font[18][:-1]
			print font[18]
			font[20] = font[20][:-2]
			print font[20]
			print i
			print ""
		#for r in soup_f.find_all(font size="3" face="arial"):
		#	font.append(f)
		#	print f
		#nut = Nutrients
		#nut.cals = 
		


#class Nutrients:
#	cals = 0
#	fat = 0
#	sod = 0
#	prot = 0

