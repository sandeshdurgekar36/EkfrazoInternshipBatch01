# Generated by Django 4.0.3 on 2022-05-10 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_delete_django_user_alter_login1_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='badge',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='max_time_min',
            field=models.TimeField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='min_charge',
            field=models.FloatField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='Coupon_discount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='forgotpassword',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.register1'),
        ),
        migrations.AlterField(
            model_name='register1',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='validity_period',
            field=models.DurationField(null=True),
        ),
    ]