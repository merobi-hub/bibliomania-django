# Generated by Django 3.2.7 on 2021-10-19 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(default=0)),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.tweet')),
            ],
        ),
    ]
