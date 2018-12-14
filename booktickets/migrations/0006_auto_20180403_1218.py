# Generated by Django 2.0.1 on 2018-04-03 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booktickets', '0005_auto_20180403_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showmovie',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie', to='booktickets.Movie'),
        ),
        migrations.AlterField(
            model_name='showmovie',
            name='theatre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theatre', to='booktickets.Theatre'),
        ),
    ]
