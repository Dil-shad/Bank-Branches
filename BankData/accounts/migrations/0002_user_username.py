# Generated by Django 4.2.1 on 2023-06-10 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=1, max_length=150, unique=True),
            preserve_default=False,
        ),
    ]
