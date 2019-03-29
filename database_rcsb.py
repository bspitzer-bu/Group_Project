#!/usr/bin/env python3
import urllib.request
import xml.etree.ElementTree as ET

pdbIDs= "2py1,4xt3"

customReportColumns = 'structureAuthor,classification,depositionDate,experimentalTechnique,resolution,structureTitle,' \
                      'ligandFormula,ligandId,ligandMolecularWeight,ligandName,ligandSmiles,EC50,IC50,Ka,Kd,Ki'


url="https://www.rcsb.org/pdb/rest/customReport.xml?pdbids={}&customReportColumns={},pubmedId,doi&primaryOnly=1&service=wsfile&format=csv"\
    .format(pdbIDs,customReportColumns)


f = urllib.request.urlopen(url)
result = f.read()


# saving the csv file
with open('rcsb.csv', 'wb') as f2:
    f2.write(result)

# This is where Lucas needs to parse the data into something useable