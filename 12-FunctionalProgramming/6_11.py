test_results = [
   {"name":"Peter","result":27},
   {"name":"Anna","result":63},
   {"name":"Robert","result":92},
   {"name":"Paul","result":46},
   {"name":"Barbara","result":52}]
between = filter(lambda student: 70>=student['result']>=50, test_results)
for student in between:
    print(student['name'])