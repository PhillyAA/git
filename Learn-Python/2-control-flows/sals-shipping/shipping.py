weight = 50

#Ground shipping
if weight  <= 2:
    cost_ground = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20

#Ground shipping premium
cost_ground_premium = 125

#Drone shipping
if weight  <= 2:
    cost_drone = weight * 4.5
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25

print("Drone shipping costs: $" , cost_drone)
print("Ground Shipping costs: $", cost_ground)
print("Premium Ground Shipping costs: $", cost_ground_premium)

#Lowest cost check

lowest_cost = min(cost_drone, cost_ground, cost_ground_premium)

if lowest_cost == cost_drone:
   print("Drone shipping is the cheapest, the price is: $" , cost_drone)
elif lowest_cost == cost_ground:
   print("Ground shipping is the cheapest, the price is: $" , cost_ground)
else:
   print("Ground shipping premium is the cheapest, which is: $", cost_ground_premium)