# Generated by Django 5.1.6 on 2025-02-25 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0019_flippeddiscussion_is_resolved_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flippeddiscussion',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='flippedreply',
            options={'ordering': ['date']},
        ),
        migrations.RenameField(
            model_name='flippedreply',
            old_name='reply',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='flippeddiscussion',
            name='replied_by',
        ),
    ]
