# Generated by Django 3.1.4 on 2021-06-14 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0043_delete_mobile_phones'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile_phone',
            name='model_embed',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='mobile_phone',
            name='spec_1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='mobile_phone',
            name='spec_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='mobile_phone',
            name='spec_3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='mobile_phone',
            name='spec_4',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='mobile_phone',
            name='spec_5',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
