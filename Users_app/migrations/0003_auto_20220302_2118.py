# Generated by Django 3.0.5 on 2022-03-02 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users_app', '0002_customuser_terms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('HO', 'Hostel Owner'), ('HS', 'Hostel Seeker')], max_length=2),
        ),
    ]
