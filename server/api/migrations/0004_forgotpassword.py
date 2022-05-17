# Generated by Django 4.0.3 on 2022-05-06 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_resetpassword'),
    ]

    operations = [
        migrations.CreateModel(
            name='forgotpassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.register1')),
            ],
        ),
    ]
