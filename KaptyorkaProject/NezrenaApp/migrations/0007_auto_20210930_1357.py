# Generated by Django 3.2.7 on 2021-09-30 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NezrenaApp', '0006_rename_profile_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipment',
            old_name='subtype',
            new_name='path',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='type',
        ),
    ]
