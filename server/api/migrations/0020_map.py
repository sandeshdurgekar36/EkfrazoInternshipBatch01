# Generated by Django 4.0.3 on 2022-06-29 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_register1_first_name_alter_register1_last_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
            ],
        ),
    ]
