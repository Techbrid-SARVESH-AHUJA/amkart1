# Generated by Django 3.1.4 on 2021-06-16 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0053_contact_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_name', models.CharField(max_length=50, null=True)),
                ('Class', models.FloatField(max_length=10, null=True)),
                ('Father_name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='contact_form',
        ),
    ]
