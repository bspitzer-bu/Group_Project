# Generated by Django 2.1.5 on 2019-02-20 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpcrdb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gpcr',
            old_name='molecule',
            new_name='classification',
        ),
        migrations.AddField(
            model_name='gpcr',
            name='rcsb_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]