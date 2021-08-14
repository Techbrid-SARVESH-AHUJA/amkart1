# Generated by Django 3.1.4 on 2021-06-13 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_bedsheet'),
    ]

    operations = [
        migrations.CreateModel(
            name='clock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to='static')),
                ('price', models.IntegerField(max_length=200, null=True)),
                ('size', models.CharField(max_length=200, null=True)),
                ('type', models.CharField(max_length=200, null=True)),
                ('mechanism', models.CharField(max_length=200, null=True)),
                ('company', models.CharField(max_length=200, null=True)),
                ('design', models.CharField(max_length=200, null=True)),
                ('style', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]