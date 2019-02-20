from django.db import models

CLASS_CHOICES = (
    ('a', 'Class A'),
    ('b', 'Class B (Secretin)'),
    ('c', 'Class C (Glutamate)'),
    ('d', 'Adhesion'),
    ('f', 'Frizzled'),
)


class Gpcr(models.Model):
    pdb_id = models.CharField(max_length=4)
    molecule = models.CharField(max_length=200, null=True)
    gpcr_class = models.CharField(max_length=1, choices=CLASS_CHOICES, null=True)
    organism = models.CharField(max_length=200, null=True)
    gene_name = models.CharField(max_length=20, null=True)
    # mapping_file


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
    affinity = models.FloatField(blank=True, null=True)
    # type
    # formula
