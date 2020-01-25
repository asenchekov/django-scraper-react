# Generated by Django 2.2 on 2020-01-24 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sku', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]
