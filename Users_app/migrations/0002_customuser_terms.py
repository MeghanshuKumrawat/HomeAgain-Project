# Generated by Django 3.0.5 on 2022-03-01 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='terms',
            field=models.BooleanField(default=False),
        ),
    ]