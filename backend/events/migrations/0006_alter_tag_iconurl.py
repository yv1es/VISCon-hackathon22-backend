# Generated by Django 4.1.2 on 2022-10-15 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_merge_20221015_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='iconUrl',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
