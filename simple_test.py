f1=open('./FoodInfo.json', 'w+')
f1.write('\
{"Breakfast":{\
  "LowCal":{\
    "MainCourse": ["Chicken Pattie", "325", "1", "5", "2"],\
    "SideDish": ["Italian Salad", "254", "5", "2", "4"]},\
  "MedCal":{\
    "MainCourse": ["Chicken Nugget", "275", "4", "8", "19"],\
    "SideDish": ["Unmedicated Pastrami", "86", "0", "31", "2"]},\
  "HighCal":{\
    "MainCourse": ["Big Mama", "666", "3", "2", "1"],\
    "SideDish": ["More Pastrami", "86", "0", "31", "22"]}\
  },\
\
"Lunch":{\
  "LowCal":{\
    "MainCourse": ["Chicken Pattie", "325", "1", "5", "2"],\
    "SideDish": ["Italian Salad", "254", "5", "2", "4"]},\
  "MedCal":{\
    "MainCourse": ["Chicken Nugget", "275", "4", "8", "19"],\
    "SideDish": ["Unmedicated Pastrami", "86", "0", "31", "2"]},\
  "HighCal":{\
    "MainCourse": ["Big Mama", "666", "3", "2", "1"],\
    "SideDish": ["More Pastrami", "86", "0", "31", "22"]}\
  },\
\
"Dinner":{\
  "LowCal":{\
    "MainCourse": ["Chicken Pattie", "325", "1", "5", "2"],\
    "SideDish1": ["Italian Salad", "254", "5", "2", "4"],\
    "SideDish2": ["Another Salad", "223", "5", "8", "1"]},\
  "MedCal":{\
    "MainCourse": ["Chicken Nugget", "275", "4", "8", "19"],\
    "SideDish1": ["Unmedicated Pastrami", "86", "0", "31", "2"],\
    "SideDish2": ["Another Salad", "223", "5", "8", "1"]},\
  "HighCal":{\
    "MainCourse": ["Big Mama", "666", "3", "2", "1"],\
    "SideDish1": ["More Pastrami", "86", "0", "31", "22"],\
    "SideDish2": ["Another Salad", "223", "5", "8", "1"]}\
  }\
 }')