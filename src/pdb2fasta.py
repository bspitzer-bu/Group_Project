import sys

if len(sys.argv) <= 1:
    print('usage: python pdb2fasta.py file.pdb')
    exit()

input_file = open(sys.argv[1])
name = (sys.argv[1].split('/')[2][:-4])
print(name)

output_file = open('media/fastas/{}.fasta'.format(name), 'w')

letters = {'ALA': 'A', 'ARG': 'R', 'ASN': 'N', 'ASP': 'D', 'CYS': 'C', 'GLU': 'E', 'GLN': 'Q', 'GLY': 'G', 'HIS': 'H',
           'ILE': 'I', 'LEU': 'L', 'LYS': 'K', 'MET': 'M', 'PHE': 'F', 'PRO': 'P', 'SER': 'S', 'THR': 'T', 'TRP': 'W',
           'TYR': 'Y', 'VAL': 'V'}

current_residue = 0
fasta_sequence = ''

for line in input_file:
    columns = line.split()
    if len(columns) < 1:
        continue
    if columns[0] != 'ATOM':
        continue
    if int(columns[5]) > current_residue:
        fasta_sequence += letters[columns[3]]
    current_residue = int(columns[5])


input_file.close()
output_file.write(fasta_sequence)
output_file.close()
