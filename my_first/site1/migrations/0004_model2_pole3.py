# Generated by Django 4.1.2 on 2022-10-13 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0003_model2_remove_model1_pole2'),
    ]

    operations = [
        migrations.AddField(
            model_name='model2',
            name='pole3',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
