# Generated by Django 4.2.4 on 2023-08-07 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timg', models.ImageField(upload_to='pics')),
                ('tname', models.CharField(max_length=250)),
                ('tdesc', models.TextField()),
            ],
        ),
    ]
