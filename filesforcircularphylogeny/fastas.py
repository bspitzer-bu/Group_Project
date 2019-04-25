import sys
import csv
import os

usage = ''' python 
'''


list_of_files = []

# read in a csv file of pdb_id, pk and stick in dict
f = open('list_of_fastas.txt', 'r')
for line in f:
    list_of_files.append(line.strip())
f.close()


for file in list_of_files:
    pdb_id = file.split('/')[2].split('.')[0]
    print('>{}'.format(pdb_id))
    fasta = open('/home/awake/Dropbox/BE768/group_project/src/{}'.format(file), 'r')
    f_text = fasta.read()
    print(f_text)




