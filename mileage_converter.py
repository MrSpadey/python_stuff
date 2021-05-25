# User input, How many kilometers did you cycle today and covert to miles

print("How many Kilometres did you cycle today?")
km = input() # User input stored as km var
miles = float(km)/1.6093 # changes km to float, miles var is km/1.6093
miles = round(miles, 2) # rounds the miles var to 2 decimal points
print(f"Ok, you cycled {km}km today. Thats the same as {miles} miles.")
# 