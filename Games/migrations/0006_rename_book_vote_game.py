# Generated by Django 4.1.3 on 2022-11-22 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0005_vote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='book',
            new_name='game',
        ),
    ]
