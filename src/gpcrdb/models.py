from django.db import models

CLASS_CHOICES = (
    ('a', 'Class A'),
    ('b', 'Class B (Secretin)'),
    ('c', 'Class C (Glutamate)'),
    ('d', 'Adhesion'),
    ('f', 'Frizzled'),
)

BINDING_CHOICES = (
    ('i', 'Ki'),
    ('d', 'Kd'),
    ('m', 'Km'),
    ('e', 'EC50'),
    ('z', 'IC50'),
)


class Gpcr(models.Model):
    pdb_id = models.CharField(max_length=4, unique=True)
    gpcr_class = models.CharField(max_length=1, choices=CLASS_CHOICES, null=True)
    gene_name = models.CharField(max_length=20, null=True)
    resolution = models.FloatField(null=True)
    pubmed_id = models.IntegerField(null=True)
    deposition_date = models.DateField(null=True)
    modification_date = models.DateField(null=True)
    rcsb_link = models.URLField(null=True, blank=True)
    rmsd_values = models.ManyToManyField('self', through="Similarities",symmetrical=False)



class Ligand(models.Model):
    lig_id = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=100)
    smiles = models.CharField(max_length=250)
    mol_weight = models.FloatField()
    gpcr = models.ManyToManyField(
        Gpcr,
        through='Binds',
    )


class Binds(models.Model):
    gpcr = models.ForeignKey(Gpcr, null=True, on_delete=models.CASCADE)
    ligand = models.ForeignKey(Ligand, null=True, on_delete=models.CASCADE)
    affinity = models.FloatField(blank=True, null=True)
    affinity_type = models.CharField(max_length=1, choices=BINDING_CHOICES, null=True)


class Similarities(models.Model):
    gpcr1 = models.ForeignKey(Gpcr, on_delete=models.CASCADE, related_name='gpcr1')
    gpcr2 = models.ForeignKey(Gpcr, on_delete=models.CASCADE, related_name='gpcr2')
    rmsd = models.FloatField()
    sequence = models.FloatField()


