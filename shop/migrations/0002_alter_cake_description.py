# Generated by Django 4.0.5 on 2022-06-05 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
