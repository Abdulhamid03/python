all = {'instructor': ['Ahmad', 'Abdul', 'Kris', 'Gulnaz', 'Esen'], 'members': ["Abdulhamid Abdullajonov", "Ahmadyar", "Aiya", "Esenbek", "Gulnaz", "Kris", "Marlen", "Meerim", "Mohammad", "Salmon", "Simon"]}

both = []


for person in range(len(all['instructor'])):
    inst = all['instructor'][person]
    if inst in all['members']:
        both.append(inst)
        all['members'].remove(inst)

        print(both)
        print(all['members'])