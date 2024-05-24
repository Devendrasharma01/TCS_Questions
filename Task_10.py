""" A washing machine works on the principle of the Fuzzy System, the weight of clothes put inside it for washing is uncertain. But based on weight measured by sensors, it decides time and water level which can be changed by menus given on the machine control area. For low level water, the time estimate is 25 minutes, where approximately weight is between 2000 grams or any nonzero positive number below that.
For medium level water, the time estimate is 35 minutes, where approximately weight is between 2001 grams and 4000 grams.
For high level water, the time estimate is 45 minutes, where approximately weight is above 4000 grams. """

def estimate_wash_time(weight):
  if weight < 0 or weight > 7000:
    return "INVALID INPUT"
  elif weight == 0:
    return "Time Estimated: 0 minutes"
  elif weight <= 2000:
    return f"Time Estimated: 25 minutes (Low Water Level)"
  elif weight >= 2001 and weight <= 4000:
    return f"Time Estimated: 35 minutes (Medium Water Level)"
  else:
    return f"Time Estimated: 45 minutes (High Water Level)"


weight = int(input("Enter weight of clothes (grams): "))
wash_time_message = estimate_wash_time(weight)

if wash_time_message != "INVALID INPUT":
  print(wash_time_message)
else:
  print("Error:", wash_time_message)
