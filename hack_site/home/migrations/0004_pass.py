# Generated by Django 5.0.6 on 2024-05-11 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_merge_0002_category_vendor_0002_pointofinterest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('county', models.CharField(max_length=100)),
            ],
        ),
    ]