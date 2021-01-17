# Generated by Django 3.1.3 on 2021-01-06 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0004_auto_20201107_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('publications', models.ManyToManyField(to='quizes.Publication')),
            ],
            options={
                'ordering': ['headline'],
            },
        ),
    ]
