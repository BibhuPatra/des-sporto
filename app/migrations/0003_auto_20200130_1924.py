# Generated by Django 3.0.2 on 2020-01-30 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_institute'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute',
            name='age_group',
            field=models.CharField(default='25-20 years', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institute',
            name='category',
            field=models.CharField(default='Football Academy', max_length=100),
            preserve_default=False,
        ),
    ]
