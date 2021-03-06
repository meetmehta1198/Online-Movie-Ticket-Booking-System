# Generated by Django 2.0.1 on 2018-04-05 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booktickets', '0023_auto_20180405_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theatre_Map',
            fields=[
                ('map_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dates', to='booktickets.ShowMovie')),
                ('theatre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theatres', to='booktickets.Theatre')),
            ],
        ),
    ]
