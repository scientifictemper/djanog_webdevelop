# Generated by Django 3.2.2 on 2021-05-12 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=250)),
                ('address', models.CharField(max_length=50)),
                ('jobrole', models.CharField(max_length=50)),
            ],
        ),
    ]
