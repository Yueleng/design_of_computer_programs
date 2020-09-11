udacity_tas = ['Peter', 'Andy', 'Sarah', 'Gudenga', 'Jon', 'Sean']

bad_uppercase_tas = []
for i in range(len(udacity_tas)):
    bad_uppercase_tas.append(udacity_tas[i].upper())
print(bad_uppercase_tas)

uppercase_tas = [name.upper() for name in udacity_tas]
print(uppercase_tas)

print()

ta_data = [('Peter', 'USA', 'CS262'),
           ('Andy', 'USA', 'CS212'),
           ('Sarah', 'England', 'CS101'),
           ('Gundega', 'Lativia', 'CS373'),
           ('Job', 'USA', 'CS387'),
           ('Sean', 'USA', 'CS253')]

ta_facts = [name + ' lives in ' + country + 'and is the ta for ' + course 
            for name, country, course in ta_data]
remote_facts_remotes = [name + ' lives in ' + country + 'and is the ta for ' + course 
            for name, country, course in ta_data if country != 'USA']

ta_300 = [name + ' is the TA for ' + course 
          for name, _ , course in ta_data if course.find('CS3') != -1]

for row in ta_facts:
    print(row)
print()

for row in remote_facts_remotes:
    print(row)
print()

for row in ta_300:
    print(row)
print()