# Generated by Django 4.0.5 on 2022-06-15 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('team_id', models.CharField(max_length=20)),
                ('bot_user_id', models.CharField(max_length=20)),
                ('bot_access_token', models.CharField(max_length=100)),
            ],
        ),
    ]
