# Generated by Django 3.0 on 2020-07-24 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('Game_id', models.AutoField(primary_key=True, serialize=False)),
                ('Game_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('Users_id', models.AutoField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=50)),
                ('Create_time', models.DateTimeField(auto_now_add=True)),
                ('Games', models.CharField(max_length=50)),
            ],
        ),
    ]
