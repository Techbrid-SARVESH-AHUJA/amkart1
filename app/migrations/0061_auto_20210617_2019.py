# Generated by Django 3.1.4 on 2021-06-17 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0060_remove_mobile_phone_current_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mobile_phone',
            old_name='model_embed',
            new_name='model_embed_1',
        ),
    ]
