# Generated by Django 3.2.5 on 2022-09-28 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220928_2124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='modified_at',
        ),
    ]
