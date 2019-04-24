import sys
import csv

usage = ''' python swap_id_for_pk.py reference.csv original.csv output.csv | upload a file to have the pdb_id colummns 
switched with the GPCR PK
'''

if len(sys.argv) < 3:
    print(usage)

# read in a csv file of pdb_id, pk and stick in dict
f = open(sys.argv[1], 'r')
pdbid_pk = dict(filter(None, csv.reader(f)))
f.close()

# replace pdb_id with the pk and write to new file
with open(sys.argv[2]) as original:
    with open(sys.argv[3], 'w') as new_main:
        input_data = original.read()
        for key, value in pdbid_pk.items():
            input_data = input_data.replace(key, value)
        new_main.write(input_data)
