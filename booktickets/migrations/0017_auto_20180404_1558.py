# Generated by Django 2.0.1 on 2018-04-04 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktickets', '0016_auto_20180404_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showmovie',
            name='date',
            field=models.CharField(max_length=20),
        ),
    ]
