# Generated by Django 2.1 on 2018-09-02 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webClass', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='description',
            field=models.CharField(default='null', max_length=400),
            preserve_default=False,
        ),
    ]
