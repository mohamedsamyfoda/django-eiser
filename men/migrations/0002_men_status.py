# Generated by Django 3.0.8 on 2020-07-30 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('men', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='men',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('Not available', 'Not available')], default='', max_length=15),
            preserve_default=False,
        ),
    ]
