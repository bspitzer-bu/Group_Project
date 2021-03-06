# Generated by Django 2.0.6 on 2019-04-24 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gpcrdb', '0003_auto_20190423_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ligand',
            name='gpcr',
        ),
        migrations.AlterField(
            model_name='binds',
            name='gpcr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gpcrdb.Gpcr', to_field='pdb_id'),
        ),
        migrations.AlterField(
            model_name='binds',
            name='ligand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gpcrdb.Ligand', to_field='lig_id'),
        ),
    ]
