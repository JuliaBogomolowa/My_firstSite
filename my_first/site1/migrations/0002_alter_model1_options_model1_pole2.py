# Generated by Django 4.1.2 on 2022-10-13 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='model1',
            options={'verbose_name': 'Модель', 'verbose_name_plural': 'Модели'},
        ),
        migrations.AddField(
            model_name='model1',
            name='pole2',
            field=models.IntegerField(default=''),
            preserve_default=False,
        ),
    ]
