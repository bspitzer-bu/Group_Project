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

METHOD_CHOICES = (
    ('x', 'X-Ray Diffraction'),
    ('n', 'Solution NMR'),

)

class Gpcr(models.Model):
    pdb_id = models.CharField(max_length=4, unique=True)
    gpcr_name = models.CharField(max_length=250)
    gpcr_class = models.CharField(max_length=1, choices=CLASS_CHOICES, null=True)
    subfamily = models.CharField(max_length=250)
    uniprot_id = models.CharField(max_length=250)
    species = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    method = models.CharField(max_length=1, choices=METHOD_CHOICES)
    resolution = models.FloatField(null=True)
    pubmed_id = models.IntegerField(null=True)
    deposition_date = models.DateField(null=True)
    modification_date = models.DateField(null=True)
    rmsd_values = models.ManyToManyField('self', through="Similarities", symmetrical=False)
    raw_pdb_file = models.FileField(upload_to='raw_pdbs/', null=True)
    mapping_pdb_file = models.FileField(upload_to='mapped_pdb/', null=True)

    def save(self, force_insert=False, force_update=False):
        self.pdb_id = self.pdb_id.upper()
        super(Gpcr, self).save(force_insert, force_update)

    def __unicode__(self):
        return self.someAttr


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
