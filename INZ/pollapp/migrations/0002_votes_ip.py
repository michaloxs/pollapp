# Generated by Django 2.2.5 on 2020-03-28 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pollapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Votes_ip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_ip', models.GenericIPAddressField()),
                ('Voted_question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pollapp.Question')),
            ],
        ),
    ]
