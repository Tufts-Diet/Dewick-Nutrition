from random import randint
import fileinput
import copy
import json 

with open('data.json') as data_file:
	data = json.load(data_file)
#print 

#for k in range(0,20):
#	print data[k]




def Algorithm():
	desiredSodium 	= 1200
	desiredCalories = 1000
	desiredFat 	= 32.5
	desiredProtein 	= 25.0
	
	
	br_main = []
	br_side = []
	for food in data:
		if (food["cal"] >= 100 and  food["meal"] == 1):
			br_main.append(food)
		elif food["meal"] == 1:
			br_side.append(food)	
	br_sod = desiredSodium * .25
	br_cal = 400
	br_fat = desiredFat * .25
	br_pro = desiredProtein * .25
	br = []
	pos_br = []
	for food in br_main:
		br.append(food)
		for side in br_side:
			temp = food["cal"] + side["cal"]
#			print temp
			if(temp >= 350 and temp <= 450):
				br.append(side)
				pos_br.append(copy.deepcopy(br))
				br.pop()
		br.pop()
				
		
	offsets = []
	
	for meal in pos_br:
		off = 0.0
		sod = 0.0
		fat = 0.0
		pro = 0.0
#		print meal
		for food in meal:
			sod += food["sodium"]
			fat += food["fat"]
			pro += food["prot"]
				
	
	Breakfasts = dict()
	Dinners = dict()
	Lunches = dict()
	BigJson = dict()
	
	for mealTime in range (0,2):
		for mealType in range(0,2):

			meal = pos_br[randint(0,len(pos_br)-1)]
			main = meal[0]
			maincourse = []		
			maincourse.append(main["name"])
			maincourse.append(main["cal"])
			maincourse.append(main["fat"])
			maincourse.append(main["sodium"])
			maincourse.append(main["prot"])
			side = meal[1]
			sidedish = []
			sidedish.append(side["name"])
			sidedish.append(side["cal"])
			sidedish.append(side["fat"])
			sidedish.append(side["sodium"])
			sidedish.append(side["prot"])
			if(mealTime == 0):
				if(mealType == 0):
					lowcal = dict()
					lowcal["MainCourse"] = maincourse
					lowcal["SideDish"]   = sidedish
					Breakfasts["LowCal"] = lowcal
				elif(mealType == 1):
					medcal = dict()
					medcal["MainCourse"] = maincourse
					medcal["SideDish"]   = sidedish
					Breakfasts["MedCal"] = medcal
				elif(mealType == 2):
					highcal = dict()
					highcal['MainCourse'] = maincourse
					highcal["SideDish"]   = sidedish
					Breakfasts["HighCal"] = highcal
			elif(mealTime == 1):
				if(mealType == 0):
					lowcal = dict()
					lowcal["MainCourse"] = maincourse
					lowcal["SideDish"]   = sidedish
					Lunches["LowCal"] =lowcal
				elif(mealType == 1):
					medcal = dict()
					medcal["MainCourse"] = maincourse
					medcal["SideDish"]   = sidedish
					Lunches["MedCal"] =medcal
				elif(mealType == 2):
					highcal = dict()
					highcal["MainCourse"] = maincourse
					highcal["SideDish"]   = sidedish
					Lunches["HighCal"]= highcal
			elif(mealTime == 2):	
				if(mealType == 0):
					lowcal = dict()
					lowcal["MainCourse"] = maincourse
					lowcal["SideDish"]   = sidedish
					Dinners["LowCal"] = lowcal
				elif(mealType == 1):
					medcal = dict()
					medcal["MainCourse"] = maincourse
					medcal["SideDish"]   = sidedish
					Dinners["MedCal"] = medcal
				elif(mealType == 2):
					highcal = dict()
					highcal["MainCourse"] = maincourse
					highcal["SideDish"]   = sidedish
					Dinners["HighCal"] = highcal
		BigJson["Breakfast"] = Breakfasts
		BigJson["Lunch"] = Lunches
		BigJson["Dinner"] = Dinners
		with open('FoodImage.json','w') as f:
			json.dump(BigJson,f)
		
Algorithm()
	
	

