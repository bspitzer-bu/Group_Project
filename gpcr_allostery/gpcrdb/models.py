from django.db import models

# Create your models here.

from django.db import models

class GPCR(models.Model):
    pdb_id = models.CharField(max_length=4)



class Ligand(models.Model):
    lig_id = models.CharField(max_length=3)
    name = models.CharField(max_length=100)