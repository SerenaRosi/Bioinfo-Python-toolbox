import csv
import json
import argparse
import re

final_dict = {}

parser = argparse.ArgumentParser(description="""

From 'csv' to JSON

    """, formatter_class= argparse.RawTextHelpFormatter)

parser.add_argument('--input_file', '-i',
                    type = str,
                    required = True,
                    help='''Name of the input file
                     ''')


args = parser.parse_args()

# Get parameters
if not re.search(".csv", args.input_file):
    input_file = str(args.input_file + ".csv")
else:
    input_file = str(args.input_file)
    
with open(input_file, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t') ### CHANGE DELIMITER IF NECESSARY 
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





