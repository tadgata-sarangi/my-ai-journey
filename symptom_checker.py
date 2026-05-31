symptom2 = input("Enter your symptoms. ")
symptom3 = input("Enter your symptoms. ")
symptom1 = input("Enter your symptoms. ")

symptoms = symptom1 + " and " + symptom2 + " and " + symptom3

if(symptoms == "fever and cough"):
    print("You See a doctor.")
elif(symptoms == "Nausea"):
    print("You Rest at home.")
else:
    print("Drink water.")