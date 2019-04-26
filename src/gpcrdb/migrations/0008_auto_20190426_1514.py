# Generated by Django 2.1.5 on 2019-04-26 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gpcrdb', '0007_auto_20190426_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpcr',
            name='gene',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gene', to='gpcrdb.Gene'),
        ),
    ]
