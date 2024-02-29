# Generated by Django 5.0.2 on 2024-02-29 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=20)),
                ('author_details', models.CharField(max_length=40)),
                ('book_title', models.CharField(max_length=30)),
                ('publication', models.DateField()),
                ('book_version', models.IntegerField()),
            ],
        ),
    ]