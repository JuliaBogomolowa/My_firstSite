# Generated by Django 4.1.2 on 2022-10-13 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0005_remove_model2_pole2'),
    ]

    operations = [
        migrations.AddField(
            model_name='model2',
            name='pole2',
            field=models.IntegerField(default=' '),
            preserve_default=False,
        ),
    ]
