""" A doctor has a clinic where he serves his patients. The doctor’s consultation fees are different for different groups of patients depending on their age. If the patient’s age is below 17, fees is 200 INR. If the patient’s age is between 17 and 40, fees is 400 INR. If patient’s age is above 40, fees is 300 INR. 
Write a code to calculate earnings in a day for which one array/List of values representing age of patients visited on that day is passed as input. """

def calculate_earnings(patient_ages):

  total_income = 0
  max_patients = 20

  if len(patient_ages) > max_patients:
    return "INVALID INPUT: Maximum 20 patients allowed."

  for age in patient_ages:
    if age <= 0 or age > 120:
      return "INVALID INPUT: Age must be between 1 and 120."
    elif age < 17:
      total_income += 200
    elif age <= 40:
      total_income += 400
    else:
      total_income += 300

  return f"Total Income: {total_income} INR"


def main():

  patient_ages = []
  while True:
    age_str = input("Enter age value (press Enter without a value to stop): ")
    if not age_str:
      break
    try:
      age = int(age_str)
      patient_ages.append(age)
    except ValueError:
      print("INVALID INPUT: Please enter a valid integer.")

  earnings_message = calculate_earnings(patient_ages)
  print(earnings_message)


main()
