#!/usr/bin/env python3
import urllib
import xml.etree.ElementTree as ET

"""This file takes a PDB ID and a chain. It then goes to the RCSB and pulls out any sequences with 
100% sequence similarity and returns a list"""

PATH = "/home/awake/Dropbox/Vajda_Lab/as_bench_set"
pdb_id = "1SUG"
pdb_chain = "A"
sim_list = []


pdb_n_chain = '{}.{}'.format(pdb_id, pdb_chain)
url = 'http://www.rcsb.org/pdb/rest/sequenceCluster?cluster=%d&structureId=%s' % (100, pdb_n_chain)

f = urllib.urlopen(url)
result = f.read()
root = ET.fromstring(result)

for pdbchain in root.iter('pdbChain'):
    sim_list.append(pdbchain.attrib['name'])
print(sim_list)
