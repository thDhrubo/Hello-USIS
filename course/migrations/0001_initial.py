# Generated by Django 3.2.15 on 2022-09-26 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('psd', models.CharField(max_length=164)),
                ('ayear', models.CharField(max_length=6)),
                ('asession', models.CharField(max_length=10)),
                ('course', models.CharField(max_length=7)),
            ],
        ),
    ]
