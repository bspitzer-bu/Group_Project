# Generated by Django 2.1.5 on 2019-04-25 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gpcrdb', '0004_auto_20190424_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gene_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.RemoveField(
            model_name='gpcr',
            name='gene_name',
        ),
        migrations.AddField(
            model_name='gpcr',
            name='gene',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='gpcrdb.Gene'),
            preserve_default=False,
        ),
    ]