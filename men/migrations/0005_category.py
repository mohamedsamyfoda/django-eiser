# Generated by Django 3.0.8 on 2020-07-30 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('men', '0004_auto_20200730_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
