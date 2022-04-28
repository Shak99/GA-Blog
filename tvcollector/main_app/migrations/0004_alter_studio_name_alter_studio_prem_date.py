# Generated by Django 4.0.4 on 2022-04-27 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_studio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studio',
            name='name',
            field=models.CharField(choices=[('A', 'Universal Studios'), ('B', 'Paramount'), ('C', 'Netflix'), ('D', 'Dreamworks'), ('E', 'Disney'), ('F', 'Lionsgate')], default='A', max_length=250),
        ),
        migrations.AlterField(
            model_name='studio',
            name='prem_date',
            field=models.DateField(verbose_name='Premiere Date'),
        ),
    ]
