import sys
import os

if len(sys.argv) <= 1:
    print('usage: python pdb2fasta.py file_list.txt ')
    exit()

input_file = open(sys.argv[1])

for line in input_file:
    os.system('python pdb2fasta.py {}'.format(line.strip()))

input_file.close()
