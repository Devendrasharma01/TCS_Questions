# An automobile company manufactures both a two wheeler (TW) and a four wheeler (FW). A company manager wants to make the production of both types of vehicle according to the given data below:
#● 1st data, Total number of vehicle (two-wheeler + four-wheeler)=v
# ● 2nd data, Total number of wheels = W
# The task is to find how many two-wheelers as well as four-wheelers need to manufacture as per the given data.

def check_production(total_vehicles,total_wheels):
    if total_vehicles <= 0 or total_wheels <= 0:
        return {"Two Wheeler" : None, "Four Wheeler" : None}
    two_wheelers = (4 * total_vehicles - total_wheels) // 2
    four_wheelers = (total_wheels - 2 * total_vehicles) // 2
    if two_wheelers < 0 or four_wheelers < 0 :
        return {"Two Wheeler" : None, "Four Wheeler" : None}
    return {"Two Wheeler " : two_wheelers, "Four Wheelre" : four_wheelers}
    
no_vehicles = int(input("Enter the total number of vehicles: "))
no_wheels = int(input("Enter the total number of wheels: "))
production = check_production(no_vehicles,no_wheels)
print(production)