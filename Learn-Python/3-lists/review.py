inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

#Assign variable to length of list
inventory_len = len(inventory)

#Assign variable to first item in list
first = inventory[0]

#Assign variable to last item in list
last = inventory[-1]

#Assign variable to a list of items from index 2 upto but not including index 6
inventory_2_6 = inventory[2:6]

#Assign variable to the first 3 items of list
first_3 = inventory[:3]

#Assign variable to number of "twin bed" occurances in list
twin_beds = inventory.count("twin bed")

#Assign variable to list removing element 5 OR index 4
removed_item = inventory.pop(4)

#Insert new string into list as element 11 or index 10
inventory.insert(10, "19th Century Bed Frame")

#Sort list in alpabetical order // replaces old list
inventory.sort()
print(inventory)

#OR

#Displays a sorted list as new variable
inventory_sorted = sorted(inventory)
print(inventory)