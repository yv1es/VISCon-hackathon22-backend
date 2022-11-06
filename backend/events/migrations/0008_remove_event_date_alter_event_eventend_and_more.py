# Generated by Django 4.1.2 on 2022-10-15 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_merge_0005_merge_20221015_1623_0006_alter_tag_iconurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.AlterField(
            model_name='event',
            name='eventEnd',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventStart',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='registrationEnd',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='registrationStart',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
