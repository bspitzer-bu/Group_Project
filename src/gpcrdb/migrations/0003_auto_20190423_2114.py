# Generated by Django 2.0.6 on 2019-04-23 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpcrdb', '0002_gpcr_gene_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gpcr',
            name='rmsd_values',
        ),
        migrations.AlterField(
            model_name='similarities',
            name='sequence',
            field=models.FloatField(null=True),
        ),
    ]
