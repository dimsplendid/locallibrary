# Generated by Django 3.2.5 on 2021-10-27 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_author_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': (('can_edit_book', 'Edit books'),)},
        ),
    ]
