f1=open('./FoodInfo.json', 'w+')
f1.write('\
  {"Meals":[\
  {"BreakfastLowCal":[\
    {"MainCourse": "Chicken Pattie",\
     "SideDish": "Italian Salad",\
     "Dessert": "Cake"\
     }]\
  },\
  {"BreakfastMedCal":[\
    {"MainCourse": "Fried Eggs",\
     "SideDish": "Bacon and Potatoes",\
     "Drink": "Lemon-infused Water"\
    }]\
  }]})')