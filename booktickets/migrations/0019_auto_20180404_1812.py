# Generated by Django 2.0.1 on 2018-04-04 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktickets', '0018_auto_20180404_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seatallocation',
            name='show',
        ),
        migrations.RemoveField(
            model_name='showmovie',
            name='theatre',
        ),
        migrations.RemoveField(
            model_name='theatre',
            name='movie',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.DeleteModel(
            name='SeatAllocation',
        ),
        migrations.DeleteModel(
            name='ShowMovie',
        ),
        migrations.DeleteModel(
            name='Theatre',
        ),
    ]
