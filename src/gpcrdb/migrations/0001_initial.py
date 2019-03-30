# Generated by Django 2.1.5 on 2019-02-20 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Binds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affinity', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gpcr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdb_id', models.CharField(max_length=4, unique=True)),
                ('molecule', models.CharField(max_length=200, null=True)),
                ('gpcr_class', models.CharField(choices=[('a', 'Class A'), ('b', 'Class B (Secretin)'), ('c', 'Class C (Glutamate)'), ('d', 'Adhesion'), ('f', 'Frizzled')], max_length=1, null=True)),
                ('organism', models.CharField(max_length=200, null=True)),
                ('gene_name', models.CharField(max_length=20, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('resolution', models.FloatField(null=True)),
                ('exp_method', models.CharField(max_length=200, null=True)),
                ('pubmed_id', models.IntegerField(null=True)),
                ('deposition_date', models.DateField(null=True)),
                ('modification_date', models.DateField(null=True)),
                ('authors', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ligand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lig_id', models.CharField(max_length=3, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('gpcr', models.ManyToManyField(through='gpcrdb.Binds', to='gpcrdb.Gpcr')),
            ],
        ),
        migrations.AddField(
            model_name='binds',
            name='gpcr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gpcrdb.Gpcr'),
        ),
        migrations.AddField(
            model_name='binds',
            name='ligand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gpcrdb.Ligand'),
        ),
    ]