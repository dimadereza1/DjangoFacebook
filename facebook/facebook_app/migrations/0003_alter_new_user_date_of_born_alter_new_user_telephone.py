# Generated by Django 4.2.1 on 2023-07-21 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook_app', '0002_alter_new_user_date_of_born_alter_new_user_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_user',
            name='date_of_born',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='new_user',
            name='telephone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
