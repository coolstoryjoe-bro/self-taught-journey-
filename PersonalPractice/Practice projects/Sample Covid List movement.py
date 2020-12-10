covid_patients_0room = ['jason vorhees', 'ming ming', 'joe biden', 'donald trump', 'monopoly man',
                        'johnny depp', 'zeus', 'gavin newsom', 'iwatani naofumi', 'grid', 'jishuka',
                        'jenny tan', 'gulston dart', 'saiyad maqbool', 'alejandro riverra', 'lisa mountry',
                        'beatrice lopez']
covid_patients_1room = []
covid_patients_treated = []
covid_patients_recovering = []

print(covid_patients_0room)
while covid_patients_0room:
    moving_1 = covid_patients_0room.pop()
    print(f"Moving {moving_1.title()} to an ICU room.")
    covid_patients_1room.append(moving_1)
print(covid_patients_0room)
print("List of patiens in ICU rooms: ", covid_patients_1room)
while covid_patients_1room:
    moving_2 = covid_patients_1room.pop()
    print(f"\tTreating {moving_2.title()} from Covid-19.")
    covid_patients_treated.append(moving_2)
print(covid_patients_1room)
print("List of treated patients: ", covid_patients_treated)
while covid_patients_treated:
    moving_3 = covid_patients_treated.pop()
    print(f"\t\t{moving_3.title()} is recovering from Covid-19.")
    covid_patients_recovering.append(moving_3)
print(covid_patients_treated)
print("List of recovering patients: ", covid_patients_recovering)