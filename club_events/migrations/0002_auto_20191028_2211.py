# Generated by Django 2.2.6 on 2019-10-28 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='First & Last Name: ')),
                ('phone_number', models.CharField(max_length=30, verbose_name='Phone Number: ')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=50)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='tickets',
            field=models.ManyToManyField(to='club_events.Ticket'),
        ),
    ]
