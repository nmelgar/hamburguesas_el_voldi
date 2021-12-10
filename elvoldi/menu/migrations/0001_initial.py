# Generated by Django 4.0 on 2021-12-10 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('H', 'Hamburguesa'), ('P', 'Papas'), ('B', 'Bebida')], max_length=1)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('cost', models.IntegerField(max_length=10)),
            ],
        ),
    ]
