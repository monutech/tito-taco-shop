# Generated by Django 4.0.5 on 2022-06-15 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='chat_type',
            field=models.CharField(choices=[('slack', 'Slack'), ('discord', 'Discord')], default='slack', max_length=25),
            preserve_default=False,
        ),
    ]
