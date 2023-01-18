import csv
import json

final_dict = {}

with open('DATABASE_CAS_new_all.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            header = row
            line_count += 1
        else:

            for index, record in enumerate(row):

                if index == 0:

                    first_index = row[index]
                    final_dict[first_index] = {}

                else:

                    final_dict[first_index][header[index]] = row[index]

with open('database.json', 'w') as f:
    json.dump(final_dict, f, indent=2)



