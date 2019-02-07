from django.db import models


class Gpcr(models.Model):
    pdb_id = models.CharField(max_length=4)


class Ligand(models.Model):
    lig_id = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    gpcr = models.ManyToManyField(
        Gpcr,
        through='Binds',
    )


class Binds(models.Model):
    gpcr = models.ForeignKey(Gpcr, null=True, on_delete=models.CASCADE)
    ligand = models.ForeignKey(Ligand, null=True, on_delete=models.CASCADE)
    affinity = models.FloatField(null=True)
