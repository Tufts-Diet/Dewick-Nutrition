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
  },\
\
  "Highlights":{\
    "Breakfast":{\
      "Food1":["Fried Eggs", "info1", "info2", "info3", "info4"],\
      "Food2":["Bacon", "info1", "info2", "info3", "info4"],\
      "Food3":["Baguettes", "info1", "info2", "info3", "info4"],\
      "Food4":["Watermelon", "info1", "info2", "info3", "info4"],\
      "Food5":["Yummy Potatoes", "info1", "info2", "info3", "info4"]\
    },\
    "Lunch":{\
      "Food1":["Swordfish", "info1", "info2", "info3", "info4"],\
      "Food2":["Yogurt", "info1", "info2", "info3", "info4"],\
      "Food3":["Colored Goldfish", "info1", "info2", "info3", "info4"],\
      "Food4":["Mozzerella sticks", "info1", "info2", "info3", "info4"],\
      "Food5":["Sandwiches", "info1", "info2", "info3", "info4"]\
    },\
    "Dinner":{\
      "Food1":["Mac n Cheese", "info1", "info2", "info3", "info4"],\
      "Food2":["Teriyaki Beef", "info1", "info2", "info3", "info4"],\
      "Food3":["Way too much rice", "info1", "info2", "info3", "info4"],\
      "Food4":["Potatoes", "info1", "info2", "info3", "info4"],\
      "Food5":["Slightly stale chicken", "info1", "info2", "info3", "info4"]\
    }}\
 }')