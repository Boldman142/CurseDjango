# Generated by Django 4.2 on 2024-02-28 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0009_alter_client_creator_alter_letter_creator_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletter',
            options={'ordering': ('status',), 'permissions': [('view_all_newsletter', 'Can view all newsletter')], 'verbose_name': 'рассылка', 'verbose_name_plural': 'рассылки'},
        ),
    ]
