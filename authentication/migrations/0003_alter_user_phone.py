# Generated by Django 4.2.10 on 2024-02-23 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]