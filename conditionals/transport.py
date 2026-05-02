
dist = 45

if dist <=3:
  transport = "Walk"    
elif dist > 3 and dist <= 10:
  transport = "Bike"    

elif dist > 10 and dist <= 50:
  transport = "Car"


print(transport)